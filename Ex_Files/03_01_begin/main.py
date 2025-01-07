import csv
from pprint import pprint

PLANCK_CSV = 'Max,Planck,1858-04-23,1947-10-04,Schleswig (now Germany),in recognition of the services he rendered to the advancement of Physics by his discovery of energy quanta,physics,1918'

PLANCK = {
    "birthplace": "Schleswig (now Germany)",
    "name": "Max",
    "surname": "Planck",
    "born": "1858-04-23",
    "category": "physics",
    "motivation": "in recognition of the services...",
}

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Planck":
        pprint(laureate)
        break
