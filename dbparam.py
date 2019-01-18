import argparse

def arguments():
    parser = argparse.ArgumentParser()
   
    parser.add_argument('-i','--input', help="Archivo csv basado en el csvtemplate.csv con las traducciones a agregar", metavar='CSVFILE')

    return parser.parse_args()