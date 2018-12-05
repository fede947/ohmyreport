import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose',help="Increase verbosity", action='store_true')
    parser.add_argument('-o','--output',help="output to a file")
    parser.add_argument('file')
    return parser.parse_args()
