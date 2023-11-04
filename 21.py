d = {"a": 1, "b": 2, "c": 3}

d = {key:  value for key,value in d.items() if value < 2}
print(d)