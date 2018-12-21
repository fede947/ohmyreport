import argparse

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose', help="Increase verbosity", action='store_true')
    parser.add_argument('--version', action='version', version='ohmyreport BETA version')
    parser.add_argument('-e','--excel', help="create a excel file (default: true)", action='store_true')
    parser.add_argument('-w','--word', help="create a word file (default: word)", action='store_true')
    parser.add_argument('-o','--output', help="output file (default: NessusFile's name)", metavar='FILE')
    parser.add_argument('-l','--language', help="language of the file (default: english)", choices=['en','es'], default='en')
    parser.add_argument('-c','--client', help="client name", default='[empresa]')
    parser.add_argument('-n','--nmap', help="nmap port scan xml output")

    parser.add_argument('file', metavar='NessusFile')
    args = parser.parse_args()

    if not args.output:
        args.output = args.file

    if not args.excel and not args.word:
        args.excel = True
        args.word = True

    return args
