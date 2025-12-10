class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        h=n-1

        while l<h:
            add=numbers[l]+numbers[h]
            if add==target:
                return [l+1,h+1]
                
            elif add<target:
                l+=1
            else:
                h-=1
           
                
                    
                