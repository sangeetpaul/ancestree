import unittest
import full_binary

mergers = dict()
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
tree_9 = '''
   ┌───┴───┐   
 ┌─┴─┐   ┌─┴─┐ 
┌┴┐ ┌┴┐ ┌┴┐    
'''


class AncestreeTestCase(unittest.TestCase):
    def test_merge(self):
        for merger in mergers:
            self.assertEqual(mergers[merger], full_binary.merge_trees(*merger), 'Merging '+str(merger))

    def test_split(self):
        for merger in mergers:
            self.assertEqual(merger, full_binary.split_tree(mergers[merger]), 'Splitting ' + str(mergers[merger]))

    def test_height(self):
        for tree in heights:
            self.assertEqual(heights[tree], full_binary.height_of_tree(tree))

    def test_n_nodes(self):
        for tree in n_nodes:
            self.assertEqual(n_nodes[tree], full_binary.n_nodes_in_tree(tree))

    def test_n_leaves(self):
        for tree in n_leaves:
            self.assertEqual(n_leaves[tree], full_binary.n_leaves_in_tree(tree))

    def test_diagram(self):
        self.assertEqual(tree_9, full_binary.show_tree(9))


if __name__ == '__main__':
    unittest.main()
