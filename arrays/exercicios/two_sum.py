##Minha implementação

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Preparamos os dados (valor, índice_original)
        nova_lista = [(v, i) for i, v in enumerate(nums)]
        
        # Ordenamos para o Two Pointers funcionar
        nova_lista.sort()

        l = 0
        r = len(nums) - 1

        while l < r:
            soma_atual = nova_lista[l][0] + nova_lista[r][0]
            
            if soma_atual == target:
                # Retornamos os índices originais que guardamos
                return [nova_lista[l][1], nova_lista[r][1]]
            elif soma_atual < target:
                l += 1
            else: 
                r -= 1

solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))

# Iplementação do vídeo 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, i in enumerate(nums):
            if hash.get(i) is not None:
                return[hash.get(i), idx]
            hash[target-i] = idx