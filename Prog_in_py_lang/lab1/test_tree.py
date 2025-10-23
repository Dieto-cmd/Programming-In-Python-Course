import unittest
from tree_class import TreeNode  # <-- podmień na właściwą nazwę pliku

class TestTreeNode(unittest.TestCase):

    def test_node_initialization(self):
        node = TreeNode("A")
        print("Testing node initialization:")
        print("Expected value: 'A', Actual value:", node.value)
        print("Expected children: [], Actual children:", node.children)
        self.assertEqual(node.value, "A")
        self.assertEqual(node.children, [])

    def test_add_child(self):
        root = TreeNode("A")
        root.add_child("B")
        root.add_child("C")
        print("\nTesting add_child:")
        print("Expected number of children: 2, Actual:", len(root.children))
        print("Expected first child value: 'B', Actual:", root.children[0].value)
        print("Expected second child value: 'C', Actual:", root.children[1].value)
        self.assertEqual(len(root.children), 2)
        self.assertEqual(root.children[0].value, "B")
        self.assertEqual(root.children[1].value, "C")

    def test_traverse(self):
        root = TreeNode("A")
        root.add_child("B")
        root.add_child("C")
        root.children[0].add_child("D")
        traversal_values = [node.value for node in root.traverse()]
        expected_traversal = ["A", "B", "D", "C"]
        print("\nTesting traverse:")
        print("Expected traversal:", expected_traversal)
        print("Actual traversal:  ", traversal_values)
        self.assertEqual(traversal_values, expected_traversal)

    def test_str_representation(self):
        root = TreeNode("A")
        root.add_child("B")
        root.add_child("C")
        root.children[0].add_child("D")
        expected_output = (
            "A\n"
            "  B\n"
            "    D\n"
            "  C\n"
        )
        actual_output = str(root)
        print("\nTesting __str__ representation:")
        print("Expected output:\n" + expected_output)
        print("Actual output:\n" + actual_output)
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
