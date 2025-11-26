import unittest
import full_binary

mergers = {}
m, n, p = 0, 0, 1
while p <= 10:
    mergers[(m, n)] = p
    if m == n:
        m += 1
        n = 0
    else:
        n += 1
    p += 1
heights = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3, 10: 3, 11: 4}
n_nodes = {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 10: 7, 11: 4}
n_leaves = {0: 1, 1: 2, 2: 3, 3: 4, 4: 4, 5: 5, 10: 8, 11: 5}
TREE_9 = '''
   ┌───┴───┐   
 ┌─┴─┐   ┌─┴─┐ 
┌┴┐ ┌┴┐ ┌┴┐    
'''


class AncestreeTestCase(unittest.TestCase):
    def test_merge(self):
        for m_n, p_val in mergers.items():
            self.assertEqual(p_val, full_binary.merge_trees(*m_n), 'Merging '+str(m_n))

    def test_split(self):
        for m_n, p_val in mergers.items():
            self.assertEqual(m_n, full_binary.split_tree(p_val), 'Splitting ' + str(p_val))

    def test_height(self):
        for tree, height in heights.items():
            self.assertEqual(height, full_binary.height_of_tree(tree))

    def test_n_nodes(self):
        for tree, n_node in n_nodes.items():
            self.assertEqual(n_node, full_binary.n_nodes_in_tree(tree))

    def test_n_leaves(self):
        for tree, n_leaf in n_leaves.items():
            self.assertEqual(n_leaf, full_binary.n_leaves_in_tree(tree))

    def test_diagram(self):
        self.assertEqual(TREE_9, full_binary.show_tree(9))


if __name__ == '__main__':
    unittest.main()
