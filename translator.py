from translate import translate
import sys
from ohmydbmenu import *

class Translator():

    def __init__(self, language):
        self.language = language

    def translate(self, vuln):
        # funcion que rompe encapsulamiento
        translation = get(vuln.id)
        # not in db
        if (translation == None):
            # translate with google
            vuln.solution = translate(vuln.solution, self.language)
            vuln.descrip = translate(vuln.descrip, self.language)
            vuln.synopsis = translate(vuln.synopsis, self.language)
            vuln.name = translate(vuln.name, self.language)
        else:
            vuln.name = translation[NAME]
            vuln.synopsis = translation[SYNOP]
            vuln.category = translation[CAT]
            vuln.descrip = translation[DESCRIP]
            vuln.solution = translation[RECOM]
            vuln.impact = translation[IMPACT]
            vuln.effort = translation[EFFORT]
            vuln.explotation = translation[EXPLOTATION]