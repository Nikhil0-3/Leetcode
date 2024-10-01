class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> remainderFreq(k, 0);
        
        for (int num : arr) {
            int remainder = ((num % k) + k) % k;
            remainderFreq[remainder]++;
        }

        if (remainderFreq[0] % 2 != 0) {
            return false;
        }

        for (int i = 1; i < k; i++) {
            if (remainderFreq[i] != remainderFreq[k - i]) {
                return false;
            }
        }

        return true;
    }
};