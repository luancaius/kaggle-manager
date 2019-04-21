import util
import sys


class Service:

    def __init__(self, compName, rootPath):
        self.compName = compName
        self.filesToCopy = ['util.txt', 'main.txt', 'prepareData.txt',
                            'training.txt', 'tuning.txt', 'submission.txt']
        self.templatesFolder = 'templates'
        self.rootPath = rootPath

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

    def ReplaceVariables(self):
        submissionFile = self.path_script+'/submission.py'
        util.replaceVariableInText(submissionFile, "@compName@", self.compName)

    def InitCompetition(self):
        print('Init competition')
        self.path = self.rootPath+'/'+self.compName
        self.DownloadData()
        self.CreateScripts()
        self.ReplaceVariables()
