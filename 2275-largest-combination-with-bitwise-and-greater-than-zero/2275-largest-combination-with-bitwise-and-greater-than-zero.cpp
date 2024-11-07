class Solution {
public:
    int largestCombination(std::vector<int>& candidates) {
        // Declare 'BITS' to specify the number of bits to check in each number.
        const int BITS = 24;
      
        // Initialize 'maxCount' to 0 to keep track of the maximum count of numbers that have the same bit set.
        int maxCount = 0;
      
        // Iterate over each bit position from 0 to 'BITS - 1'.
        for (int i = 0; i < BITS; ++i) {
            // Initialize 'bitCount' to count the number of candidates with the current bit set.
            int bitCount = 0;
          
            // Iterate through each number in the 'candidates' vector.
            for (int num : candidates) {
                // Use bitwise operations to check if the bit at position 'i' is set.
                if ((num >> i) & 1) {
                    // If the current bit is set, increment 'bitCount'.
                    bitCount++;
                }
            }
          
            // Update 'maxCount' if 'bitCount' of the current bit is greater than the 'maxCount' found so far.
            maxCount = std::max(maxCount, bitCount);
        }
      
        // Return the maximum count of numbers that have the same bit set.
        return maxCount;
    }
};