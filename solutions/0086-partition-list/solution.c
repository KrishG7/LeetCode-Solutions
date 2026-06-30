/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) {
    if(!head || !head->next) return head;

    struct ListNode lessHead, greatHead;
    struct ListNode * less=&lessHead;
    struct ListNode * great=&greatHead;

    less->next=NULL;
    great->next=NULL;

    struct ListNode * curr=head;
    while(curr){
        if (curr->val<x){
            less->next=curr;
            less=less->next;
        }
        else{
            great->next=curr;
            great=great->next;
        }
        curr=curr->next;
    }
    great->next=NULL;
    // Connect the end of 'less' list to the start of 'great' list
    less->next=greatHead.next;

    return lessHead.next;
}

