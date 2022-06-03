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


def merge_trees(i1: int, i2: int):
    n, m = sorted([i1, i2])  # n <= m
    return m*(m+1)//2 + n + 1


def split_tree(i: int):
    if i == 0:
        return 0
    elif i == 1:
        return 0, 0
    h = height_of_tree(i)
    n = i-n_trees[h-1]
    for m in range(n_trees[h-2], n_trees[h-1]):
        if n <= m:
            return m, n
        else:
            n -= m+1


def height_of_tree(i: int):
    # generation-1
    if i in n_trees:
        return n_trees.index(i) + 1
    else:
        return sorted([i] + n_trees).index(i)


def height_of_tree_recursive(i: int):
    # generation-1
    if i == 0:
        return 0
    else:
        m, n = split_tree(i)
        return max(height_of_tree(m), height_of_tree(n)) + 1


def n_nodes_in_tree(i: int):
    # n_mergers
    if i == 0:
        return 0
    else:
        m, n = split_tree(i)
        return n_nodes_in_tree(m) + n_nodes_in_tree(n) + 1


def n_leaves_in_tree(i: int):
    # n_natal
    if i == 0:
        return 1
    else:
        m, n = split_tree(i)
        return n_leaves_in_tree(m) + n_leaves_in_tree(n)
