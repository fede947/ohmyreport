SI = "s"
NO = "n"

def start(vulnerabilities):
    changeNameMenu(vulnerabilities)
    delete(vulnerabilities)
    linkVulnerabilitiesMenu(vulnerabilities)

def showVulnerabilities(vulnerabilities):
    for index, vuln in enumerate(vulnerabilities):
        print("{} {}".format(index, vuln.name))

def linkVulnerabilitiesSelection(vulnerabilities):
    while(True):
        entry = input("Ingrese numero de vulnerabilidades a unir separadas por comas:")
        aux = entry.split(",")
        vulnsNums = [int(i) for i in aux]
        vulnsNums.sort(reverse=True)
        error = False
        for index, vulnNum in enumerate(vulnsNums):
            vulnsNums[index] = int(vulnNum)
            if (vulnsNums[index] >= len(vulnerabilities)):
                print("La entrada {} no es valida".format(entry))
                error = True
                break

        if (error):
            continue

        name = input("Ingrese nuevo nombre para la vulnerabilidad:")
        vulnsNums.sort(reverse=True)
        mainVulnNum = vulnsNums[-1]
        for vulnNum in vulnsNums:
            if (vulnNum == mainVulnNum):
                continue
            vulnerabilities[mainVulnNum].link(vulnerabilities[vulnNum], name)
            del vulnerabilities[vulnNum]
        print("----------------------------------")
        break

def linkVulnerabilitiesMenu(vulnerabilities):
    while(True):
        showVulnerabilities(vulnerabilities)
        entrada = input("Desea unir alguna vulnerabilidad? [S/N]: ")
        if (entrada.lower() == SI):
            linkVulnerabilitiesSelection(vulnerabilities)
        elif (entrada.lower() == NO):
            break
        else:
            print("El caracter ingresado no es valido")
            print("----------------------------------")

def changeName(vulnerabilities):
    while(True):
        entry = int(input("Ingrese numero de vulnerabilidad a cambiar el nombre:"))
        if (entry >= len(vulnerabilities)):
            print("La entrada {} no es valida".format(entry))
            continue

        print("{} {}".format(entry, vulnerabilities[entry].name))
        name = input("Ingrese nuevo nombre para la vulnerabilidad:")
        vulnerabilities[entry].changeName(name)
        print("----------------------------------")
        break

def changeNameMenu(vulnerabilities):
    while(True):
        showVulnerabilities(vulnerabilities)
        entrada = input("Desea cambiar el nombre de alguna vulnerabilidad? [S/N]: ")
        if (entrada.lower() == SI):
            changeName(vulnerabilities)
        elif (entrada.lower() == NO):
            break
        else:
            print("El caracter ingresado no es valido")
            print("----------------------------------")



def delete(vulnerabilities):
    showVulnerabilities(vulnerabilities)
    entrada = input("Desea eliminar alguna alguna vulnerabilidad? [S/N]: ")
    if (entrada.lower() == SI):
        entry = input("Ingrese numero de vulnerabilidades a eliminar separadas por comas:")
        aux = entry.split(",")
        vulnsNums = [int(i) for i in aux]
        vulnsNums.sort(reverse=True)
        for index in vulnsNums:
            del vulnerabilities[int(index)]
