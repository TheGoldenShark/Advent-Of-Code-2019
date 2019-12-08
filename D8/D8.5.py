import xlsxwriter
def toExcel(dimlist,name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    for i in range(0,len(dimlist)):
        for l in range(0,len(dimlist[i])):
            worksheet.write(i, l, (dimlist[i][l]))
    workbook.close()
with open("input.txt","r") as f: data=f.readline()[:-1]
x,y=25,6
n=x*y
# data=("0222112222120000")
# x,y=2,2
# n=x*y
layers = [list(data[i:i+n]) for i in range(0,len(data),n)]
output = ["2" for i in range(0,n)]
for i in range(0,n):
    for k in layers:
        if output[i]=="2":
            output[i]=k[i]
        else:
            break
final = [output[i:i+x] for i in range(0,len(output),x)]
toExcel(final,"final.xlsx")
