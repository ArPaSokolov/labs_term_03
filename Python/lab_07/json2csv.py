import json
import csv

input_file_name = str(input("Enter a JSON file name to convert to CSV: ")[:-5])
try:
    with open(f"{input_file_name}.json", "r") as json_f:
        data = json.load(json_f)
        print(f"{input_file_name}.json read")

        output_file_name = str(list(data.keys())[0])

    with open(f"{output_file_name}.csv", "w", newline='') as csv_f:
        writer = csv.writer(csv_f)

        for x in data:
            headers = data[x][0].keys()
            writer.writerow(headers)
            for i in range(len(data[x])-1):
                row = list()
                for header in data[x][i].keys():
                    row.append(data[x][i].get(header))
                writer.writerow(row)

        print(f"{output_file_name}.csv written")

except Exception as e:
    print(f"Error: {str(e)}")