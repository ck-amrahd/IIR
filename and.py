class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes):
        node = Node(nodes.pop(0))
        self.head = node
        for node_data in nodes:
            node.next = Node(node_data)
            node = node.next

    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


l1 = LinkedList([1, 2, 4, 11, 31, 45, 173, 174])
l2 = LinkedList([2, 31, 54, 101])

print(f"l1: {l1}")
print(f"l2: {l2}\n")

ans = []

p1 = l1.head
p2 = l2.head

while p1 is not None and p2 is not None:
    if p1.data == p2.data:
        ans.append(p1.data)
        p1 = p1.next
        p2 = p2.next
    elif p1.data < p2.data:
        p1 = p1.next
    else:
        p2 = p2.next


print(f"l1 AND l2: {ans}")
