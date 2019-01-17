# -*- coding: utf-8 -*-

import portinfo
import socket
import os

class IpInfo:

    def __init__(self, ip):
        self.ip = ip
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

    def getIpPorts(self):
        return [port.strIp(self.ip) for port in self.puertos.values()]
    
    def getIp(self):
        return self.ip

    def getPorts(self):
        ports = list(self.puertos.values())
        ports.sort()
        return ports
