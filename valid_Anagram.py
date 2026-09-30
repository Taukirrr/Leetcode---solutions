def validAnagram(s,t):
        hashmap ={}
        if len(s) != len(t):
            return False

        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for j in t:
            if j not in hashmap:
                return False
            hashmap[j] -= 1

            if hashmap[j] == -1:
                return False

        return True 

s = "anagram"
t = "aagnram"
print(validAnagram(s,t)) 
