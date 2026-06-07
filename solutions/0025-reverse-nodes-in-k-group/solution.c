/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (!head || k == 1)
        return head;

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode* prevGroupEnd = &dummy;
    struct ListNode* curr = head;

    while (curr) {
        struct ListNode* kthNode = curr;
        for (int i = 1; i < k && kthNode; i++)
            kthNode = kthNode->next;

        if (!kthNode)
            break;

        struct ListNode* nextGroupStart = kthNode->next;
        struct ListNode* prev = nextGroupStart;
        struct ListNode* node = curr;
        for (int i = 0; i < k; i++) {
            struct ListNode* next = node->next;
            node->next = prev;
            prev = node;
            node = next;
        }

        prevGroupEnd->next = kthNode;
        prevGroupEnd = curr;
        curr = nextGroupStart;
    }
    return dummy.next;
}
