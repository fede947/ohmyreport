# -*- coding: utf-8 -*-

import os

class PortInfo:
    def __init__(self, port):
        self.port = port
        self.protocol = ""
        self.service = ""

    def add(self, protocol, service):
        self.protocol = protocol
        self.service = service

    def __lt__(self,other):
        return (int(self.port) < int(other.port))



    def __str__(self):
        return "{}/{} {}".format(self.port, self.protocol, self.service)

    def strIp(self, ip):
        return "{} ({}/{})".format(ip, self.port, self.protocol)
