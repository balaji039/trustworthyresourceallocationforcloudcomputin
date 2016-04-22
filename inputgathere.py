import openpyxl
class result:
    def computeresult(self,feed, avail, util, sec):
        wb = openpyxl.load_workbook('D:\\cloud\\Fuzzyrule.xlsx')
        sheet = wb.get_sheet_by_name('Sheet1')

        result = "LOW"

        for rowOfCellObjects in sheet['A2':'E82']:
            count = 1
            t = 0
            b = 0
            for cellObj in rowOfCellObjects:
                if count == 1:
                    if feed == cellObj.value:
                        #print cellObj.value, cellObj.coordinate
                        t = 1
                    else:
                        break
                elif count == 2:
                    if avail == cellObj.value:
                        #print cellObj.value, cellObj.coordinate
                        t = 1
                    else:
                        t = 0
                        break
                elif count == 3:
                    if util == cellObj.value:
                        #print cellObj.value, cellObj.coordinate
                        t = 1
                    else:
                        break
                elif count == 4:
                    if sec == cellObj.value:
                        #print cellObj.value, cellObj.coordinate
                        t = 1
                    else:
                        break
                elif count == 5:
                    if t == 1:
                        result = cellObj.value
                        #print cellObj.value,cellObj.coordinate
                        b = 1
                        break
                count = count + 1
            if b == 1:
                break
            count = 0
            t = 0
            b = 0
        return result

    def rangecalculator(self,text,avai):
        inp1= open(text,"r")
        range = 0.0
        range2 = 0.0
        te = 'L'
        res = "LOW"
        for line in inp1.readlines():
            ct = 0
            for i in line.split():
                if (ct == 0):
                    if i == 'L':
                        te = 'L'
                    elif i == 'M':
                        te = 'M'
                    else:
                        te = 'H'
                elif (ct == 1):
                    range = float(i)
                elif (ct == 2):
                    range2 = float(i)
                ct = ct + 1
            if te == 'L' and avai >= range and avai <= range2:
                res = "LOW"
                break
            elif te == 'M' and avai >= range and avai <= range2:
                res = "MEDIUM"
                break
            elif te == 'H' and avai >= range and avai <= range2:
                res = "HIGH"
                break
        return res

