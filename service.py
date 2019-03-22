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

    def CreateFirstScript():
        print("Creating first script")
        
    def InitCompetition(self):
        compName = input("Type Kaggle competition name:")
        self.DownloadData(compName)
        self.CreateFirstScript(self.newPath)

    def PreparingData(self):
        print("Preparing data")

    def TrainingAndTuning(self):
        print("Training and Tuning")

    def CreateSubmissionFile(self):
        print("Create submission")

    def UploadSubmission(self):
        print("Upload submission")
        return 10

    def RunAndScore(self):
        self.PreparingData()
        self.TrainingAndTuning()
        self.CreateSubmissionFile()
        score = self.UploadSubmission()
        return score
        