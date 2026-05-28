class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1; cmax = -1

        while i >= 0:
            cval = arr[i]
            arr[i] = cmax
            i -= 1
            cmax = max(cmax, cval)

        return arr

