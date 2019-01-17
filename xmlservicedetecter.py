# -*- coding: utf-8 -*-

from servicedetecter import ServiceDetecter
import xml.etree.ElementTree as ET

class XmlServiceDetecter(ServiceDetecter):
    
    def __init__(self, path):
        super().__init__()
        self.root = ET.parse(path).getroot()
        self.parse()
    
    def parse(self):
        for host in self.root.iter('host'):
            address = host.find("address") 
            for port in host.iter('port'):
                state = port.find('state')
                if (state != None):
                    if (state.attrib.get("state","") == "open"):
                        service = port.find('service')
                        if (service):
                            service_nombre = service.attrib.get("name","")
                            service_product = service.attrib.get("product","")
                            service_version = service.attrib.get("version","")
                            service_extrainfo = service.attrib.get("extrainfo","")
                            if (service_extrainfo != ""):
                                service_extrainfo = "(" + service_extrainfo + ")"
                        else:
                            service_nombre = ""
                            service_product = ""
                            service_version = ""
                            service_extrainfo = ""
                        self.add(address.attrib["addr"], port.attrib["portid"], 
                                    port.attrib["protocol"], 
                                    "{} {} {} {}".format(service_nombre, 
                                    service_product, service_version, service_extrainfo))