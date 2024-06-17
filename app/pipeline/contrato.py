from pydantic import BaseModel, PositiveFloat, PositiveInt, validator
from datetime import datetime

class AbsenteeismSchema(BaseModel):
    """
    Modelo de dados para as absenteeism.
    """
    Colaborador_id: PositiveFloat
    Colaborador_nome: str
    Departamento: str
    Motivo_da_ausência: str
    Horas_de_ausência: PositiveInt
    Data_da_ausência: datetime
    Salário: PositiveFloat
        