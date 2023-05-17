from sys import argv
scriptName,fileName,encodingScheme,error=argv
def mainCaller(file,Scheme,err):
    currLine = file.readline()
    if currLine:
        encoder_decoder(currLine,Scheme,err)
        return mainCaller(file,Scheme,err)

def encoder_decoder(line:str,Scheme,err):
    line=line.strip()
    rawLine = line.encode(Scheme,errors=err)# converts to bytes (hexadecimal)
    meal = rawLine.decode(Scheme,errors=err)# converts to unicode from bytes
    print(f"{rawLine} ==> {meal}")

fileData=open(fileName,encoding=encodingScheme)
mainCaller(fileData,encodingScheme,error)
