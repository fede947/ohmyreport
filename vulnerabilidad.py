import xlsxwriter
from translate import translate
import os
import ipinfo

NA = "N/A"
CRITICAL = "Critical"
HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"

class Vulnerabilidad:

    def __init__(self):
        self.cve = NA
        self.cvss = NA
        self.risk = NA
        self.ips = {}
        self.name = NA
        self.synopsis = NA
        self.descrip = NA
        self.solution = NA

    def mostrar(self):
        print("name: " + self.name)
        print("level: " + self.risk)
        print("cvss: " + self.cvss)
        print("description: \n" + self.descrip)
        print("synopsis: \n" + self.synopsis)
        print("ips: ")
        for ip in self.ips:
            print(ip)
        print("--------------------------------------------------------------")

    def link(self, other, name):
        self.descrip = "{}:{} {}{}{}{}:{} {}".format(self.name, os.linesep, self.descrip, os.linesep, os.linesep, other.name, os.linesep, other.descrip)
        self.synopsis = "{}:{} {}{}{}{}:{} {}".format(self.name, os.linesep, self.synopsis, os.linesep, os.linesep, other.name, os.linesep, other.synopsis)
        self.solution = "{}:{} {}{}{}{}:{} {}".format(self.name, os.linesep, self.solution, os.linesep, os.linesep, other.name, os.linesep, other.solution)
        if not (self.cve):
            self.cve = other.cve
        elif (other.cve and self.cve):
            self.cve = "{}, {}".format(self.cve, other.cve)
        self.ips = self.ips.union(other.ips)
        self.cvss = max(self.cvss, other.cvss)
        if (self.risk == HIGH):
            if (other.risk == CRITICAL):
                self.risk = CRITICAL
        elif (self.risk == MEDIUM):
            if (other.risk != LOW):
                self.risk = other.risk
        elif (self.risk == LOW):
            self.risk = other.risk
        self.name = name

    def changeName(self, name):
        self.name = name

    def set(self, row):
        if (self.name == NA):
            self.cve = row["CVE"]
            self.cvss = row["CVSS"]
            self.risk = row["Risk"]
            ip = ipinfo.IpInfo(row["Host"])
            ip.add(row["Port"], row["Protocol"], "")
            self.ips[row["Host"]] = ip
            self.name = row["Name"]
            self.synopsis = row["Synopsis"]
            self.descrip = row["Description"]
            self.solution = row["Solution"]
        else:
            ip = self.ips.get(row["Host"], ipinfo.IpInfo(row["Host"]))
            ip.add(row["Port"], row["Protocol"], "")
            self.ips[row["Host"]] = ip

    def traducir(self, lang):
        self.solution = translate(self.solution, lang)
        #self.risk = translate(self.risk, lang)
        #risk translated when writing
        self.descrip = translate(self.descrip, lang)
        self.synopsis = translate(self.synopsis, lang)
        self.name = translate(self.name, lang)

    def __lt__(self, other):
        if (self.risk == other.risk):
            return self.cvss < other.cvss
        else:
            if (self.risk == CRITICAL):
                return False
            elif (self.risk == HIGH):
                if (other.risk == CRITICAL):
                    return True
                return False
            elif (self.risk == MEDIUM):
                if (other.risk == CRITICAL or other.risk == HIGH):
                    return True
                return False
            return True

    def __eq__(self, other):
        return (self.risk == other.risk and self.cvss == other.cvss)
            
