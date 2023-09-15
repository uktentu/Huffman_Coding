import heapq

class node:
    def __init__(self, value, symbol, children=None):
        self.value = value
        self.symbol = symbol
        self.children = children
        self.huff = ''

    def __lt__(self, nxt):
        return self.value < nxt.value

def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if node.children:
        for i, child in enumerate(node.children):
            child.huff = i
            printNodes(child, newVal)
    else:
        print(f"{node.symbol} -> {newVal}")

def buildHuffmanTree(symbols, values, base):
    nodes = []
    for x in range(len(symbols)):
        heapq.heappush(nodes, node(values[x], symbols[x]))

    while len(nodes) > 1:
        children = [heapq.heappop(nodes) for _ in range(min(base, len(nodes)))]
        newNode = node(sum(child.value for child in children), ''.join(child.symbol for child in children), children)
        heapq.heappush(nodes, newNode)
        
    return nodes[0]

if __name__ == "__main__":
    # Define the base (e.g., 2, 3, 4, ...)
    base = 3

    # Symbols
    symbols = ['a', 'b', 'c', 'd', 'e', 'f']
    values = [0.05, 0.09, 0.12, 0.13, 0.16, 0.45] # probabilities

    # Build the Huffman Tree
    root = buildHuffmanTree(symbols, values, base)

    # Printing the result Huffman Code
    printNodes(root)
