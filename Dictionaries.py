import random,bisect,time
def find_number(phonebook,name):
    for n,p in phonebook:
        if n== name:
            return p

    return None

def gen_bisect_insort():
    num_book,dict_num=[],{}
    for i in range(10):
        j,k='key'+str(i),random.randint(-100,100)
        bisect.insort(num_book,(j,k))
    return num_book



if __name__ == '__main__':
    phonebook= [
        ('Jone','1232-444-555'),
        ('albert Einstein','6879-454-4545')
    ]
    num_book= gen_bisect_insort()
    p_dict= {'Jone':'1232-444-555','albert Einstein':'6879-454-4545'}
    #print("Phone number for Jone is {}".format(find_number(phonebook,'Jone')))
    #print("Phone number for albert Einstein is {}".format(p_dict['albert Einstein']))
    print(num_book)
    first=time.time()
    print("Value at {}, {:.4f}".format(find_number(num_book,'key9'),time.time()-first))
    last=time.time()
    #print("total time {}".format(last-first))
    #print("Value at {}, {:.4f}".format(num_book['key9'],time.time()-last ))

