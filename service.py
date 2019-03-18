import kaggle
import os


class Service:

    def __init__(self):
        self.path = '../../Kaggle'

    def SendEmail(to, body):
        print("Sending email")

    def ReadSettings(path):
        print("Reading configuration")

    def DownloadData(competition):
        print("Download data")

    def InitialTemplate():
        compName = input("Type Kaggle competition name:")
        command = 'kaggle competitions download ' + compName+' '+self.path
        os.system(command)

    def MakeSubmission(competition):
        print("Making submission")

    def RunScript(scriptPath, settings):
        print("Running script")
        pass
