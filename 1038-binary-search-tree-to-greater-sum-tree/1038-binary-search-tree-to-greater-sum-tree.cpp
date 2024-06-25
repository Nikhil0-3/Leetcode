/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        dfs(root, 0);
        return root;
    }

private:
    int dfs(TreeNode* node, int count) {
        if (node == nullptr) return count;
        int t = dfs(node->right, count);
        node->val += t;
        return dfs(node->left, node->val);
    }
};