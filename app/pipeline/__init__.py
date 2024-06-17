"""This module contains functions for the ETL process."""

from .extract import extract_excel
from .load import load_excel
from .pipeline import pipeline_completa
from .transform import transforma_em_um_unico
from .contrato import AbsenteeismSchema
