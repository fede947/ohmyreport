# -*- coding: utf-8 -*-

import portinfo
import socket
import os

class IpInfo:
    
    def __init__(self, ip):
        self.ip = ip
        self.os = ""
        self.puertos = {}
        
    def add(self, port, protocol, service):
        portInfo = self.puertos.get(port, portinfo.PortInfo(port))
        portInfo.add(protocol, service)
        self.puertos[port] = portInfo
    
    def write(self, table, ip_idx, port_idx):
        row_cells = table.add_row().cells
        row_cells[ip_idx].text = self.ip
        ports = self.puertos.values()
        row_cells[port_idx].text = (os.linesep).join(map(str,ports))
            
            
            
