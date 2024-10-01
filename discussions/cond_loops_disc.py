### This is the syntax of a for-loop ###

#for variable in range(start, stop, step):
    # Code block to be executed

### This is the syntax of a while-loop ###

#while condition == true:
    # Code block to be executed


# Note: It is normal to forget the syntax! That is why google is your bff and you just need to google "for loop syntax" or "while loop syntax"
# and there are tons of resources. I usually just go to images to quickly check the syntax.


'''### Problem 1: Your turn!

Print i 10 times using both a for and while loop.'''

for x in range(0,10):
    print("i")

x=0
while x<10:
    print("i")
    x=x+1

'''###Problem 2: Range()
Range is a cool function but there are a lot of parts to it so let's disect it!

What happens if the range is from (5, 5)?  How about from (10, 6)?  
Try different step sizes: (10, 6, -1), (1, 10, 2). Write down all your observations and answer the following questions.'''

for x in range(5,5):
    print("a")

# observations: no 'a' is printed :(

for x in range(10, 6):
    print("b")

# observations: no 'b' is printed

for x in range(10, 6, -1):
    print("c")

# observations: 4 'c's are printed

for x in range(1, 10, 2):
    print("d")

# observations: 5 'd's are printed

'''### Problem 3: Listness
How do you loop through elements in a list using a for loop? '''

# write: "for i in list_name:", where i is the index (or you can use a diff variable)

l=['b','e','r','k','e','l','e','y']

for i in l:
    print(i)
