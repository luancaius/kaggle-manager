import util


class Service:

    def __init__(self):
        self.rootPath = '../../Kaggle'
        self.filesToCopy = ['util.txt', 'main.txt', 'prepareData.txt',
                            'training.txt', 'tuning.txt', 'submission.txt']
        self.templatesFolder = 'templates'

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
        for filename in self.filesToCopy:
            util.copyFileTo(self.templatesFolder, filename, self.path_script)

    def InitCompetition(self):
        compName = input("Type Kaggle competition name:")
        self.compName = compName
        self.path = self.rootPath+'/'+compName
        self.DownloadData()
        self.CreateScripts()

    def ExecuteMain(self):
        compName = input("Type Kaggle competition name:")
        self.compName = compName

    def UploadSubmission(self, filename):
        command = 'kaggle competitions submission ' + \
            self.compName + ' -p '+self.path_submission

    def RunAndScore(self):
        filename = ExecuteMain()
        score = self.UploadSubmission(filename)
        return score
