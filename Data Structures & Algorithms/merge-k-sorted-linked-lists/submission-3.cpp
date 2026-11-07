/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        int k = lists.size();
        for (int step = 1; step < k; step *= 2) {
            for (int i = 0; i + step < k; i += 2 * step) {
                lists[i] = merge(lists[i], lists[i + step]);
            }
        }
        return lists[0];
    }

private:
    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;

        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val <= l2->val){
                curr->next = l1;
                l1 = l1->next;
            }else {
                curr->next = l2;
                l2 = l2->next;
            }

            curr = curr->next;
        }

        curr->next = l1 ? l1 : l2;

        return dummy->next;
    }
};
