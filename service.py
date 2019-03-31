import util
import sys
from dataAndTemplate import DataAndTemplate
from runAndScore import RunAndScore


class Service:

    def __init__(self, compName):
        self.compName = compName
        self.rootPath = '../../Kaggle'

    def main(self, option):
        if option == 1:
            data = DataAndTemplate(self.compName, self.rootPath)
            data.InitCompetition()
        elif option == 2:
            run = RunAndScore(self.compName, self.rootPath)
            run.RunScriptAndGetScore()
