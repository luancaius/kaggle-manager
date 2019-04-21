from service import Service
import json
from pprint import pprint

rootPath = '../../Kaggle'

with open('settings.txt') as f:
    settings = json.load(f)

compName = input("Type Kaggle competition name to Download:")
settings["compName"] = compName

service = Service(settings)
service.InitCompetition()

exit(0)
