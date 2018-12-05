import xlsxwriter

workbook = xlsxwriter.Workbook('reporte.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Item', bold)

expenses = (
['Rent', 1000],
['Gas',   100],
['Food',  300],
['Gym',    50],
)

# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total',       bold)

    workbook.close()
