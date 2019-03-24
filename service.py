import util


class Service:

    def __init__(self):
        self.rootPath = '../../Kaggle'

    def DownloadData(self):
        print("Downloading data")
        util.createDir(self.path)
        self.path_data = self.path+'/data'
        util.createDir(self.path_data)
        command = 'kaggle competitions download ' + \
            self.compName + ' -p '+self.path_data
        util.execute(command)

    def CreateScripts(self):
        print("Creating scripts")
        self.path_script = self.path+'/script'
        util.createDir(self.path_script)
        self.path_submission = self.path+'/submission'
        util.createDir(self.path_submission)
        util.copyFileTo('templates', 'prepareData.txt', self.path_script)
        util.copyFileTo('templates', 'trainingAndTuning.txt', self.path_script)
        util.copyFileTo('templates', 'createSubmission.txt', self.path_script)

    def InitCompetition(self):
        compName = input("Type Kaggle competition name:")
        self.compName = compName
        self.path = self.rootPath+'/'+compName
        # self.DownloadData()
        self.CreateScripts()

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
