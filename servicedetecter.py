# -*- coding: utf-8 -*-

import ipinfo
import docx

HEADER = 0
IP = 0
PUERTO = 1

TablaIPPuerto = 'Tabla IP/Puerto'

class ServiceDetecter:

    def __init__(self):
        self.ipsDict = {}

    def add(self, host, port, protocol, service):
        ip = self.ipsDict.get(host, ipinfo.IpInfo(host))
        ip.add(port, protocol, service)
        self.ipsDict[host] = ip

    def write(self, document):
        #Armando la tabla de detalles
        table = document.add_table(rows=1, cols=2)
        table.style = TablaIPPuerto
        table.autofit = False
        for cell in table.columns[0].cells:
            cell.width = docx.shared.Cm(3)
        for cell in table.columns[1].cells:
            cell.width = docx.shared.Cm(12)
        table.rows[HEADER].cells[IP].text = "IP"
        table.rows[HEADER].cells[PUERTO].text = "PUERTO Y SERVICIO"
        ipList = list(self.ipsDict.values())
        ipList.sort()
        for ip in ipList:
            ip.write(table, IP, PUERTO)
