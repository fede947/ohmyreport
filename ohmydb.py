import dictpersist
import os

NAME = "Nombre"
SYNOP = "Sinopsis"
CAT = "Categoría"
DESCRIP = "Descripción"
RECOM = "Recomendación"
IMPACT = "Impacto"
EFFORT = "Esfuerzo"

def main():
    db = dictpersist.DictPersistJSON("db.json")
    mainMenu(db)


def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu(db):
    limpiarPantalla()
    print("Bienvenido a OhMyDB, para guardar sus traducciones y no la mierda de google")
    while (True):
        print("1 - Ver las vulnerabilidades que ya se encuentran traducidas")
        print("2 - Agregar una nueva traduccion")
        print("3 - Salir")
    
        entry = int(input("Elija una de las opciones: "))
        if (entry > 3 or entry < 1):
            noValidEntry(entry)
            continue
        if (entry == 3):
            print("Gracias, vuelva prontos")
            break
        if (entry == 1):
            printTranslations(db)
        if (entry == 2):
            addTranslation(db)

def addTranslation(db):
    id = input("Ingrese id de la vulnerabilidad: ")
    name = input("Ingrese nombre de la vulnerabilidad: ")
    synop = input("Ingrese sinopsis de la vulnerabilidad: ")
    cat = input("Ingrese categoría de la vulnerabilidad:")
    descrip = input("Ingrese descripción para la vulnerabilidad: ")
    recom = input("Ingrese recomendación para la vulnerabilidad:")
    impact = input("Ingrese impacto de negocio de la vulnerabilidad:")
    effort = input("Ingrese esfuerzo para reparar la vulnerabilidad:")
    actual = db.get(id, None)
    if (actual == None):
        db[id] = {NAME: name, SYNOP: synop, CAT: cat, DESCRIP: descrip, RECOM: recom, IMPACT: impact, EFFORT: effort}
        print("Vulnerabilidad agregada correctamente")
    else:
        print("La vulnerabilidad de id: {} ya existe".format(id))
        while(True):
            print("1 - Sobreescribir")
            print("2 - Ver contenido actual")
            print("3 - Cancelar")
            entry = int(input("Elija una de las opciones: "))
            if (entry > 3 or entry < 1):
                noValidEntry(entry)
                continue
            if (entry == 3):
                break
            if (entry == 1):
                db[id] = {NAME: name, SYNOP: synop, CAT: cat, DESCRIP: descrip, RECOM: recom, IMPACT: impact, EFFORT: effort}
                print("Vulnerabilidad agregada correctamente")
            if (entry == 2):
                printVuln(id, db)
                continue

def printTranslations(db):
    while (True):
        for id, vuln in db.items():
            print("{} {}".format(id, vuln[NAME]))
        print("1 - Elegir una vulnerabilidad")
        print("2 - Atras")
    
        entry = int(input("Elija una de las opciones: "))
        if (entry > 2 or entry < 1):
            noValidEntry(entry)
            continue
        if (entry == 2):
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        if (entry == 1):
            selectVuln(db)
            break

def selectVuln(db):
    while(True):
        entry = input("Ingrese id de vulnerabilidad a seleccionar:")
        vuln = db.get(entry, None)
        if (vuln == None):
            print("El id: {} no existe".format(entry))
            continue
        vulnMenu(entry, db)
        break

def vulnMenu(id, db):
    while(True):
        printVuln(id, db)
        print("1 - Modificar vulnerabilidad")
        print("2 - Atras")
        entry = int(input("Elija una de las opciones: "))
        if (entry > 2 or entry < 1):
            noValidEntry(entry)
            continue

        if (entry == 2):
            break
        if (entry == 1):
            modifyVuln(id, db)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

def printVuln(id, db):
    print("Id")
    print(id)
    for k,v in db[id].items():
        print(k)
        print(v)

def modifyVuln(id, db):
    newDict = {}
    name = input("Ingrese nuevo nombre de la vulnerabilidad ('-' para saltear): ")
    if (name != '-'):
        newDict[NAME] = name
    synop = input("Ingrese nueva sinopsis de la vulnerabilidad ('-' para saltear): ")
    if (synop != '-'):
        newDict[SYNOP] = synop
    cat = input("Ingrese nueva categoría de la vulnerabilidad ('-' para saltear): ")
    if (cat != '-'):
        newDict[CAT] = cat
    descrip = input("Ingrese nueva descripción para la vulnerabilidad ('-' para saltear): ")
    if (descrip != '-'):
        newDict[DESCRIP] = descrip
    recom = input("Ingrese nueva recomendación para la vulnerabilidad ('-' para saltear): ")
    if (recom != '-'):
        newDict[RECOM] = recom
    impact = input("Ingrese nuevo impacto de negocio de la vulnerabilidad ('-' para saltear): ")
    if (impact != '-'):
        newDict[IMPACT] = impact
    effort = input("Ingrese nuevo esfuerzo para reparar la vulnerabilidad ('-' para saltear): ")
    if (effort != '-'):
        newDict[EFFORT] = effort
    db[id].update(newDict)
    db._dump()

def noValidEntry(entry):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("La entrada {} no es valida".format(entry))
main()