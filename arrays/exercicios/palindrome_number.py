# Usei a técnica dos ponteiros paralelos, onde vamos verificando se os dois ponteiros são iguais após isso iteramos
# se forem diferente, retorna false, se encontrarem retorna True.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False

            left += 1
            right -= 1

        return True