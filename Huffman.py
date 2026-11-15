from collections import Counter
import heapq

class huffmanNode:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None
    def __lt__(self,other):
        return self.freq<other.freq

def build_huffman_tree(text):
    freq=Counter(text)
    min_heap=[huffmanNode(char,freq) for char,freq in freq.items()]
    heapq.heapify(min_heap)
    while(len(min_heap)>1):
        left_node=heapq.heappop(min_heap)
        right_node=heapq.heappop(min_heap)
        merged=huffmanNode(None,left_node.freq+right_node.freq)
        merged.left=left_node
        merged.right=right_node
        heapq.heappush(min_heap,merged)
    return min_heap[0] if min_heap else None

def generate_huffman_codes(root,current_node="",codes={}):
    if root is None:
        return 
    if root.char is not None:
        codes[root.char]=current_node
        return codes
    generate_huffman_codes(root.left,current_node+"0",codes)
    generate_huffman_codes(root.right,current_node+"1",codes)

    return codes

def huffman_encoding(text):
    if not text:
        return "",{}

    if len(set(text))==1:
        return "0"*len(text),{text[0]:"0"}

    root=build_huffman_tree(text)
    huffman_codes=generate_huffman_codes(root)

    encoded_text="".join(huffman_codes[char] for char in text)
    return encoded_text,huffman_codes


if __name__=="__main__":
    sample_text="hello huffman"
    print(f"Original text: {sample_text}")
    encoded_text,huffman_codes=huffman_encoding(sample_text)
    print("Huffman Codes: ")
    for char,code in sorted(huffman_codes.items()):
        print(f"{char}: {code}")
    print(f"Encoded text: {encoded_text}")