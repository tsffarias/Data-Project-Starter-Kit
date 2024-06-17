# API Documentation

Abaixo, você encontrará detalhes sobre as funções e módulos do nosso projeto.

## Módulo **consolidador**

### extract

```python
def extract_excel(input_folder: str) -> List[pd.DataFrame]:
    """
    função para extrair dados de arquivos Excel de uma pasta data/imput e retornar uma lista de dataframes.

    args: input_folder (str): caminho da pasta com os arquivos

    return:  lista de dataframes
    """
```

### transform

```python
def transforma_em_um_unico(all_data: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de DataFrames em um único DataFrame consolidado.

    Args:
        data (list): Lista contendo DataFrames para consolidação.

    Returns:
        DataFrame: DataFrame consolidado.
    """
```

### load

```python
def load_excel(df: pd.DataFrame, output_folder: str, output_file_name: str):

    """
    Salva um DataFrame em um arquivo Excel no diretório especificado.

    :param df: pd.DataFrame - DataFrame a ser salvo
    :param output_folder: str - Caminho do diretório onde o arquivo será salvo
    :param output_file_name: str - Nome do arquivo Excel a ser salvo
    :raises PermissionError: Se não houver permissão para escrever no diretório
    """
```

### consolidate_excels

```python
def pipeline_completa(input_folder: str, output_folder: str, output_file_name: str) -> None:
    """
    Função para consolidar múltiplos arquivos Excel em um único arquivo.

    Args:
        input_folder (str): Pasta contendo arquivos Excel.
        output_folder (str): Pasta onde o arquivo consolidado será salvo.
        output_file_name (str): Nome do arquivo Excel consolidado.

    Returns:
        None
    """
```
