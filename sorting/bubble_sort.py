def bubble(nums):
    size = len(nums)
    for _ in nums:
        is_sorted = True # melhoria que garante que se estiver ordenado retorna o array e não vai ser necessário percorre-lo n vezes
        print(nums)
        for i in range(size-1):
            if nums[i] > nums[i+1]: #faz a comparação com o número do lado
                is_sorted = False
                nums[i+1], nums[i] = nums[i], nums[i+1]
        if is_sorted:
            return


bubble([1, 2, 5, 4, 3])