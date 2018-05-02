import bisect
import random

def find_closest(haystick,needle):
    i = bisect.bisect_left(haystick,needle)
    if i ==len(haystick):
        return i-1
    elif haystick[i]==needle:
        return i
    elif i>0:
        j=i-1
        if haystick[i]-needle>needle-haystick[j]:
            return j
    return i


if __name__=="__main__":
    important_numbers=[]
    for i in range(30):
        new_number=random.randint(-1000,1000)
        bisect.insort(important_numbers,new_number)
    print(important_numbers)
    closest_num=find_closest(important_numbers,-250)
    print("The closest number to -250 is {} and index is ".format(important_numbers[closest_num], closest_num))
    closest_num = find_closest(important_numbers, 50)
    print("The closest number to 50 is {}".format(important_numbers[closest_num],closest_num))


