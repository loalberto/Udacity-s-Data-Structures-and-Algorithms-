class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # If there are two empty lists then we get an empty union.
    if llist_1.head is None and llist_2.head is None:
        return None

    union_list = LinkedList()

    if llist_1.head is None:
        union_list.head = Node(llist_2.head.value)
        lis1_iter = llist_2.head.next
        union_nodes = union_list.head
    else:
        union_list.head = Node(llist_1.head.value)
        lis1_iter = llist_1.head.next
        union_nodes = union_list.head

    # I will iterate one list at a time.
    # Assuming no duplicates, I get a list and add one item at a time.
    while lis1_iter is not None:
        while union_list is not None:
            # If a duplicate is present then I skip it
            if lis1_iter.value == union_nodes.value:
                union_nodes = union_list.head
                break
            # Else I add it to the back of the union list.
            if union_nodes.next is None:
                temp = Node(lis1_iter.value)
                union_nodes.next = temp
                break
            union_nodes = union_nodes.next
        union_nodes = union_list.head
        lis1_iter = lis1_iter.next

    # I do the same for list 2 by attaching it to the already constructed union list.

    if llist_2.head is not None:
        union_nodes = union_list.head
        lis2_iter = llist_2.head

        while lis2_iter is not None:
            while union_nodes is not None:
                if lis2_iter.value == union_nodes.value:
                    union_nodes = union_list.head
                    break
                if union_nodes.next is None:
                    temp = Node(lis2_iter.value)
                    union_nodes.next = temp
                    break
                union_nodes = union_nodes.next
            union_nodes = union_list.head
            lis2_iter = lis2_iter.next
    return union_list


def intersection(llist_1, llist_2):
    # Check if any of the lists are empty. If one is then there is no intersection
    if llist_1.head is None or llist_2.head is None:
        return None
    inter_list = LinkedList()
    # I want to start from each of the list's first node.
    first_list = llist_1.head
    second_list = llist_2.head
    inter_node = None

    # I will traverse element by element in the first list
    # and compare it to each element in the second list
    while first_list is not None:
        while second_list is not None:
            # If there is match then:
            if first_list.value == second_list.value:
                # I add it as the new list's head node
                if inter_list.head is None:
                    inter_list.head = Node(first_list.value)
                    inter_node = inter_list.head
                    break
                else:
                    # Else I see if it already exists in the list
                    while inter_node is not None:
                        # If it exists, then I skip it since I am assuming no duplicates in an intersection
                        if inter_node.value == first_list.value:
                            inter_node = inter_list.head
                            break
                        # If it's not there then I add it to the back of the new list
                        if inter_node.next is None:
                            inter_node.next = Node(first_list.value)
                            break
                        inter_node = inter_node.next
            second_list = second_list.next
        first_list = first_list.next
        second_list = llist_2.head

    if inter_list.head is None:
        return None

    return inter_list


def test_case(element_1, element_2):
    list1 = LinkedList()
    list2 = LinkedList()

    for i in element_1:
        list1.append(i)

    for i in element_2:
        list2.append(i)

    print(union(list1, list2))
    print(intersection(list1, list2))


print('Test case 1')
# Test case 1
"""Test case 1 will have both a successful union and intersection"""
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

test_case(element_1, element_2)

print('Test case 2')
# Test case 2
"""Test case 2 will have only a union of elements in element_2 and an empty intersection"""
element_1 = []
element_2 = [2, 3, 4, 5, 5]

test_case(element_1, element_2)

print('Test case 3')
# Test case 3
"""Test case 3 will have a union of elements in element_1 and an empty intersection"""
element_1 = [2, 3, 4, 5]
element_2 = []

test_case(element_1, element_2)

print('Test case 4')
# Test case 4
"""Test case 4 will have a union of 1 - 10 and an empty intersection"""
element_1 = [1, 2, 3, 4, 5]
element_2 = [6, 7, 8, 9, 10]

test_case(element_1, element_2)

print('Test case 5')
#Test case 5
"""Test case 5 will have an empty union and intersection"""
element_1 = []
element_2 = []

test_case(element_1, element_2)