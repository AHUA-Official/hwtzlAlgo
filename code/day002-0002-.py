"""
2. 两数相加 (Add Two Numbers)

题目描述：
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807

解题思路：
1. 同时遍历两个链表，对应位置的数字相加（注意进位）
2. 如果一个链表遍历完了，另一个链表还有剩余，继续遍历剩余部分
3. 最后检查是否还有进位，如果有，需要增加新节点

时间复杂度：O(max(m,n))，其中m和n分别为两个链表的长度
空间复杂度：O(max(m,n))，返回的链表长度最大为max(m,n) + 1
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # 哑节点
        curr = dummy
        carry = 0  # 进位
        
        while l1 or l2 or carry:
            # 获取当前位的值
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # 计算和与进位
            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            # 移动指针
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

# 测试代码
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def linked_list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_add_two_numbers():
    solution = Solution()
    
    # 测试用例1
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [7,0,8]
    
    # 测试用例2
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [0]
    
    # 测试用例3
    l1 = create_linked_list([9,9,9,9])
    l2 = create_linked_list([9,9,9])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [8,9,9,0,1]
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_add_two_numbers()


    