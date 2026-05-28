class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cmax = -1

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = cmax
            cmax = max(cmax, curr)

        return arr

