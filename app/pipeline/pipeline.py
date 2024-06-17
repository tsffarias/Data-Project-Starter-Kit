"""This module contains functions for the ETL process."""

from .extract import extract_excel
from .load import load_excel
from .transform import transforma_em_um_unico


def pipeline_completa(input_folder: str, output_folder: str, output_file_name: str):
    """
    Função para consolidar múltiplos arquivos Excel em um único arquivo.

    Args:
        input_folder (str): Pasta contendo arquivos Excel.
        output_folder (str): Pasta onde o arquivo consolidado será salvo.
        output_file_name (str): Nome do arquivo Excel consolidado.

    Returns:
        None
    """
    data = extract_excel(input_folder)
    consolidated_df = transforma_em_um_unico(data)
    load_excel(consolidated_df, output_folder, output_file_name)
    print("Arquivo salvo com sucesso")
