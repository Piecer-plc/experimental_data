import csv

def read_csv_and_calculate_avg(csv_file_path):
    # Initialize dictionaries to store counts for different ranges
    ranges = {
        "[1, 10)": 0,
        "[10, 50)": 0,
        "[50, 100)": 0,
        "[100, 500)": 0,
        "[500, 10000000)": 0,
    }

    total_values = 0

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if len(row) >= 2:
                value = int(row[1].strip())
                total_values += value

                # Assign the value to the corresponding range
                if value < 10:
                    ranges["[1, 10)"] += 1
                elif value < 50:
                    ranges["[10, 50)"] += 1
                elif value < 100:
                    ranges["[50, 100)"] += 1
                elif value < 500:
                    ranges["[100, 500)"] += 1
                else:
                    ranges["[500, 10000000)"] += 1

    # Calculate the average
    if total_values == 0:
        avg = 0
    else:
        avg = total_values / sum(ranges.values())

    return ranges, avg
def calculate_numbers_greater_than_avg(csv_file_path, avg):
    numbers_greater_than_avg = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if len(row) >= 2:
                value = int(row[1].strip())
                if value >= int(avg):
                    numbers_greater_than_avg.append(value)

    return len(numbers_greater_than_avg)

# Example usage
csv_file_paths = ["Data Collection ML Library combinations.csv",
"Data Cleaning ML Library combinations.csv",
"Feature Engineering ML Library combinations.csv",
"Model Training ML Library combinations.csv",
"Model Evaluation ML Library combinations.csv",
"DataOriented ML Library combinations.csv",
"Model Oriented ML Library combinations.csv"]


for path in csv_file_paths:
    ranges, avg = read_csv_and_calculate_avg(path)
    print("Counts for different ranges:", ranges)
    print("Average:", avg)
    print("Common:",calculate_numbers_greater_than_avg(path,avg))
