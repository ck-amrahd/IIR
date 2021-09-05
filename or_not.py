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

    def to_set(self):
        nodes = []
        node = self.head
        while node is not None:
            if node.data not in nodes:
                nodes.append(node.data)
            node = node.next
        return set(nodes)


l1 = LinkedList([1, 2, 4, 11, 15])
l2 = LinkedList([2, 3, 5, 10, 15, 17])
total_doc = 20
doc = list(range(1, total_doc + 1))
not_l2 = LinkedList(list(set(doc) - l2.to_set()))

print(f"l1: {l1}")
print(f"l2: {l2}")
print(f"NOT l2: {not_l2}\n")

ans_naive = []

p1 = l1.head
p2 = not_l2.head

while p1 is not None and p2 is not None:
    if p1.data == p2.data:
        ans_naive.append(p1.data)
        p1 = p1.next
        p2 = p2.next
    elif p1.data < p2.data:
        ans_naive.append(p1.data)
        p1 = p1.next
    else:
        ans_naive.append(p2.data)
        p2 = p2.next

# One of them will be None
if p1 is not None:
    while p1 is not None:
        ans_naive.append(p1.data)
        p1 = p1.next

if p2 is not None:
    while p2 is not None:
        ans_naive.append(p2.data)
        p2 = p2.next

print(f"l1 or NOT l2 naive: {ans_naive}")

p1 = l1.head
p2 = l2.head

ans = []
for docId in doc:
    if p2 is None:
        ans.append(docId)
    else:
        if docId < p2.data:
            ans.append(docId)
            continue
        elif docId == p2.data:
            # check if p1 has the same data
            found_in_p1 = False
            while p1 is not None:
                if p1.data == p2.data:
                    found_in_p1 = True
                    break
                elif p1.data > p2.data:
                    break
                else:
                    p1 = p1.next

            if found_in_p1:
                ans.append(docId)

            p2 = p2.next


assert ans == ans_naive

print(f"l1 or NOT l2 optimized: {ans}")

# outputs following:
# l1: 1 -> 2 -> 4 -> 11 -> 15 -> None
# l2: 2 -> 3 -> 5 -> 10 -> 15 -> 17 -> None
# NOT l2: 1 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 12 -> 13 -> 14 -> 16 -> 18 -> 19 -> 20 -> None

# l1 or NOT l2 naive: [1, 2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20]
# l1 or NOT l2 optimized: [1, 2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20]
