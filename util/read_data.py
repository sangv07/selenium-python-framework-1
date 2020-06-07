import csv

def get_csv_data(file_name):
    # create an empty list ot store rows
    rows = []

    # open the csv file
    data_file = open(file_name, 'r')

    # create a CSV Reader from CSV file
    #col_list = ["course_name", "num", "exp,csv", "zip_cd"]

    reader = csv.reader(data_file)

    # skip the headers
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
