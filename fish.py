import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x -=1
        print('now.the position is ({0},{1})'.format(self.x,self.y))

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("我饿了！！！")
            self.hungry=False
        else:
            print("不行了，吃撑了")
