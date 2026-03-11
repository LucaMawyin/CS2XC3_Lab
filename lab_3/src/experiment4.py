class XC3Node:
    def __init__(self,degree):
        self.degree = degree
        self.children = []
        for i in range (1, degree + 1):
            child_degree = (i - 2) if i > 2 else 0
            self.children.append(XC3Node(child_degree))

def get_nodes(node):
    return 1 + sum(get_nodes(c) for c in node.children)

for i in range (26):
    tree = XC3Node(i)
    print(f"degree = {i}, nodes = {get_nodes(tree)}")
