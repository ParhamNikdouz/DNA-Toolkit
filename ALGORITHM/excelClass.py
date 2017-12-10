from xlrd import open_workbook

####################################################################################
#Excel class                                                                      ##
#In this class you can open each excel file and you can save value of tuple in list#
#You can print values and get number of values in excel file                      ##
####################################################################################

class Excel:

    values = [] #In this  program is motif list

    #Open execl file
    def openExcel(self, addr):

        self.values.append('#') #Add space character !!!!!!
        wb = open_workbook(addr)

        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols

            for row in range(number_of_rows):
                for col in range(number_of_columns):
                    if (sheet.cell(row, col).value == ''):
                        continue
                    value = (sheet.cell(row, col).value)
                    try:
                        value = str(value)
                    except ValueError:
                        pass
                    finally:
                        self.values.append(value)

    #Print values/ in this program print motifs
    def printValues(self):
        print (self.values)

    #Print number of values/ in this program number of motifs
    def getNumberOfValues(self):
        print (len(self.values))
