# 1 oski stole your power:
def power(x,y):
    z=1
    p=x
    while z<y:
        p=p*x
        z=z+1 
    return print(p)

# 2 what should i wear?
readings = [15,14,17,20,23,28,20]
def temp_range(readings):
    x=min(readings)
    y=max(readings)
    return print((x,y))

# 3 check if its the weekend
def weekend_check(z):
    z=int
    if z==6 or z==7:
        return print("True")
    else:
        return print("False")

# 4 fuel efficiency calculator
def fuel_efficiency(distance, fuel):
    return print(distance/fuel)

# 5 secret code 
def decode_numbers(n):
    x=n%10
    y=n//10
    return print(x,y, sep="")

# 6 min & max but with loops!
# 6.1
nums=[2024,98,131,2,3,72]
def find_min_w_for_loop(x):
    min=x[0]
    for i in x:
        if i<min:
            min=i
    return print(min)

def find_max_w_for_loop(x):
    max=x[0]
    for i in x:
        if i>max:
            max=i
    return print(max)

# 6.2
nums=[2024,98,131,2,3,72]
def find_min_w_while_loop(x):
    min=x[0]
    i=1
    while i<len(x):
        if x[i]<min:
            min=x[i]
        i=i+1
    return print(min)

def find_max_w_while_loop(x):
    max=x[0]
    i=1
    while i<len(x):
        if x[i]>max:
            max=x[i]
        i=i+1
    return print(max)

# 7 counting vowels
text = 'UC Berkeley, founded in 1868!'
def vowel_and_consonant_count(str):
    x=0
    y=0
    for i in str:
        if i =='e' or i=='o' or i=='a' or i=='i' or i=='u' or i=='E' or i=='O' or i=='A' or i=='I' or i=='U':
            x=x+1
        elif i.isalpha()==True:
            y=y+1
        else:
            x=x
            y=y
    return print((x,y))

# 8 calculate digital root
num=2648
def digital_root(number):
    sum=0
    for i in str(number):
        sum=sum+int(i)
    return print(sum)


    