import sys
import csv

students = []

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith('.csv'):
            sys.exit("Not a CSV file")

        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                first, last = split_the_name(row['name'])
                students.append({"first": first, "last": last, "house": row['house']})

        with open(f"{sys.argv[2]}", mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def split_the_name(full_name):
    last, first = full_name.split(',')
    return first.strip(), last.strip()


if __name__ == "__main__":
    main()
