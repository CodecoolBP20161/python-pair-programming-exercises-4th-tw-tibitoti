import csv
import sys
from person import Person


def open_csv(file_name):
    data_list
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.append(Person(row[0], row[1]))
    print (data_list)

def get_csv_file_name(argv_list):
    # implent this function
    pass  # delete this


def format_output(person):
    # implent this function
    pass  # delete this


def get_person_by_phone_number(person_list, user_input_phone_number):
    # implent this function
    pass  # delete this


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))
open_csv(file_name)
if __name__ == '__main__':
    main()
