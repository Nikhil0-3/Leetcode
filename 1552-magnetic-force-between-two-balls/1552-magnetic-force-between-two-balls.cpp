class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        int n = position.size();
        sort(position.begin(), position.end());
        int left = 1, right = position[n-1] - position[0];
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (canPlaceBalls(position, m, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    bool canPlaceBalls(vector<int>& position, int m, int force) {
        int prev = position[0];
        int count = 1;
        for (int i = 1; i < position.size() && count < m; i++) {
            if (position[i] - prev >= force) {
                prev = position[i];
                count++;
            }
        }
        return count >= m;
    }
};