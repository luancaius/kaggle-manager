import os
import shutil


def copyFileTo(src, filename, dst):
    shutil.copy(src+'/'+filename, dst)
    newfilename = os.path.splitext(filename)[0]+'.py'
    os.rename(dst+'/'+filename, dst+'/'+newfilename)


def createDir(folder):
    try:
        if not os.path.exists(folder):
            os.mkdir(folder)
    except OSError:
        print("Creation of the directory %s failed" % folder)
    else:
        print("Successfully created the directory %s " % folder)


def execute(command):
    os.system(command)
