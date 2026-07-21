class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        ret = ""
        for n in strs:
            word = ""
            for i in n:
                word += str(ord(i) + 1)
                word += ","

            ret += word
        
            ret += "-"
        print(ret)
        return ret
        
        ret = ""
        for i in strs:
            for l in i:
                ret += l
            ret += "-"
        ret = ret[:-1]
        print ("encode" , ret)
        return ret
        '''

        if strs is None:
            return ""
        
        ret = ""
        for s in strs:
            ret += str(len(s))
            ret +=","
        ret += "#"
        
        for s in strs:
            ret += s
        print (ret)
        return ret

    def decode(self, s: str) -> List[str]:
        '''
        ret = []
        s = s.strip("-")
        print("stripped", s)
        arr = s.split("-")
        for n in arr:
            word = ""
            n = n.split(",")
            print("n:", n)
            for i in n:
                if not i == "":
                    print(i)
                    word += chr(int(i) - 1) 
                    print(word)
            
            ret.append(word)
        return ret
        

        s = s.split("-")
        print ("decode" , s)
        if s == [""]:
            print("hello?")
            return []
        return s

        '''

        if s is None:
            return []
        sizes = []
        i = 0
        
        while s[i] != "#":
            num = ""
            while s[i] != ",":
                num += s[i]
                i += 1
            sizes.append(int(num))
            i += 1
        i += 1

        res = []
        
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res





