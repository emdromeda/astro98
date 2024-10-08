# 2 practicing slicing & striding
# 2.1

mylist = range(0,21)
myactuallist = list(mylist)
print(list(mylist))

"""
I did not receive an error, but intitally I only got the output "range[0,12]"". I think is because I told the code to print the range, but I need to actually specify that I want to print out a list with the range
"""

# 2.2

def squaringlist(list):
    for i in list:
     list[i]= list[i]**2
    return list

mynewlist = squaringlist(myactuallist)
print(mynewlist)
    
"""
I intially forgot to add the colon after defining the list, and got an error that stated "invalid syntax." I also originally had my output for the function as "print(list)", but then kept getting "None" from the last print statement. I realized that this was because I was returning a string instead of a list, so mynewlist wasn't returning anything. I changed the function to return a list and now it is working.
"""

# 2.3

def first_fifteen_elements(list):
    list = list[0:15]
    return list
print(first_fifteen_elements(mynewlist))

# 2.4

def every_fifth_element(list):
   list = list[4::5]
   return list
print(every_fifth_element(mynewlist))

# 2.5 

def fancy_function(list):
   list = list[-30:]
   list = list[2::3]
   list = list[::-1]
   return list
print(fancy_function(mynewlist))

# 3.1

def create_2d_list():
   x=1
   y=6
   list = []
   for j in range(0,5):
      sublist = []
      for i in range(x,y):
        sublist.append(i)
        x=x+1
        y=y+1
      list.append(sublist)
   return list

matrix = create_2d_list()
print(matrix)

"""
I didn't run into errors while creating this function, but in the beginning I kept getting nothing as my output, which I realized was because I had written the print statemtn indexed when it shouldn't have been. After I fixed this, the function worked
"""

# 3.2

def modified_2d_list(list):
   for j in list:
        for i in range(len(j)):
            if j[i]%3==0:
                j[i]="?"
   return list
new_matrix=modified_2d_list(matrix)
print(new_matrix)
print(matrix)
"""
I ran into errors because I was using 'i' instead of j[i], so the code was just returning the same list because the list did not actually change. I fixed this by using indexing to tell it which actual element to change, which gave me the right answer.
"""

# 3.3

def sum_non_question_elements(list):
    x=0
    for j in list:
         for i in range(len(j)):
             if j[i]!="?":
                x=x+j[i]
    return print(x)

sum_non_question_elements(new_matrix)

"""
I ran into an error becayse I orignally printed modified_2d_list(matrix) directly instead of assigning the variable first, which changed "matrix" so that function was not working. I fixed this by assigning the variable first in order for python to understand that I still want to use my original "matrix" function.
"""



