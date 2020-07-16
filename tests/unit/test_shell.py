import i6


def test_diff():
    diff = i6.shell.diff('file1.txt', 'file2.txt')
    print(diff)
