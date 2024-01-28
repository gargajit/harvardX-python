import sys
import csv
from tabulate import tabulate

data = []
headers = {}

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith('.csv'):
            sys.exit("Not a CSV file")

        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                #data = append_data(row)
                if sys.argv[1] == 'sicilian.csv':
                    data.append({"pizza": row['Sicilian Pizza'],"small": row['Small'],"large": row['Large']})
                else:
                    data.append({"pizza": row['Regular Pizza'],"small": row['Small'],"large": row['Large']})

        headers = {'pizza': 'Sicilian Pizza' if sys.argv[1] == 'sicilian.csv' else 'Regular Pizza', 'small': 'Small', 'large': 'Large'}
        table = table_format(data, headers)
        print(table)

    except FileNotFoundError:
        sys.exit("File does not exit")


def table_format(data, headers):
    return tabulate(data, headers, tablefmt="grid")


if __name__ == "__main__":
    main()
