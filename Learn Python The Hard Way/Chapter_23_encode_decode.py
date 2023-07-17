rawStringSample:bytes = b'\xe6\x96\x87\xe8\xa8\x80'
print(f"{rawStringSample} decode gives us {rawStringSample.decode()}")  #文言
utf_stringSample:str = "文言"
print(f"{utf_stringSample} encode gives us {utf_stringSample.encode()}")  # b'\xe6\x96\x87\xe8\xa8\x80'
print(f"rawStringSample == utf_stringSample.encode() => {rawStringSample == utf_stringSample.encode()}") # True
print(f"utf_stringSample == rawStringSample.decode() => {utf_stringSample == rawStringSample.decode()}") # True
