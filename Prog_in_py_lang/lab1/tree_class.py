class TreeNode:

    def __init__(self,value):
        self.value = value
        self.children = []

    def add_child(self,value):
        self.children.append(TreeNode(value))

    def traverse(self):
        yield self
        for child in self.children:
            yield from child.traverse()
            
    def __str__(self, level=0,):
        indent = "  " * level
        result = f"{indent}{self.value}\n"
        for child  in self.children:
            result += child.__str__(level + 1)
        return result

    


