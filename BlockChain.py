import hashlib
import time


class Block:
    # I added the next variable to be able to traverse the blockchain
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    # I added the data that was going to be hashed
    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    # This has a variable recent_block that will be used to attach each block
    # to the block's previous hashcode
    def __init__(self, head):
        self.head = head
        self.recent_block = None
        self.size = 0
        self.node = None

    # I created this function like in a linked list
    def add_element(self, data):

        # If the data is none then just return
        if data is None or len(data) == 0:
            return
        # This will be used to retrieve the curretn GMT
        gmt_time = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

        # I will build the block with setting the previous_hash as None

        block = Block(gmt_time, data, None)

        # This is for when there is no head created yet
        if self.size == 0:
            self.head = block

            # The first block will not have a previous_hash
            self.head.previous_hash = 0
            self.recent_block = self.head
            self.node = self.head
            self.size += 1
            return

        # When a head already exists then we just attach the block to the chain/
        # Setting the previous_hash to the block before it

        self.node.next = block
        self.node = self.node.next
        block.previous_hash = self.recent_block.hash
        self.recent_block = block
        self.size += 1

    # The next variable comes in handy here because it
    # let's me access each block one by one.
    def print_info(self):
        temp = self.head
        while temp is not None:
            print("The block's timestamp is: {}".format(temp.timestamp))
            print("The block's data is: {}".format(temp.data))
            print("The block's current hash is: {}".format(temp.calc_hash()))
            print("The block's previous_hash is: {}\n".format(temp.previous_hash))
            temp = temp.next


# Test Case 1: first run when there is data for each block

"""Will print the information for each block and the previous hash """

a = "This is data"
b = "This is more data"
c = "This is my last data"
d = ''

block_chain = BlockChain(None)
block_chain.add_element(a)
block_chain.add_element(b)
block_chain.add_element(c)
# These last two blocks will not be created
block_chain.add_element(None)
block_chain.add_element(d)
block_chain.print_info()
