import json
with open('data/lastNames.json') as lastNamesJson:
    lastNames = json.load(lastNamesJson)['lastNames']

print(lastNames)