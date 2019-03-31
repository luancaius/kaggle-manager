from service import Service

option = input("Download kaggle data competition: 1\nRun script: 2\n")
compName = input("Type Kaggle competition name:")

service = Service(compName)
service.main(int(option))

exit(0)
