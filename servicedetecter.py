# -*- coding: utf-8 -*-

import ipinfo
import docx

HEADER = 0
HOSTNAME = 0
IP = 1
PUERTO = 2

class ServiceDetecter:
    
    def __init__(self):
        self.ipsDict = {}

    def add(self, host, port, protocol, service):
        ip = self.ipsDict.get(host, ipinfo.IpInfo(host))
        ip.add(port, protocol, service)
        self.ipsDict[host] = ip 
        
    def write(self, document):
        #Armando la tabla de detalles
        table = document.add_table(rows=1, cols=3)
        table.rows[HEADER].cells[HOSTNAME].text = "URL"
        table.rows[HEADER].cells[IP].text = "IP"
        table.rows[HEADER].cells[PUERTO].text = "PUERTO Y SERVICIO"
        for ip in self.ipsDict.values():
            ip.write(table, HOSTNAME, IP, PUERTO)
        
        

