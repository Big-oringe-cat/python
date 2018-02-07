import pickle
with open('/tmp/test.pkl','rb') as p:
    my_list=pickle.load(p)
    print(my_list)
