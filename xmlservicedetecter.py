# -*- coding: utf-8 -*-

import servicedetecter
import xml.etree.ElementTree as ET
class XmlServiceDetecter:
    
    def __init__(self, serviceDetecter, path):
        self.serviceDetecter = serviceDetecter
        self.root = ET.parse(path).getroot()
        self.parse()
    
    def parse(self):
        for host in self.root.iter('host'):
            address = host.find("address")  
            for port in host.iter('port'):
                service = port.find('service')
                service_nombre = service.attrib.get("name","")
                service_product = service.attrib.get("product","")
                service_version = service.attrib.get("version","")
                service_extrainfo = service.attrib.get("extrainfo","")
                if (service_extrainfo != ""):
                    service_extrainfo = "(" + service_extrainfo + ")"
                self.serviceDetecter.add(address.attrib["addr"], port.attrib["portid"], 
                                    port.attrib["protocol"], 
                                    "{} {} {} {}".format(service_nombre, 
                                    service_product, service_version, service_extrainfo))
