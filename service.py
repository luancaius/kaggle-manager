import util


class Service:

    def __init__(self):
        self.path = '../../Kaggle'

    def DownloadData(self, compName):
        print("Downloading data")
        self.newPath = self.path+'/'+compName
        util.createDir(self.newPath)
        command = 'kaggle competitions download ' + compName+' -p '+self.newPath
        util.execute(command)

    def CreateFirstScript(self, competition):
        print("Making submission")

    def InitCompetition(self):
        compName = input("Type Kaggle competition name:")
        self.DownloadData(compName)
        self.CreateFirstScript(self.newPath)

    def RunScript(self, scriptPath, settings):
        print("Running script")
        pass
