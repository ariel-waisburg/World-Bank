import csv
import os

def write_to_csv(file_path, headers, data):
    old = os.path.exists(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        if not old:
            csv_writer.writerow(headers)
        for row in data:
            csv_writer.writerow(row)
    print("Data has been successfully written to", file_path)