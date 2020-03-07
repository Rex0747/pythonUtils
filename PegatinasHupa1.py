import openpyxl

book = openpyxl.load_workbook('pegatinas.xlsx')

sheet = book.active
sheet['A1'] = "HOLA"
sheet['A2'] = "PERIKO"

a1 = sheet['A1']
a2 = sheet['A2']
a3 = sheet.cell(row=3, column=1)

book.save('pegatinas.xlsx')

print(a1.value)
print(a2.value) 
print(a3.value)