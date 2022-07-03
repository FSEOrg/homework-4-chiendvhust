class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        dict = {}
        res = [0] * len(arr)
        for i, v in enumerate(arr):
            if v not in dict:
                dict[v] = list()
            dict[v].append(i)
        print(dict)
        for values in dict.values():
            sumvalue = sum(values)
            prefixSum = 0
            print(values)
            for idx, i in enumerate(values, 1):

                sumvalue -= i

                prefixSum += i
                res[i] = i * idx - prefixSum + \
                    sumvalue - i * (len(values) - idx)

        return res
