SI = "s"
NO = "n"

def start(vulnerabilities):
    #changeNameMenu(vulnerabilities)
    #delete(vulnerabilities)
    #linkVulnerabilitiesMenu(vulnerabilities)
    exit = False
    while not exit:
        try:
            print()
            entry = input('ohmyreport>>>').split(" ")
            command = entry.pop(0)

            if command == "show":
                showVulnerabilities(vulnerabilities)
                continue
            if command == "delete":
                vulnerabilities = delete(vulnerabilities, entry[0])
                continue
            if command == "chname":
                vulnerabilities = changeName(vulnerabilities, entry)
                continue
            if command == "merge":
                vulnerabilities = linkVulnerabilitiesSelection(vulnerabilities, entry[0])
                continue
            if command == "help":
                printHelp()
                continue
            if command == "sasha":
                easterEgg()
                continue
            if command == "exit":
                exit = True
                continue
            print('[-] Invalid command ')
        except KeyboardInterrupt:
            print()
            print('[-] nah nah nah')
        except:
            print('[-] Super invalid command (╯°□°）╯︵ ┻━┻')


def showVulnerabilities(vulnerabilities):
    for index, vuln in enumerate(vulnerabilities):
        print("{} {}".format(index, vuln.name))

def linkVulnerabilitiesSelection(vulnerabilities, listVuln):

    aux = []
    if '-' in listVuln:
        listVuln = listVuln.split('-')
        for i in range(int(listVuln[0]),int(listVuln[1]) + 1): #FIXIT arreglar el algoritmo
            aux.append(i)
    else:
        aux = listVuln.split(",")
    vulnsNums = [int(i) for i in aux]
    vulnsNums.sort(reverse=True)
    print(vulnsNums)
    name = vulnerabilities[vulnsNums[-1]].name
    for index, vulnNum in enumerate(vulnsNums):
        vulnsNums[index] = int(vulnNum)
        if (vulnsNums[index] >= len(vulnerabilities)):
            print("[-] Invalid index")
            return vulnerabilities

    mainVulnNum = vulnsNums[-1]
    for vulnNum in vulnsNums:
        if (vulnNum == mainVulnNum):
            continue
        vulnerabilities[mainVulnNum].link(vulnerabilities[vulnNum],name)
        del vulnerabilities[vulnNum]
    print("[+] Merged")
    return vulnerabilities

def changeName(vulnerabilities,params):

    index = int(params.pop(0))
    name = ' '.join(params)
    if (index >= len(vulnerabilities)):
        print("[-] Invalid index")
        return vulnerabilities

    vulnerabilities[index].changeName(name)
    print("[+] Name changed")
    return vulnerabilities


def delete(vulnerabilities, params):
    aux = []
    if '-' in params:
        for i in range(int(params[0]),int(params[2]) + 1):
            aux.append(i)
    else:
        aux = params.split(",")
    vulnsNums = [int(i) for i in aux]
    vulnsNums.sort(reverse=True)
    for index in vulnsNums:
        del vulnerabilities[int(index)]
    print('[+] deleted')
    return vulnerabilities

def printHelp():
    text = []
    text.append("show       show vulnerabilites")
    text.append("delete     Delete list of vulnerabilites. eg: delete 1,2,3,4")
    text.append("merge      Merge list of vulnerabilites. eg: merge 1,2,3,4")
    text.append("chname     Change a name of one vulnerability. eg: chname 4 NEW_NAME")
    text.append("exit       exit and continue with the report.")
    text.append("help       This help :).")

    print('\n'.join(text))

def easterEgg():
    print(" easter egg pendiente.....(╯°□°）╯︵ ┻━┻")
