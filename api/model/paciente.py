from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time,DEATH_EVENT

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    age = Column("age", Integer)
    anae = Column("anaemia", Integer)
    crea = Column("creatinine_phosphokinase", Integer)
    diab = Column("diabetes", Integer)
    ejec = Column("ejection_fraction", Integer)
    high = Column("high_blood_pressure", Integer)
    plate = Column("platelets", Float)
    ser_crea = Column("serum_creatinine", Float)
    ser_sodi = Column("serum_sodium", Integer)
    sex = Column("sex", Integer)
    smok = Column("smoking", Integer)
    tim = Column("tim", Integer)
    death = Column("death", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, anae:int, crea:int, plate:float, name:str, age:int,
                 diab:int, ejec:int, high:int, ser_crea:float,ser_sodi:int,
                 smok:int, sex:int,tim:int, death:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
            name: nome do paciente
            age: idade
            anae: anemia - Decrease of red blood cells or hemoglobin (boolean)
            crea: creatina fosfoquinase - Level of the CPK enzyme in the blood (mcg/L)
            diab: diabetes
            ejec: fração de ejeção - Percentage of blood leaving the heart at each contraction (percentage)
            high: pressão sanguínea alta - If the patient has hypertension (boolean)
            plate: plaquetas - Platelets in the blood (kiloplatelets/mL)
            ser_crea: creatinina sérica - Level of serum creatinine in the blood (mg/dL)
            ser_sodi: soro sódio - Level of serum sodium in the blood (mEq/L)
            sex: sexo
            smok: fuma
            time: tempo - Follow-up period (days)
            death: diagnóstico
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name=name
        self.anae = anae
        self.crea = crea
        self.plate = plate
        self.age = age
        self.diab = diab
        self.ejec = ejec
        self.high = high
        self.ser_crea = ser_crea
        self.ser_sodi = ser_sodi
        self.smok = smok
        self.sex = sex
        self.tim = tim        
        self.death = death

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao