import ohmydbmenu
import dbparam
import csv
import dictpersist

DB = "db.json"

def main():
    args = dbparam.arguments()
    db = dictpersist.DictPersistJSON(DB)
    if (args.input):
        with open(args.input, 'r') as inputCsv:
            inputReader = csv.DictReader(inputCsv, delimiter = ';')
            for row in inputReader:
                print(row)
                ohmydbmenu.addTranslation(db, row)
    else:
        ohmydbmenu.mainMenu()

main()