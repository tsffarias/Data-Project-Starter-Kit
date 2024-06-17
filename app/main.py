"""pipeline principal do projeto."""

from pipeline import pipeline_completa

input_folder = "data/input"
output_folder = "data/output"


def consolidate_files():
    """Consolida os arquivos Excel gerados em um único arquivo."""
    output_file_name = "consolidated_absenteeism_data.xlsx"
    pipeline_completa(input_folder, output_folder, output_file_name)


if __name__ == "__main__":
    consolidate_files()
