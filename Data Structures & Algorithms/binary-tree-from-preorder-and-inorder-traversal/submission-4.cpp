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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> position;

        // Store each value's index in inorder
        for (int i = 0; i < inorder.size(); i++) {
            position[inorder[i]] = i;
        }

        int preorderIndex = 0;

        return build(preorder, position, preorderIndex, 0, inorder.size() - 1);
    }

private:
    TreeNode* build(
        vector<int>& preorder,
        unordered_map<int, int>& position,
        int& preorderIndex,
        int left,
        int right
    ) {
        // No values in this subtree
        if (left > right) {
            return nullptr;
        }

        // The next preorder value is always the root
        int rootValue = preorder[preorderIndex++];
        TreeNode* root = new TreeNode(rootValue);

        // Find the root's position in inorder
        int middle = position[rootValue];

        // Values to the left form the left subtree
        root->left = build(
            preorder,
            position,
            preorderIndex,
            left,
            middle - 1
        );

        // Values to the right form the right subtree
        root->right = build(
            preorder,
            position,
            preorderIndex,
            middle + 1,
            right
        );

        return root;
    }
};