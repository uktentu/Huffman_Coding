import heapq, math

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

def calculate_entropy(probabilities, base):
    entropy = -sum(p * math.log(p, base) for p in probabilities if p > 0)
    return entropy

def calculate_average_code_length(symbols, probabilities, huffman_codes):
    pro_sym = {symbol: probability for symbol,probability in zip(symbols,probabilities)}
    total_length = list(len(list(huffman_codes[symbol])) * pro_sym[symbol] for symbol in symbols)

    return sum(total_length)

def calculate_efficiency(entropy, average_code_length):
    efficiency = entropy / average_code_length
    return efficiency

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
    
    # H -> Entropy
    entropy = calculate_entropy(values, base)
    print("Entropy : ",round(entropy,4))

    #L -> AvgCodeLength
    average_code_length = calculate_average_code_length(symbols, values, huffman)
    print("Average Code Word Length: ",round(average_code_length,4))

    # Calculate efficiency
    efficiency = calculate_efficiency(entropy, average_code_length)
    print("Efficiency: ",round(efficiency,4))
