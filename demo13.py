
import easygui as g
import sys
while True:
    g.msgbox("嘿♂，欢迎来到米奇♂妙妙屋")
    msg='do you like van♂游戏？'
    title='新日暮里'
    choices=['比利','木吉','van','魔男']
    choice=g.choicebox(msg,title,choices)
    answer=['奥义♂很爽','吼吼吼，全给党','deep♂dark♂fantasy','你也是个广♂东人，所以我们可能是老乡']
    if str(choice) == choices[0]:
        i=0
    elif str(choice) == choices[1]:
        i=1
    elif str(choice) == choices[2]:
        i=2
    elif str(choice) == choices[3]:
        i=3
    g.msgbox(str(choice)+':'+answer[i],'你的选♂择')
    msg_2="boy next door?"
    if g.ccbox(msg_2,title):
        pass
    else:
        sys.exit(1)
