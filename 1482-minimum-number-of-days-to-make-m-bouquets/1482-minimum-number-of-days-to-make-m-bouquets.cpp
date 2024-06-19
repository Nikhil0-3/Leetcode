class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        // Use long long to prevent overflow
        if (static_cast<long long>(m) * k > bloomDay.size()) {
            return -1;
        }

        int mi = INT_MAX, mx = INT_MIN;
        for (int& bd : bloomDay) {
            mi = min(mi, bd);
            mx = max(mx, bd);
        }

        int left = mi, right = mx;
        while (left < right) {
            int mid = left + ((right - left) >> 1); // Safe way to calculate mid
            if (check(bloomDay, m, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    bool check(vector<int>& bloomDay, int m, int k, int day) {
        int cnt = 0, cur = 0;
        for (int& bd : bloomDay) {
            cur = bd <= day ? cur + 1 : 0;
            if (cur == k) {
                ++cnt;
                cur = 0;
            }
        }
        return cnt >= m;
    }
};
