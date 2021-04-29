import os
import shutil
import time
def main():
    deletedFolders=0
    deletedFiles=0
    path="/pathToDelete"
    days=1
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folders,files in os.walk(path):
            if seconds>=getfileorfolderh(rootFolder): 
                removeFolder(rootFolder)
                deletedFolders+=1
                break
            else:
                for folder in folders: 
                    folderPath=os.path.join(rootFolder,folder)
                    if seconds>=getfileorfolderh(folderPath):
                        removeFolder(folderPath)
                        deletedFolders+=1
                for file in files: 
                    filePath=os.path.join(rootFolder,file)
                    if seconds>=getfileorfolderh(filePath):
                        removeFile(filePath)
                        deletedFiles+=1
        else:
            if seconds>=getfileorfolderh(path):
                removefile(path)
                deletedFiles+=1
    else:
        print("File Not Found")
        deletedFiles+=1
    print("Total Number of Folders Deleted: ", deletedFolders)
    print("Total Number of Files Deleted: ", deletedFiles)
def removeFolder(path):
    if not shutil.rmtree(path):
        print("Folder Removed Successfully")
    else:
        print("Cannot Delete Folder")
def removeFile(path):
    if not os.remove(path): 
        print("File Removed Successfully")
    else:
        print("Cannote Delete File")
def getfileorfolderh(path):
    ctime=os.stack(path).st_ctime
    return ctime
if __name__=='__main__':
    main()