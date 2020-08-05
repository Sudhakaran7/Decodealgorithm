class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
val=Solution()
str1,K=map(str,input().split())
A=int(K)
print(val.decodeAtIndex(str1,A))
