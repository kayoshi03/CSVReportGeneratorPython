import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Macro data report generator")

    parser.add_argument(
        "--files",
        nargs="+",              # позволяет передать несколько файлов
        required=True,
        help="Paths to CSV files"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report type"
    )

    return parser.parse_args()