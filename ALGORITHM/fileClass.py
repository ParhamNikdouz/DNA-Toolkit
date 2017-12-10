####################################
#File class                        #
#This class Open and Print any file#
####################################


class File:

    fileAddress = ''

    #Open files
    def openFile(self, fileAddress):
        self.fileAddress = fileAddress #File address
        self.fileContent = open(self.fileAddress, 'r') #Open file
        return self.fileContent;

    #Print files
    def printFile(self):
        print(self.fileContent.read())

