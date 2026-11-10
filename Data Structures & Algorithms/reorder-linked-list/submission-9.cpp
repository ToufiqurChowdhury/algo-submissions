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
    void reorderList(ListNode* head) {
        ListNode* slow=head;
        ListNode* fast=head;
        while (fast && fast->next) {
            slow=slow->next;
            fast=fast->next->next;
        }

        ListNode* cur = slow;
        ListNode* prev = NULL;
        while (cur) {
            ListNode* tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }

        ListNode* first=head;
        ListNode* second=prev;
        while (second->next != nullptr) {
            ListNode* tmp1 = first->next;
            first->next = second;
            first = tmp1;

            ListNode* tmp2 = second->next;
            second->next = first;
            second = tmp2;
        }
    }
};
