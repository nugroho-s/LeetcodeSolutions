/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var remainder = 0;
        val lr = ListNode(0);
        var lrn = lr;
        var n1 = l1;
        var n2 = l2;
        do {
            var v1 = n1?.`val` ?: 0;
            var v2 = n2?.`val` ?: 0;
            lrn.`val` = (v1 + v2 + remainder) % 10;
            remainder = (v1 + v2 + remainder).div(10);
            n1 = n1?.next ?: null;
            n2 = n2?.next ?: null;
            if (n1 != null || n2 != null) {
                lrn.next = ListNode(0);
                lrn = lrn.next;
            }
        } while (n1 != null || n2 != null)
        if (remainder > 0) {
            lrn.next = ListNode(remainder);
        }
        return lr;
    }
}
