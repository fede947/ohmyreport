from vulnerabilidad import Vulnerabilidad
import re
import progressbar
import csv

class CsvParser():

    def __init__(self, fileName):
        self.fileName = fileName

    def getAllVuln(self):
        vulnDict = {}
        with open(self.fileName, 'r') as nesusCsv:
            nesusReader = csv.DictReader(nesusCsv)
            for row in nesusReader:
                vuln = vulnDict.get(row["Name"], Vulnerabilidad())
                vuln.set(row)
                vulnDict[row["Name"]] = vuln

        return vulnDict.values()
