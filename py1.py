#problem 1
class n_Set:
    def __init__(self, x):
        self.x = set(x)

    def insert(self, new_x):
        self.x |= set(new_x)

    def check(self, e):
        if e in self.x:
            print("is_member")
        else:
            print("not_a_member")

    def remove(self, e):
        try:
            self.x.remove(e)
        except:
            raise ValueError("Member is not in set")

    def get(self):
        return list(self.x)
    
    def desc_order(self):
        result = []
        while self.x:
            max_= max(self.x)
            self.x.remove(max_)
            result.append(max_)
        self.x = set(result)
        return result
a= n_Set([])
a.insert([1, 2, 3, 4, 5])
print(a.get())
a.check(2)
a.remove(2)
print(a.get())
print(a.desc_order())

