from collections import OrderedDict
a = ["1", 1, "1", 2]
# print(list(set(a)))
# output = []
print(list(OrderedDict.fromkeys(a)))
# for i in a:
#     if i not in output:
#         output.append(i)
#
# print(output)