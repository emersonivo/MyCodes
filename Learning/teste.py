# print("Hey %s there. How are %s %s" % ("you", "you", "doing"))
# print(round(1.49))

# from contextlib import contextmanager
#
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
#
# with tag("h1"):
#     print("foo")

# import fileinput
# import inspect
# with fileinput.input(files=('bola.txt', 'caco.txt')) as f:
#     for line in f:
#         print(line)
#
#     print(inspect.getdoc(f))

# 5.1.4. Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
r = matrix[1]
c = r[3]
print(c)
print(matrix[1,[3]])
