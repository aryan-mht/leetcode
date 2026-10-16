class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0
        ps = [0] * n

        ps[0] = arr[0]
        for i in range(1, n):
            ps[i] = ps[i-1] + arr[i]
        
        f_count = {}
        for j in range(n):
            if ps[j] == k:
                count+=1
            val = ps[j] - k
            if val in f_count:
                count += f_count[val]
            
            if ps[j] not in f_count:
                f_count[ps[j]] = 0
            
            f_count[ps[j]] +=1
        
        return count
        




        