import sys
script, encodingMain, error = sys.argv

def printLine(line:str, encoding, errors):
    line = line.strip()
    encodedText = line.encode(encoding,errors=errors)
    decodedText = encodedText.decode(encoding,errors=errors)
    print(f"{encodedText} <====> {decodedText}")

def process(language_file,encoding,errors):
    line = language_file.readline()
    if line:
        printLine(line,encoding,errors)
        return process(language_file,encoding,errors)

languageFile = open("Languages.txt",encoding="utf-8")
process(languageFile,encodingMain,error)





