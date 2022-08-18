import csv
with open('venv/people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','ID','Gender'])
    writer.writerow(['Navya', '31266', 'F'])
    writer.writerow(['Lavanya', '31162', 'F'])
with open('venv/people.csv', 'r') as file:
    '''reader = csv.reader(file)
    for row in reader:
        print(row)'''
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))
file.close()