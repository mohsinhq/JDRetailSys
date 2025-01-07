from openpyxl import Workbook, load_workbook

wb = load_workbook(filename = 'db.xlsx')
shoeSheet=wb['Sheet1']
shoeSheet['B9'].value = 'WOOO'

wb.save(filename='db.xlsx')
print(shoeSheet['B2'].value)