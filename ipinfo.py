# -*- coding: utf-8 -*-

import portinfo
import socket
import os

class IpInfo:

    def __init__(self, ip):
        self.ip = ip
        self.os = ""
        self.puertos = {}

    def add(self, port, protocol, service=""):
        portInfo = self.puertos.get(port, portinfo.PortInfo(port))
        portInfo.add(protocol, service)
        self.puertos[port] = portInfo

    def __eq__(self, other):
        return self.ip == other.ip

    def __lt__(self, other):
        if (self == other):
            return False
        parsedSelf = self.ip.split(".")
        parsedOther = other.ip.split(".")
        for i in range(0,4):
            if (int(parsedSelf[i]) < int(parsedOther[i])):
                return True
            elif (int(parsedSelf[i]) > int(parsedOther[i])):
                return False
        return False

    def link(self, other):
        if not(other):
            return
        # Hay que hacer un link de puertos
        self.puertos.update(other.puertos)
    
    def write(self, table, ip_idx, port_idx):
        row_cells = table.add_row().cells
        row_cells[ip_idx].text = self.ip
        ports = list(self.puertos.values())
        ports.sort()
        # To evit the first line empty
        row_cells[port_idx].text = str(ports[0])
        ports.pop(0)
        for port in ports:
            row_cells[port_idx].add_paragraph(str(port))
        #row_cells[port_idx].text = "".join(map(str,sorted(ports)))

    def __str__(self):
        return (os.linesep).join([port.strIp(self.ip) for port in self.puertos.values()])
