import xlsxwriter
from translate import translate

NA = "N/A"

class Vulnerabilidad:

    def __init__(self):
        self.cve = NA
        self.cvss = NA
        self.risk = NA
        self.ips = []
        self.name = NA
        self.synopsis = NA
        self.descrip = NA
        self.solution = NA

    def mostrar(self):
        print("name: " + self.name)
        print("level: " + self.level)
        print("cvss: " + self.cvss)
        print("description: \n" + self.descrip)
        print("synopsis: \n" + self.synopsis)
        print("ips: ")
        for ip in self.ips:
            print(ip)
        print("--------------------------------------------------------------")

    def set(self, row):
        if (self.name == NA):
            self.cve = row["CVE"]
            self.cvss = row["CVSS"]
            self.risk = row["Risk"]
            self.ips.append("{} ({}/{})".format(row["Host"], row["Protocol"], row["Port"]))
            self.name = row["Name"]
            self.synopsis = row["Synopsis"]
            self.descrip = row["Description"]
            self.solution = row["Solution"]
        else:
            self.ips.append("{} ({}/{})".format(row["Host"], row["Protocol"], row["Port"]))


    def traducir(self, lang):
        self.solution = translate(self.solution, lang)
        self.risk = translate(self.risk, lang)
        self.descrip = translate(self.descrip, lang)
        self.synopsis = translate(self.synopsis, lang)
        self.name = translate(self.name, lang)

    def trimIp(self, ip):
        return ip.split()[0]
