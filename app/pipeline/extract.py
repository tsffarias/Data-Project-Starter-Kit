"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os
from typing import List

import pandas as pd

path = "data/input/"

def extract_excel(input_folder: str) -> List[pd.DataFrame]:
    """
    função para extrair dados de arquivos Excel de uma pasta data/imput e retornar uma lista de dataframes.

    args: input_folder (str): caminho da pasta com os arquivos

    return:  lista de dataframes
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")
    all_data = [pd.read_excel(file) for file in files]
    return all_data

if __name__ == "__main__":
    data_frame_list = extract_excel(path)
    print(data_frame_list)
