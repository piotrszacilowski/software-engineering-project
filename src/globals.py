
fileselection = ""
meta = None

# 0 - iris, 1 - digits, 2 - wine, 3 - breast_cancer
treeDataset = None 

def initialize(): 
    global fileselection
    
def get_selection():
    return fileselection
def set_selection(val):
    global fileselection
    fileselection = val

def get_metadata():
    return meta
def set_metadata(metadata):
    global meta
    meta = metadata

def set_tree_dataset(id):
    global treeDataset
    treeDataset = id
def get_tree_dataset():
    return treeDataset