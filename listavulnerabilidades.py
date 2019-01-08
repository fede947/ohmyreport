class ListaVulnerabilidades(list):

    def __init__(self):
        self.TotalIps = []

    def agregar(self, vuln, excluir):
        for ip in vuln.ips:
            if vuln.trimIp(ip) not in self.TotalIps:
                self.TotalIps.append(vuln.trimIp(ip))

        if vuln.risk not in excluir:
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
        return self.TotalIps
