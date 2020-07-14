import i6


i = 1
i = '1'
try:
    i6.util.type_check(i, int)
except TypeError as e:
    print(e)
