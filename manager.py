from service import Service
import json

with open('settings.txt') as f:
    settings = json.load(f)

compName = input("Type Kaggle competition name to Download:")
settings["compName"] = compName

service = Service(settings)
service.InitCompetition()

exit(0)
