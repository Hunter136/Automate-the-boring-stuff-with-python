import collections
class dicti(collections.UserDict):
    def __init__(self, dicti = None ):
        self.dicti = {}
        #self.items = {items}
    def __instancecheck__(self, instance):
        instance = isinstance(dicti(), dicti)
        if instance:
            print("This is indeed a dictionary")
        else:
            print("THis is bad")
    def add(self,):
        inp = str(input("type in a user key than value"))
        inpu = input()
        self.dicti[inp] = inpu
    def defdictaddstrkey(self):
        inp = input("give us a new key of the def dict style")
        dic = collections.defaultdict(str)
        dic[inp]
        self.dicti.update(dic)
        return self.dicti
    def defdictaddintkey(self):
        inp = input("give us a new key def dict style")
        dic = collections.defaultdict(int)
        dic[inp]
        self.dicti.update(dic)
        return self.dicti
    def subtract(self):
        inp = str(input("type in a user key to delete"))
        del[self.dicti[inp]]
        #word = self.dicti.pop(inp)
        print("The key "+inp+" was removed")
    def getvalue(self, key):
        word = self.dicti[key].value
        print('key: '+ key + 'value: ' + word)
    def keys(self):
        return self.dicti.keys()
    def values(self):
        return self.dicti.values()
    def items(self):
        return self.dicti.items()
    def getkey(self, value):
        for k,v in self.dicti.items():
            if v == value:
                print('key: ' + k + 'value: ' + v)
    def __repr__(self):
       return str(self.dicti.items())
    def printfancy(self):
        for k,v in self.dicti.items():
            print('Keys: '+ k + '\n' +  'Value: ' + v)
    def update(self,other):
        copy = other.copy()
        self.dicti.update(copy)
        return self.dicti
    def counter(self): #counts number of different keys in dicti
        dic = collections.Counter(self.dicti)
        return dic
    def __missing__(self, key):
        dic = collections.defaultdict(str)
        dic[key]
        return dic
def main():
    dicti1 = dicti()
    dicti1.__instancecheck__(dict)
    command = input('tell us what you want to do add, subtract, fields, default dicti???')
    while command != 'no':
        if command == 'add':
            dicti1.add()
        elif command == 'subtract':
            dicti1.subtract()
        elif command == 'defaultdict':
            inputt = input("int or str???")
            if inputt == 'str':
                dicti1 = dicti1.defdictaddstrkey()
            else:
                dicti1 = dicti1.defdictaddintkey()
        #print(inspect.getmembers(dicti1)) prints out objects attributes
        print(dicti1)
        command = input('tell us what you want to do add, subtract, fields, default dicti???')
        print(globals())
if __name__ == "__main__":
    main()