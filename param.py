import argparse

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose',help="Increase verbosity", action='store_true')
    parser.add_argument('-e','--excel',help="output to a excel file")
    parser.add_argument('-w','--word',help="output to a word file")
    parser.add_argument('-l','--language',help="language of the file",choices=['en','es'],required=True)
    parser.add_argument('file')
    return parser.parse_args()
