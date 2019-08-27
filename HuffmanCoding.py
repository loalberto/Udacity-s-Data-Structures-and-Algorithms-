import sys


class Node:
    def __init__(self, val, key=''):
        self.key = key
        self.val = val
        self.code = None
        self.left = None
        self.right = None


# This will fill each node with its designated '0' or '1'
# I am using a DFS approach to traverse the tree
def fill_codes(node):
    if node.left is None and node.right is None:
        return

    if node.left is not None:
        node.left.code = '0'
        fill_codes(node.left)
    if node.right is not None:
        node.right.code = '1'
        fill_codes(node.right)


# This will traverse each node to get each leaves(letters) and their codes
# It will then store it into a dictionary to easily store each letter's compressed value
def get_letter_codes(di, node, val):
    if node.left is None and node.right is None:
        di[node.key] = '{}'.format(node.code) + val
        return
    get_letter_codes(di, node.left, val + node.left.code)
    get_letter_codes(di, node.right, val + node.right.code)


def huffman_encoding(data):
    if data is None:
        return None

    val = {}
    # I broke the data into single characters
    for char in data:
        if char not in val:
            val[char] = 1
            continue
        val[char] += 1
    # Then there is only 1 character
    if len(val) == 1:
        first_node = Node(val[data[0]], data[0])
        root = Node(first_node.val)
        root.left = first_node
        first_node.code = 0
        result = '0' * val[data[0]]
        return result, root

    # Then sorted them in increasing order
    sorted_values = sorted(val.items(), key=lambda x: x[1])
    # I used a queue to help me build the tree
    queue_of_nodes = [Node(value[1], value[0]) for value in sorted_values]
    queue_of_nodes.append(Node(None))
    # I make sure that it breaks once there are two nodes left in the queue
    while len(queue_of_nodes) > 2:
        left_node = queue_of_nodes.pop(0)
        # If the left node has a None value then we need to append to the end and continue
        if left_node.val is None:
            queue_of_nodes.append(left_node)
            continue
        # Similarly, if the right node's value is ever None
        # then we put both the left node and None Node to the back
        right_node = queue_of_nodes.pop(0)
        if right_node.val is None:
            queue_of_nodes.append(left_node)
            queue_of_nodes.append(right_node)
            continue
        # My method continously takes two nodes in the queue and creates an internal node for them
        # This internal node is then put in the queue. I keep doing this until I have two nodes left
        # in the queue. Also linking each internal node with the left and right node.
        internal_node = Node(left_node.val + right_node.val)
        internal_node.left = left_node
        internal_node.right = right_node
        queue_of_nodes.append(internal_node)

    # In the end I will have the None Node or the root Node in the Queue
    root = queue_of_nodes.pop(0)
    if root.val is None:
        root = queue_of_nodes.pop(0)
    # Then I use the root node to give each node its designated code (0 or 1)
    fill_codes(root)
    di = {}
    # Next I store the letter's new compressed representation in a dictionary
    get_letter_codes(di, root, '')
    e = ''
    # join everything together and output a result
    for char in data:
        e += di[char]
    return e, root


def huffman_decoding(data, dec_tree):
    if data is None or dec_tree is None:
        return

    # When there is no node on the right then that means that we are dealing
    # with a data string that only contains 1 character.
    if dec_tree.right is None:
        count = len(data)
        get_letter = dec_tree.left.key
        return get_letter * count

    final_value = ''
    temp = {}
    # I store the designated codes in a dictionary again
    get_letter_codes(temp, dec_tree, '')
    generated_dict = {}

    # Swap the keys and values to traverse easier
    for key in temp:
        generated_dict[temp[key]] = key
    v = ''

    # Check character by character for when there is a match in the dictionary
    # When there is match, I store that value into the final_result variable
    for char in data:
        v += char
        if v in generated_dict:
            final_value += generated_dict[v]
            v = ''
    return final_value


# Test case 1: Normal test

"""This will compress the data and then decompress it"""

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


# Test case 2: Large input data

"""This should still return the data compressed"""

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 3: This will return to the console an error of NoneType and ValueType

if __name__ == "__main__":
    codes = {}

    a_great_sentence = None

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))


    try:
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

    except (TypeError, ValueError):
        print('Error')

# Test case 4: Dealing with a single character should mean we get a compressed code with the same 0/1
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "aaaaaaaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))