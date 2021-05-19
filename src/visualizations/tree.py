
import numpy as np
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import tkinter
from globals import get_tree_dataset

def generate_tree(val):
    treeMaxLeafNodes = val
    datasetId = get_tree_dataset()
    dataSet = None

    if datasetId == 0:
        dataSet = load_iris()
    elif datasetId == 1:
        dataSet = load_digits()
    elif datasetId == 2:
        dataSet = load_wine()
    elif datasetId == 3:
        dataSet = load_wine()

    if dataSet == None:
        show_method = getattr(tkinter.messagebox, 'show{}'.format("warning"))
        show_method("Error", "Not enough numeric types in dataset.")       
        return

    X = dataSet.data
    y = dataSet.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = DecisionTreeClassifier(max_leaf_nodes=treeMaxLeafNodes, random_state=0)
    clf.fit(X_train, y_train)


    n_nodes = clf.tree_.node_count
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    feature = clf.tree_.feature
    threshold = clf.tree_.threshold

    node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, 0)]  # start with the root node id (0) and its depth (0)
    while len(stack) > 0:
        # `pop` ensures each node is only visited once
        node_id, depth = stack.pop()
        node_depth[node_id] = depth

        # If the left and right child of a node is not the same we have a split
        # node
        is_split_node = children_left[node_id] != children_right[node_id]
        # If a split node, append left and right children and depth to `stack`
        # so we can loop through them
        if is_split_node:
            stack.append((children_left[node_id], depth + 1))
            stack.append((children_right[node_id], depth + 1))
        else:
            is_leaves[node_id] = True

    tree.plot_tree(clf)
    plt.show()


