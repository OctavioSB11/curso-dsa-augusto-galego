# Sliding window: um problema onde temos que verificar o maximo de vezes que 
# uma substring aparece na window, vamos aumentando e diminuindo a window até encontrarmos

class Solution:
    def maximumLenghtSubstring(self, s: str) -> int:
        l, r = 0, 0 # ponteiros esquerda e direita
        _max = 1
        counter = {}
        counter[s[0]] = 1
        while r < len(s) - 1:
            r += 1
            if counter.get[s[r]]:
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3: #3 é o max
                counter[s[r]] -= 1
                l += 1
            _max = _max(_max, r-l+1)

        return _max