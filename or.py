class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


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

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


l1 = LinkedList([1, 2, 4, 11, 31, 45, 173, 174])
l2 = LinkedList([2, 31, 54, 101])

print(f"l1: {l1}")
# print(f"l2: {l2}\n")

# check __iter__
print("l2:")
for nd in l2:
    print(nd)

ans = []

p1 = l1.head
p2 = l2.head

while p1 is not None and p2 is not None:
    if p1.data == p2.data:
        ans.append(p1.data)
        p1 = p1.next
        p2 = p2.next
    elif p1.data < p2.data:
        ans.append(p1.data)
        p1 = p1.next
    else:
        ans.append(p2.data)
        p2 = p2.next

# One of them will be None
if p1 is not None:
    while p1 is not None:
        ans.append(p1.data)
        p1 = p1.next

if p2 is not None:
    while p2 is not None:
        ans.append(p2.data)
        p2 = p2.next

print(f"l1 OR l2: {ans}")
