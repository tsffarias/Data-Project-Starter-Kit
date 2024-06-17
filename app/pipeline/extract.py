"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os
from typing import List
from .contrato import AbsenteeismSchema

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
    
    all_data = []
    for file in files:
        try:
            df = pd.read_excel(file)
            # Validação dos dados com Pydantic
            validated_data = [AbsenteeismSchema(**record) for record in df.to_dict(orient='records')]
            all_data.append(pd.DataFrame([data.dict() for data in validated_data]))
        except ValueError as ve:
            print(f"Erro de valor ao processar o arquivo {file}: {ve}")
        except Exception as e:
            print(f"Erro inesperado ao processar o arquivo {file}: {e}")
    
    if not all_data:
        raise ValueError("Nenhum dado válido foi extraído dos arquivos Excel")
    
    return all_data

if __name__ == "__main__":
    data_frame_list = extract_excel(path)
    print(data_frame_list)
