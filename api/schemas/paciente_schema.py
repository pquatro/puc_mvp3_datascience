from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Fulano"
    anae: int = 1
    crea: int = 100
    plate: float = 200000
    age: int = 50
    diab: int = 0
    ejec: int = 20
    high: int = 1
    ser_crea: float = 2.0
    ser_sodi: int = 120
    smok: int = 1
    sex: int = 0
    tim: int = 3    
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Fulano"
    anae: int = 1
    crea: int = 100
    plate: float = 200000
    age: int = 50
    diab: int = 0
    ejec: int = 20
    high: int = 1
    ser_crea: float = 2.0
    ser_sodi: int = 120
    smok: int = 1
    sex: int = 0
    tim: int = 3    
    death: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Fulano"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Fulano"

class PacienteUpdateSchema(BaseModel):
    """ Define como um novo paciente pode ser atualizado.
    """
    id: int = 1
    name: str = "Fulano"    
    anae: int = 1
    crea: int = 100
    plate: float = 200000
    age: int = 50
    diab: int = 0
    ejec: int = 20
    high: int = 1
    ser_crea: float = 2.0
    ser_sodi: int = 120
    smok: int = 1
    sex: int = 0
    tim: int = 3    

# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,        
        "name": paciente.name,
        "anae": paciente.anae,
        "crea": paciente.crea,
        "plate": paciente.plate,
        "age": paciente.age,
        "diab": paciente.diab,
        "ejec": paciente.ejec,
        "high": paciente.high,
        "ser_crea": paciente.ser_crea,
        "ser_sodi": paciente.ser_sodi,
        "smok": paciente.smok,
        "sex": paciente.sex,
        "tim": paciente.tim,       
        "death": paciente.death
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "anae": paciente.anae,
            "crea": paciente.crea,
            "plate": paciente.plate,
            "age": paciente.age,
            "diab": paciente.diab,
            "ejec": paciente.ejec,
            "high": paciente.high,
            "ser_crea": paciente.ser_crea,
            "ser_sodi": paciente.ser_sodi,
            "smok": paciente.smok,
            "sex": paciente.sex,
            "tim": paciente.tim,       
            "death": paciente.death            

        })

    return {"pacientes": result}




   
