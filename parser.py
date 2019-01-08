from vulnerabilidad import Vulnerabilidad
import re
import progressbar
import csv

class CsvParser():

    def __init__(self, fileName):
        self.fileName = fileName

    def getAllVuln(self):
        vulnDict = {}
        with open(self.fileName, 'r') as nesusCsv:
            nesusReader = csv.DictReader(nesusCsv)
            for row in nesusReader:
                vuln = vulnDict.get(row["Name"], Vulnerabilidad())
                vuln.set(row)
                vulnDict[row["Name"]] = vuln

        return vulnDict.values()

    def getVulnCount(self):
        names = []
        ul = self.soup.body.div.findAll('ul')
        for name in ul[1].findAll('li'):
            names.append(name.get_text().split('-')[1].strip())
        return len(names)



    def getVulnInfo(self, index):

        name = self.soup.body.div.findAll('ul')[1].findAll('li')[index]
        Taginfo = self.soup.body.div.findAll('div')[5].findAll('div','section-wrapper')[index]


        vulnerabilidad = Vulnerabilidad()
        divs = Taginfo.findAll('div')
        for tag in range(100):
            if(divs[tag+2].get_text().strip() == "Plugin Output"):
                break
            vulnerabilidad.agregar(divs[tag].get_text().strip(),divs[tag+2].get_text().strip())


        name = '-'.join(name.get_text().split('-')[1:]).strip()
        ips = list(map(lambda ip : ip.get_text(),Taginfo.findAll('h2')))

        vulnerabilidad.agregar("Ips", ips)
        vulnerabilidad.agregar("Name", name)
        return vulnerabilidad

    def mostrarTitulo(self):
        print("")
        print("")
        print(self.soup.title.get_text())
        print("")
