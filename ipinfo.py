# -*- coding: utf-8 -*-

import portinfo
import socket
import os

HOSTNAME = 0

class IpInfo:
    
    def __init__(self, ip):
        self.ip = ip
        self.os = ""
        self.puertos = {}
        try:
            self.hostname = socket.gethostbyaddr(ip)[HOSTNAME]
        except:
            self.hostname = "Not detectable"
        
    def add(self, port, protocol, service):
        portInfo = self.puertos.get(port, portinfo.PortInfo(port))
        portInfo.add(protocol, service)
        self.puertos[port] = portInfo
    
    def write(self, table, hostname_idx, ip_idx, port_idx):
        row_cells = table.add_row().cells
        row_cells[ip_idx].text = self.ip
        row_cells[hostname_idx].text = self.hostname
        ports = self.puertos.values()
        row_cells[port_idx].text = (os.linesep).join(map(str,ports))
            
            
            
