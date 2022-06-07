# Full Binary Trees
# Merger Ancestries

# n_trees[i] = number of full binary trees of height <= i
# n_trees[i] = number of possible ancestries after i evolutions
# n_trees[i] = n[i-1]*(n[i-1]+1)/2 + 1
n_trees = [1, 2, 4, 11, 67, 2279, 2598061, 3374961778892, 5695183504492614029263279,
           16217557574922386301420536972254869595782763547561,
           131504586847961235687181874578063117114329409897615188504091716162522225834932122128288032336298142]

# h_trees[i] = number of full binary trees of height = i
# h_trees[i] = number of possible max-gen ancestries after i evolutions
# h_trees[i] = h[i-1]*(h[i-2]+...+h[0]) + n[i-1]*(n[i-1]+1)/2
h_trees = [1, 1, 2, 7, 56, 2212, 2595782, 3374959180831, 5695183504489239067484387,
           16217557574922386301420531277071365103168734284282,
           131504586847961235687181874578063117114329409897598970946516793776220805297959867258692249572750581]


def merge_trees(tree1: int, tree2: int):
    n, m = sorted([tree1, tree2])  # n <= m
    return m*(m+1)//2 + n + 1


def split_tree(tree: int):
    if tree == 0:
        return None, None
    elif tree == 1:
        return 0, 0
    h = height_of_tree(tree)
    n = tree - n_trees[h-1]
    for m in range(n_trees[h-2], n_trees[h-1]):
        if n <= m:
            return m, n
        else:
            n -= m+1


def height_of_tree(tree: int):
    # generation-1 (natal = 1st gen)
    if tree in n_trees:
        return n_trees.index(tree) + 1
    else:
        return sorted([tree] + n_trees).index(tree)


def height_of_tree_recursive(tree: int):
    # generation-1
    if tree == 0:
        return 0
    else:
        m, n = split_tree(tree)
        # return max(height_of_tree(m), height_of_tree(n)) + 1
        # max(h(m),h(n)) = h(m) as m>=n and h is non-decreasing
        return height_of_tree(m) + 1


def n_leaves_in_tree(tree: int):
    # n_natal
    if tree == 0:
        return 1
    else:
        m, n = split_tree(tree)
        return n_leaves_in_tree(m) + n_leaves_in_tree(n)


def n_nodes_in_tree(tree: int):
    # n_mergers
    return n_leaves_in_tree(tree) - 1


def n_vertices_in_tree(tree: int):
    # n_objects
    return 2*n_leaves_in_tree(tree) - 1


def show_tree(tree: int):
    if tree == 0:
        return '│'
    h = height_of_tree(tree)
    components = [tree]
    diagram = '\n'
    for row in range(h, 0, -1):
        new_components = []
        node = '┌'+'─'*(2**(row-1)-1)+'┴'+'─'*(2**(row-1)-1)+'┐'
        no_node = ' '*len(node)
        spacing = ' '*(len(node)-2)
        diagram += ' '*(2**(row-1)-1)  # blank at start of row
        for i in range(len(components)):
            new_components.extend(split_tree(components[i]))
            if components[i]:
                diagram += node
            else:
                diagram += no_node
            if i < len(components)-1:
                diagram += spacing
        components = [0 if None else i for i in new_components]
        diagram += ' '*(2**(row-1)-1)  # blank at end of row
        diagram += '\n'  # line change at end of row
    return diagram


def merge_tree_stats(height1: int, n_leaves1: int, height2: int, n_leaves2: int):
    height = max(height1, height2) + 1
    n_leaves = n_leaves1 + n_leaves2
    return height, n_leaves
