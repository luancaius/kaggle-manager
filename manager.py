from service import Service

rootPath = '../../Kaggle'

compName = input("Type Kaggle competition name to Download:")

service = Service(compName, rootPath)
service.InitCompetition()

exit(0)
