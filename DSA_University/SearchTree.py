class Trie:
    def __init__(self):
        self._topDict = dict()

    def buildTree(self, stringList:[str]):
        for string in stringList:
            d = self._topDict
            for characters in string:
                if characters not in d:
                    d[characters] = dict()
                d = d[characters]

    def searchTrie(self, word:str)->bool:
        trie = self._topDict
        for letter in word:
            if letter not in trie:
                print("Not Found!!")
                return False
            trie = trie[letter]
        print("Letter Found")
        return True

    def printTrie(self):
        print(self._topDict)
strList = ["all","aloud","above","at","about"]
makeInstance = Trie()
makeInstance.buildTree(strList)
for words in strList:
    print(makeInstance.searchTrie(words))
print(makeInstance.searchTrie("alout"))
makeInstance.printTrie()
makeInstance.searchTrie("albeit")
makeInstance.searchTrie("aboo")
makeInstance.searchTrie("att")
makeInstance.searchTrie("abo")

class BinarySearch_ForStrings:
    def __init__(self, strList):
        self.mainArray = strList
        self.quickSort(self.mainArray,0,len(strList)-1)
    def quickSort(self, strList:[str], left:int, right:int):
        if left >= right:
            return
        partition = self.partMe(strList,left,right)
        self.quickSort(strList,left,partition-1)
        self.quickSort(strList,partition+1,right)
    def partMe(self,arrList:[str],left:int,right:int):
        pivot = arrList[left]
        nLeft = left+1
        nRight = right
        while True:
            while nLeft<=nRight and arrList[nLeft]<=pivot:
                nLeft+=1
            while nLeft<=nRight and arrList[nRight]>=pivot:
                nRight-=1
            if nLeft<=nRight:
                arrList[nLeft],arrList[nRight]=arrList[nRight],arrList[nLeft]
            else:
                break
        arrList[left],arrList[nRight]=arrList[nRight],arrList[left]
        return nRight

    def binSearch(self,word:str):
        return self.Search(word,self.mainArray)
    def Search(self,word:str,arr:[str]):
        length = len(arr)
        if length == 0:
            return -27
        middle = length//2
        if arr[middle] == word:
            return middle
        elif word < arr[middle]:
            return self.Search(word,arr[:middle])
        else:
            return self.Search(word,arr[middle+1:])
    def printList(self):
        print(self.mainArray)

print("========================================")
makeInstance_2 = BinarySearch_ForStrings(strList)
makeInstance_2.printList()
print(makeInstance_2.binSearch("at"))
print(makeInstance_2.binSearch("albeit"))
print(makeInstance_2.binSearch("aloud"))
print(makeInstance_2.binSearch("abo"))