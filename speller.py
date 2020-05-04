words = set()
def check(word):
    if word.lower() in words:
        return True
    else:
        return False
def load(dictionary):
    file = open(dictionary,"r")
    for line in file:
        # rstrip will strip the newline character from the reverse order for each word in dictionary file 
        words.add(line.rstrip("\n"))  
    file.close()
    return True
def size():
    return len(words)
def unload():
    return True
    