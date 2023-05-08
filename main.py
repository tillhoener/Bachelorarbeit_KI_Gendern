import csv
import json

csv_file = 'C:\\Users\\tillhoener\\Downloads\\Datensatz_gendergerechte_Begriffe.csv'
jsonl_file = 'C:\\Users\\tillhoener\\Downloads\\data.jsonl'

data = []

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        prompt = row['Hauptwort']
        completion = row['Vorschlag']
        entry = {'prompt': prompt, 'completion': completion}
        data.append(entry)

with open(jsonl_file, 'w', encoding='utf-8') as file:
    for entry in data:
        json.dump(entry, file)
        file.write('\n')
