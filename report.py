import xlsxwriter
from docx import Document
from Vulnerabilidad import *

class Report:

    def toExcel(vulnerabilidades,fileName):
        workbook = xlsxwriter.Workbook(fileName + '.xlsx')
        worksheet = workbook.add_worksheet()

        #Colores
        LIGHT_GRAY = '#CCCCCC'

        #Formatos
        bold = workbook.add_format({'bold': True, 'bg_color': LIGHT_GRAY,'align': 'center'})
        align_center = workbook.add_format({'align': 'center','valign':'vcenter','text_wrap':True})
        align_center_left = workbook.add_format({'valign':'vcenter','text_wrap':True})
        deep_red_format = workbook.add_format({'bg_color': '#860000'})
        red_format = workbook.add_format({'bg_color': '#FF0000'})
        yellow_format = workbook.add_format({'bg_color': 'yellow'})
        green_format = workbook.add_format({'bg_color': 'green'})
        formatCritical = {'type':'cell','criteria':'equal to','value':'"Critical"','format':deep_red_format}
        formatHigh = {'type':'cell','criteria':'equal to','value':'"High"','format':red_format}
        formatMedium = {'type':'cell','criteria':'equal to','value':'"Medium"','format':yellow_format}
        formatLow = {'type':'cell','criteria':'equal to','value':'"Low"','format':green_format}



        #Width
        worksheet.set_column('A:A',60,align_center)
        worksheet.set_column('B:B',9,align_center)
        worksheet.set_column('C:C',26,align_center_left)
        worksheet.set_column('D:D',39,align_center)
        worksheet.set_column('E:E',80,align_center)
        worksheet.set_column('F:F',80,align_center)

        #Titulos
        worksheet.write('A1', 'Vulnerabilidad', bold)
        worksheet.write('B1', 'Risk', bold)
        worksheet.write('C1', 'IPs', bold)
        worksheet.write('D1', 'Synopsis', bold)
        worksheet.write('E1', 'Description', bold)
        worksheet.write('F1', 'Solution', bold)

        #Empieza desde la segunda linea
        row = 1
        col = 0

        for vuln in vulnerabilidades:

            #Formato condicional al riesgo high,medium,low
            cell = 'B' + str(row+1)
            worksheet.conditional_format(cell,formatCritical)
            worksheet.conditional_format(cell,formatHigh)
            worksheet.conditional_format(cell,formatMedium)
            worksheet.conditional_format(cell,formatLow)

            #Escribo la fila con los datos de la vulnerabilidad
            worksheet.write(row,col,vuln.name)
            worksheet.write(row,col+1,vuln.level)
            worksheet.write(row,col+2,'\n'.join(vuln.ips))
            worksheet.write(row,col+3,vuln.synopsis)
            worksheet.write(row,col+4,vuln.descrip)
            worksheet.write(row,col+5,vuln.solution)
            worksheet.set_row(row,max(len(vuln.ips)*15+20,30))
            row +=1

        workbook.close()


    def toWord(vulnerabilidades,fileName):
        document = Document('templateInforme.docx')

        for vuln in vulnerabilidades:
            document.add_heading(vuln.name)
            document.add_heading("Identification",level=2)
            document.add_paragraph("Identification here")
            document.add_heading("Vulnerability detection",level=2)
            document.add_paragraph("Detection here")
            document.add_heading("Exploitation",level=2)
            document.add_paragraph("Exploitation here")
            document.add_heading("Detailed findings and recommendations",level=2)
            table = document.add_table(rows=6, cols=2)

            table.rows[0].cells[0].text = "Vulnerability"
            table.rows[0].cells[1].text = vuln.name
            table.rows[1].cells[0].text = "Risk Factor: "
            table.rows[1].cells[1].text = vuln.level
            table.rows[2].cells[0].text = "Synopsis: "
            table.rows[2].cells[1].text = vuln.synopsis
            table.rows[3].cells[0].text = "Description: "
            table.rows[3].cells[1].text = vuln.descrip
            table.rows[4].cells[0].text = "Ips: "
            table.rows[4].cells[1].text = '\n'.join(vuln.ips)
            table.rows[5].cells[0].text = "Solution: "
            table.rows[5].cells[1].text = vuln.solution
            document.add_page_break()
        document.save(fileName + '.docx')
