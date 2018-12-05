import xlsxwriter

class Vulnerabilidad:

    def __init__(self):
        valor = "N/A"
        self.solution = valor
        self.level = valor
        self.descrip = valor
        self.synopsis = valor
        self.cvss = valor
        self.ips = []
        self.name = valor

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

    def agregar(self,tag,valor):
        if("Solution"==tag):
            self.solution = valor
        if("Risk Factor"==tag):
            self.level = valor
        if("Description"==tag):
            self.descrip = valor
        if("Synopsis"==tag):
            self.synopsis = valor
        if("CVSS Base Score"==tag):
            self.cvss = valor.split()[0]
        if("Ips"==tag):
            self.ips = valor
        if("Name"==tag):
            self.name = valor

    def toExcel(self,file):
        file.write(self.name + ',')
        file.write(self.level + ',')
        file.write("\"")
        for ip in self.ips:
            file.write("\n" + ip)
        file.write("\"")
        file.write(',')
        file.write(self.synopsis + ',')
        file.write(self.descrip)
        file.write('\n')

    #def entreComillas(self, ips):
