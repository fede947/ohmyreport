class ListaVulnerabilidades(list):
    def agregar(self,vuln,excluir):
        if vuln.level not in excluir:
            self.append(vuln)

    def mostrar(self):
        for vuln in self:
            vuln.mostrar()
