class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = set(s)
        t1 = set(t)
        dict1 = {}
        dict2 = {}
        for i in s1:
            dict1[i] = s.count(i)
        for i in t1:
            dict2[i] = t.count(i)
        dict1key = dict1.keys()
        dict2key = dict2.keys()
        if sum(dict1.values()) == sum(dict2.values()):
            for key1 in dict1key:
                if key1 in dict2key:
                    if dict1[key1] != dict2[key1]:
                        return False
                else:
                    return False
            return True
        return False




        
        


        
        


        