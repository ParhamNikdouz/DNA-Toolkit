from Algorithm.fileClass import File #Import File Class

################################################################################
#Sequence class                                                                #
#In this class you can analyze sequences in fasta file and add to sequence list#
#You can print sequences and get number of sequences in fasta file             #
################################################################################

class Sequence:

    sequences = []

    #Create sequence list
    def sequence(self, addr):
        f = File()
        fileContent = f.openFile(addr)

        line = ''
        meta = ''
        sequence = ''

        line = fileContent.readline()
        while line:
            line = line.rstrip('\n')
            if '>' in line:
                meta = line
            else:
                sequence = line
                self.sequences.append(sequence) #Append sequence to list
            line = fileContent.readline()
        return self.sequences

    #Print sequences
    def printSequences(self):
        print (self.sequences)

    def getNumberOfSequences(self):
        print (len(self.sequences))
