from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} = {value}")
        if key in self.keys():
            print("cle already exists")
            return
        super().__setitem__(key, value)

d = MyDict()
d[2] = 4
d[4] = 4
d[4] = 8

d.update({"3": "3", "R":"r"})

print(d)