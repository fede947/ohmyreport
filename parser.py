from Vulnerabilidad import *
import re

def getAllVuln(soup):
    names = []
    ul = soup.body.div.findAll('ul')
    for name in ul[1].findAll('li'):
        names.append(name.get_text().split('-')[1].strip())
    return names

def getVulnInfo(soup,index):

    name = soup.body.div.findAll('ul')[1].findAll('li')[index]
    Taginfo = soup.body.div.findAll('div')[5].findAll('div','section-wrapper')[index]


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

def mostrarTitulo(soup):
    print("")
    print("")
    print(soup.title.get_text())
    print("")
