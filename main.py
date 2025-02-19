from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in range(len(s)):
            found = 0
            for j in range(count,len(t)):
                if t[j] == s[i]:
                    count = j+1
                    found = 1
                    break
            if found == 0:
                return False
        return True

    # Definition for singly-linked list.
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            result = ListNode(list1.val)
            list1 = list1.next
        else:
            result = ListNode(list2.val)
            list2 = list2.next
        current = result
        while list1 is not None and list2 is not None:
            if list2.val <= list1.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            current = current.next
        if list2 is None:
            current.next = list1
            return result
        current.next = list2
        return result

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        while head is not None:
            result = ListNode(head.val, result)
            head = head.next
        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        result = head
        while current is not None:
            current = current.next
            count += 1
        for i in range(count//2):
            result = result.next
        return result

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checked = set()
        while head is not None:
            if checked.__contains__(head):
                return head
            checked.add(head)
            head = head.next
        return None

    def detectCycleNoMemory(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        checked = set()
        while head.next is not None:
            for i in range(100):
                if head.next is not None:
                    if checked.__contains__(head):
                        return head
                    checked.add(head)
                    head = head.next
                else:
                    return None
            fast = head.next
            for i in range(10001):
                if checked.__contains__(fast):
                    return fast
                if fast is None or fast.next is None:
                    return None
                fast = fast.next
        return None

    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        currentMin = prices[0]
        for i in range(len(prices)):
            if currentMin < prices[i]:
                if (prices[i] - currentMin) > result:
                    result = (prices[i] - currentMin)
            else:
                currentMin = prices[i]
        return result

    def longestPalindrome(self, s: str) -> int:
        result = 0
        singles = set()
        for i in range(len(s)):
            if singles.__contains__(s[i]):
                singles.remove(s[i])
                result += 2
            else:
                singles.add(s[i])
        if singles:
            result += 1
        return result

    def preorderRec(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        result = [root.val]
        if root.children:
            for i in range(len(root.children)):
                result.extend(self.preorderRec(root.children[i]))
        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = [[root.val]]
        if root.left is None and root.right is None:
            return result
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        childrenResult = []
        if left is None:
            childrenResult = right
        elif right is None:
            childrenResult = left
        elif len(left) > len(right):
            for i in range(len(left)):
                if i < len(right):
                    left[i].extend(right[i])
                childrenResult.append(left[i])
        else:
            for i in range(len(right)):
                if i < len(left):
                    left[i].extend(right[i])
                    childrenResult.append(left[i])
                else:
                    childrenResult.append(right[i])
        result.extend(childrenResult)
        return result

    def search(self, nums: List[int], target: int) -> int:
        max = len(nums)
        min = 0
        result = max//2
        while nums[result] != target:
            if max - min <= 0:
                return -1
            if nums[result] > target:
                max = result-1
            else:
                min = result+1
            result = (max+min)//2
            if result > len(nums)-1 or result < 0:
                return -1
        return result




solution = Solution()

result = solution.search([5],9)
#root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
#result = solution.levelOrder(root)
print(solution.isSubsequence("abc", "abbaac"))
