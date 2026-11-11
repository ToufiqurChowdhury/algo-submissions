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

        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };

        priority_queue<ListNode* , vector<ListNode*>, decltype(cmp)> pq;

        ListNode dummy(0);
        ListNode* cur = &dummy;

        for (auto& l:lists) {
            if (l) {
                pq.push(l);
            }
        }

        while (!pq.empty()) {
            ListNode* node = pq.top(); pq.pop();
            cur->next = node;
            cur = cur->next;

            if(node->next) pq.push(node->next);
        }

        return dummy.next;
    }
};



