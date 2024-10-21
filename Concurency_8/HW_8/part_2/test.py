
def test():
    with open('file_1.txt', 'r') as f:
        content = f.read()
    assert content == "This is file number 1"
