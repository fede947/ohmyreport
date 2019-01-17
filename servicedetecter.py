# -*- coding: utf-8 -*-

import ipinfo

class ServiceDetecter:

    def __init__(self):
        self.ipsDict = {}

    def add(self, host, port, protocol, service):
        ip = self.ipsDict.get(host, ipinfo.IpInfo(host))
        ip.add(port, protocol, service)
        self.ipsDict[host] = ip
    
    def getIps(self):
        return list(self.ipsDict.values())
