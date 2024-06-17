"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

import os

import pandas as pd


def load_excel(df: pd.DataFrame, output_folder: str, output_file_name: str):
    """
    Salva um DataFrame em um arquivo Excel no diretório especificado.

    :param df: pd.DataFrame - DataFrame a ser salvo
    :param output_folder: str - Caminho do diretório onde o arquivo será salvo
    :param output_file_name: str - Nome do arquivo Excel a ser salvo
    :raises PermissionError: Se não houver permissão para escrever no diretório
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, output_file_name)

    # Verificação explícita das permissões de escrita
    if not os.access(output_folder, os.W_OK):
        raise PermissionError(
            f"Não há permissão de escrita no diretório: {output_folder}"
        )

    df.to_excel(output_path, index=False)