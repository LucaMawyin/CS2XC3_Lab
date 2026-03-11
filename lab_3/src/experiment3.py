class XC3Node:
    def __init__(self,degree):
        self.degree = degree
        self.children = []
        
        #Create childrend following the rule 
        for i in range (1, degree + 1):
            child_degree = i - 2 if i > 2 else 0
            self.children.append(XC3Node(child_degree))

def get_height(node):
    if len(node.children) == 0:
        return 0
    return 1 + max(get_height(c) for c in node.children)

def get_num_nodes(node):
    return 1 + sum(get_num_nodes(child) for child in node.children)

for i in range(26):
    tree = XC3Node(i)
    h = get_height(tree)
    print(f"degree={i}, height={h}")


 
    