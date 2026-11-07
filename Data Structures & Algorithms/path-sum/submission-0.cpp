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
    bool hasPathSum(TreeNode* root, int targetSum) {

        return dfs(root, targetSum, 0);
        
    }

    bool dfs(TreeNode* root, int targetSum, int currentSum){

        if (root == nullptr){
            return false;
        }

        currentSum = currentSum + root->val;

        if (root->left == nullptr and root->right == nullptr){
            if (currentSum == targetSum){
                return true;
            }

        }

        bool left = dfs(root->left, targetSum, currentSum);
        if (left){
            return true;
        }
        bool right = dfs(root->right, targetSum, currentSum);
        if (right){
            return true;
        }

        return false;
    }
};