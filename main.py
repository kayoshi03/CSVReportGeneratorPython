from cli import parse_args
from read import read_files
from tabulate import tabulate
from reports import REPORTS

def main():
    args = parse_args()

    if args.report not in REPORTS:
        raise ValueError(f"Unknown report: {args.report}")
    
    rows = read_files(args.files)

    report_class = REPORTS[args.report]
    report = report_class()

    table = report.generate(rows)
    print(tabulate(table, headers=report.title))

if __name__ == "__main__":
    main()