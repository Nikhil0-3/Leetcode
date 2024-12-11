class Solution:
    def maximumBeauty(self, flowers: List[int], steps: int) -> int:
        # Calculate the maximum constant for adjusting the range
        max_flower = max(flowers) + steps * 2 + 2
      
        # Initialize a difference array with the same range
        diff_array = [0] * max_flower
      
        # Construct the difference array to perform range updates
        for flower_count in flowers:
            diff_array[flower_count] += 1
            diff_array[flower_count + steps * 2 + 1] -= 1
      
        # Initialize the variables for tracking the maximum beauty and the running sum
        max_beauty = running_sum = 0
      
        # Apply the difference array technique to find the total at each point
        for count_diff in diff_array:
            running_sum += count_diff
            max_beauty = max(max_beauty, running_sum)
      
        # Return the maximum beauty value found
        return max_beauty   