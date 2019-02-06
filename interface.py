SI = "s"
NO = "n"

def start(vulnerabilities):
    #changeNameMenu(vulnerabilities)
    #delete(vulnerabilities)
    #linkVulnerabilitiesMenu(vulnerabilities)
    exit = False
    while not exit:
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
        if command == "exit":
            exit = True
            continue
        print('[-] Invalid command ')



def showVulnerabilities(vulnerabilities):
    for index, vuln in enumerate(vulnerabilities):
        print("{} {}".format(index, vuln.name))

def linkVulnerabilitiesSelection(vulnerabilities, listVuln):

    aux = listVuln.split(",")
    vulnsNums = [int(i) for i in aux]
    vulnsNums.sort(reverse=True)
    name = vulnerabilities[vulnsNums[-1]].name
    for index, vulnNum in enumerate(vulnsNums):
        vulnsNums[index] = int(vulnNum)
        if (vulnsNums[index] >= len(vulnerabilities)):
            print("[-] Invalid index")
            return vulnerabilities

    vulnsNums.sort(reverse=True)
    mainVulnNum = vulnsNums[-1]
    for vulnNum in vulnsNums:
        if (vulnNum == mainVulnNum):
            continue
        vulnerabilities[mainVulnNum].link(vulnerabilities[vulnNum],name)
        del vulnerabilities[vulnNum]
    print("[+] Merged")
    return vulnerabilities

def changeName(vulnerabilities,params):

    index = int(params[0])
    name = params[1]
    if (index >= len(vulnerabilities)):
        print("[-] Invalid index")
        return vulnerabilities

    vulnerabilities[index].changeName(name)
    print("[+] Name changed")
    return vulnerabilities


def delete(vulnerabilities, params):
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
