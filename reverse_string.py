def reverseString(s):
       s_list = list(s)
       left = 0
       right = len(s) - 1
       while left < right:
        temp = s_list[left]
        s_list[left] = s_list[right]
        s_list[right] = temp

        left += 1
        right -= 1
        return "".join(s_list)
s = "Taukir"
print(reverseString(s))