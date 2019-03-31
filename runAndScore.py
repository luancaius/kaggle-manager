import util
import sys


class RunAndScore:

    def __init__(self, compName, rootPath):
        self.rootPath = rootPath
        self.compName = compName
        self.scriptPath = self.rootPath + '/'+self.compName
        sys.path.append(self.scriptPath)

    def UploadSubmission(self, absolutePath):
        command = 'kaggle competitions submission ' + absolutePath
        util.execute(command)

    def RunScript(self):
        import main
        main()

    def RunScriptAndGetScore(self):
        absolutePath = self.RunScript()
        score = self.UploadSubmission(absolutePath)
        return score
