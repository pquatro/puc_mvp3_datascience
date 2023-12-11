from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Parada Cardíaca")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.
    
    Args:
        nome (str): nome do paciente
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    session = Session()
    
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:      

        name (str): nome do paciente
        age (int): idade
        anae (int): anemia - Decrease of red blood cells or hemoglobin (boolean)
        crea (int): creatina fosfoquinase - Level of the CPK enzyme in the blood (mcg/L)
        diab (int): diabetes
        ejec (int): fração de ejeção - Percentage of blood leaving the heart at each contraction (percentage)
        high (int): pressão sanguínea alta - If the patient has hypertension (boolean)
        plate (float): plaquetas - Platelets in the blood (kiloplatelets/mL)
        ser_crea (float): creatinina sérica - Level of serum creatinine in the blood (mg/dL)
        ser_sodi (int): soro sódio - Level of serum sodium in the blood (mEq/L)
        sex (int): sexo
        smok (int): fuma
        tim (int): tempo - Follow-up period (days)        
      
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/modelo_treinado.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    paciente = Paciente(
        name=form.name.strip(),
        anae=form.anae,
        crea=form.crea,        
        plate=form.plate,
        age=form.age,
        diab=form.diab,
        ejec=form.ejec,
        high=form.high,
        ser_crea=form.ser_crea,
        ser_sodi=form.ser_sodi,
        smok=form.smok,
        sex=form.sex,
        tim=form.tim,
        death=Model.preditor(modelo, form)        
    )
    logger.debug(f"Adicionando produto de nome: '{paciente.name}'")
   

    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == paciente.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{paciente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200
    

@app.post('/update_paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def update_paciente(form: PacienteUpdateSchema):
    """Edita um PAciente já salvo na base de dados

    Retorna uma representação dos Pacientes.
    """
    paciente_nome = form.name 
   


    try:                    

        # criando conexão com a base para verificar paciente
        session = Session()

         # fazendo a busca do paciente pelo id informado
        query = session.query(Paciente).filter(Paciente.name == paciente_nome)        
        db_paciente = query.first()      

        if not db_paciente:
            # se o paciente não foi encontrado
            error_msg = "Paciente não encontrado na base :/"            
            return {"mesage": error_msg}, 404
        else:

             # altera os campos do paciente
            db_paciente.anae = form.anae
            
            if form.crea:
                db_paciente.crea = form.crea

            if form.plate:
                db_paciente.plate = form.plate
            
            if form.age:
                db_paciente.age = form.age

            db_paciente.diab = form.diab

            if form.ejec:
                db_paciente.ejec = form.ejec

            db_paciente.high = form.high

            if form.ser_crea:
                db_paciente.ser_crea = form.ser_crea

            if form.ser_sodi:
                db_paciente.ser_sodi = form.ser_sodi
            
            db_paciente.smok = form.smok      

            db_paciente.sex = form.sex      

            if form.tim:
                db_paciente.tim = form.tim                            

            
            #atualiza o alimento
            session.add(db_paciente)
            session.commit()            
            return apresenta_paciente(db_paciente), 200        

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Paciente de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400  