from Vulnerabilidad import *
import re
from progressBar import *
from bs4 import BeautifulSoup

class htmlParser():

    def __init__(self,html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def getAllVuln(self):
        listaAux = []
        cantidad = self.getVulnCount()
        progress = ProgressBar(cantidad)
        progress.mostrar()
        for index in range(cantidad):
            progress.siguiente()
            listaAux.append(self.getVulnInfo(index))
        return listaAux

    def getVulnCount(self):
        names = []
        ul = self.soup.body.div.findAll('ul')
        for name in ul[1].findAll('li'):
            names.append(name.get_text().split('-')[1].strip())
        return len(names)



    def getVulnInfo(self,index):

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

        vulnerabilidad.agregar("Ips",ips)
        vulnerabilidad.agregar("Name",name)
        return vulnerabilidad

    def mostrarTitulo(self):
        print("")
        print("")
        print(self.soup.title.get_text())
        print("")
