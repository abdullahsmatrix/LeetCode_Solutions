class Solution:
    """Understanding the Algorithm: 
    Test case: [2, 7, 11, 15], Target: 9
    
    Lets say we carry a notebook as we enter a room with number 2.
    We see 2. To hit 9 we need 7. Do we have 7 in notebook?
    YES: We have the solution.
    NO: Move to the next room.
    Since we don't have 7 on our note book, we note burrent room index and number. notebook[room_number] = room_index
    Next room: 7. To hit 9 we need 2. Do we have 2 in our notebook? Yes. 

    EUREKA! 
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map: dict = {}
        for i, n in enumerate(nums):
            difference = target - nums[i]
            if difference in num_map:
                return[num_map[difference], i]
            num_map[n] = i
        return []

