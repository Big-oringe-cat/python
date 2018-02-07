class Turtle:
    color = 'green'
    legs = 4
    weight = 10
    shell = True
    mount = '大嘴'
    def __init__(self,name):
        self.__name=name
    def getName(self):
        print('本大爷是{0}'.format(self.__name))
    def run(self):
        print("其实跑得比兔子快")
    def climb(self):
        print("慢慢爬，慢慢摸鱼")
    def bite(self):
        print("乌龟人永不为奴！！！")
    def sleep(self):
        print("朕累了，睡了")
t1=Turtle('leo')
t1.getName()
print(t1._Turtle__name)
t1.run()
t1.climb()
t1.bite()
t1.sleep()
