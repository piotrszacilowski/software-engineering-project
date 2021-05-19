
fileselection = ""
meta = None

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