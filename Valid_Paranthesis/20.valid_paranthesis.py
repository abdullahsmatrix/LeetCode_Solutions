class Solution:
    def isValid(self, s: str) -> bool:
        dic = []
        par = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for a in s:
            if a == "(" or a == "{" or a == "[":
                dic.append(a)
            elif (a == ")" or a == "]" or a == "}"):
                if len(dic) == 0:
                    return False
                b = len(dic) - 1
                
                if par[a] == dic[b]:
                    dic.pop()
                else:
                    return False
        
        if len(dic) == 0:
            return True
        else:
            return False


#convert base Question frombase = 25 n = "4r" tobase = 2
#[[1,3,4], [32, 43 ,34]] == [[1,3,4], [32,34,43]]
# arr1, arr2 = (arr1 + arr2).sort()
