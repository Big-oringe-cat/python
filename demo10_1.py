import pickle
my_list=['cat',123,['hahah']]
with open('/tmp/test.pkl','wb') as p:
    pickle.dump(my_list,p)
