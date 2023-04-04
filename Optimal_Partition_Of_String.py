from array import array
class Solution(object):
    # Runtime: 159ms beats 33.33%
    def partitionString(self, s):
        obj = {
            "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,
            "o": 14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25
        }
        arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        count = 0
        for i in s:
            if arr[obj[i]] == 1:
                count +=1
                arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            arr[obj[i]]=1

        return count+1
    # Runtime: 65ms beata 100%, Memory: 14.9MB beats 89.?%
    def partitionString_part2(self,s):
        count = 0
        string = ""
        for i in s:
            if i in string:
                count+=1
                string=""
            string+=i
        return count+1
    # Runtime: 115ms beats 60.42%, Memory: 15MB beats 54.17%
    def partitionString_part3(self,s):
        count = 0
        string = []
        for i in s:
            if i in string:
                count += 1
                string = []
            string.append(i)
        return count + 1