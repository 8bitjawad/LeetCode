class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        #using set ops:

        set1,set2 = set(nums1), set(nums2)
        return [list(set1-set2), list(set2-set1)]
    
        #using loops
        # set1 = set(nums1)
        # set2 = set(nums2)
        # temp = []
        # answers = []

        # for i in range(len(nums1)):
        #     if nums1[i] not in set2 and nums1[i] not in temp:
        #         temp.append(nums1[i])
        
        # answers.append(temp.copy())
        
        # temp.clear()

        # for i in range(len(nums2)):
        #     if nums2[i] not in set1 and nums2[i] not in temp:
        #         temp.append(nums2[i])
        # answers.append(temp.copy())

        # return answers
        