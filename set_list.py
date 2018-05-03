def list_unique_names(phonebook):
    unique_name = []
    for name, phonenum in phonebook:
        firstname, lastname = name.split(" ", 1)
        for unique in unique_name:
            if unique == firstname:
                break
            else:
                unique_name.append(firstname)
    return len(unique_name)


def set_unique_names(phonebook):
    unique_name = set()
    for name, phonenum in phonebook:
        firstname, lastname = name.split(" ", 1)
        unique_name.add(firstname)
    return len(unique_name)

class City(str):
    def __hash__(self):
        return ord(self[0])

class Point(object):
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __hash__(self):
        return hash((self.x,self.y))
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y


if __name__ == '__main__':
    phonebook = [
        ("John Doe", "5555-555-555"),
        ("Albert E", "32334-234234-234234"),
        ("Albert R", "32434-43435-324453")
    ]
    print('number of unique names {}'.format(set_unique_names(phonebook)))
    print('number of unique names {}'.format(list_unique_names(phonebook)))
    data={
        City('Rome'):4,
        City('San.Fr'):5,
        City('New York'):6,
        City('Barcelona'):8
    }
    print(data)
    p1=Point(1,1)
    p3=Point(3,3)
    print(set([p1,p3]))
    if Point(1,1) in set([p1,p3]):
        print("True")
    else:
        print("False")
