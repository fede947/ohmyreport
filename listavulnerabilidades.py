import translator

class ListaVulnerabilidades(list):

    def __init__(self, language):
        self.TotalIps = []
        self.translator = translator.Translator(language)

    def agregar(self, vuln, excluir):
        for ip in vuln.ips.values():
            if not ip in self.TotalIps:
                self.TotalIps.append(ip)

        if vuln.risk not in excluir:
            self.translator.translate(vuln)
            self.append(vuln)

    def mostrar(self):
        for vuln in self:
            vuln.mostrar()

    def count(self, risk):
        count = 0
        for vuln in self:
            if vuln.risk == risk:
                count = count + 1
        return count

    def ips(self):
        #self.TotalIps.sort()
        return [ipInfo.ip for ipInfo in self.TotalIps]

    def getIps(self):
        return self.TotalIps
