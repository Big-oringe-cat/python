class Turtle:
    def __init__(self,x):
        self.num=x

class Fish:
    def __init__(self,x):
        self.num=x

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def showNum(self):
        print("水池里有{0}只王八 ，{1}只鱼".format(self.turtle.num,self.fish.num))

p1=Pool(2,8)
p1.showNum()
