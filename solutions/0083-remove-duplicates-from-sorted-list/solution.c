/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(!head || ! head->next) return head;
    struct ListNode * dummy=head;
    struct ListNode* next=head->next;
    while(next){
        if (dummy->val == next->val){
            dummy->next=next->next;
            next=next->next;
        }
        else{
            dummy=dummy->next;
            next=next->next;
        }
    }
    return head;
}
