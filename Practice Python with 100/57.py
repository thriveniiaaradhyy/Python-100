from pprint import pprint
import json

with open("company1.json",'r') as file:
    d = json.loads( file.read())

pprint(d)    
