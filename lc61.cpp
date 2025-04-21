// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode() : val(0), next(nullptr) {}
//  *     ListNode(int x) : val(x), next(nullptr) {}
//  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
//  */
class Solution
{
public:
    ListNode *rotateRight(ListNode *head, int k)
    {

        ListNode *temp = head;
        int length = 1;

        if (head == NULL || head->next == NULL || k == 0)
        {
            return head;
        }

        while (temp->next)
        {
            temp = temp->next;
            length++;
        }
        k = k % length;
        if (k == 0)
        {
            return head;
        }
        ListNode *new_tail = head;
        ListNode *new_head;

        for (int i = 0; i < (length - k - 1); i++)
        {
            new_tail = new_tail->next;
        }

        new_head = new_tail->next;
        new_tail->next = NULL;
        temp->next = head;

        return new_head;
    }
};