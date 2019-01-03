class ListaVulnerabilidades(list):

    def __init__(self):
        self.TotalIps = []

    def agregar(self, vuln, excluir, language):
        for ip in vuln.ips:
            if vuln.trimIp(ip) not in self.TotalIps:
                self.TotalIps.append(vuln.trimIp(ip))

        if vuln.level not in excluir:
            vuln.traducir(language)
            self.append(vuln)

    def mostrar(self):
        for vuln in self:
            vuln.mostrar()

    def count(self, level):
        count = 0
        for vuln in self:
            if vuln.level == level:
                count = count + 1
        return count

    def ips(self):
        return self.TotalIps
