# Variables are dynamically typed 
n = 0 
print('n=' , n)

n = "hello ok"
print('n=',n)

#type is determined at the runtime 


#multiple assigments possible
n, m = 2, 30
first_n = n # save first value
 # protecting from overwriting
n,m,z= 20,"hy",90
print('n=', n,"m=",m,"z=",z)
print('first_n=', first_n)


#INCREMENT
n = n +1
n += 1
 #n++ # not valid 



#None Is Null value in python
n = 4 
n = None
print('n=',n)

#IF STATEMENTS
#OR CURLY BRACES we  use indentation
n = 30
if n > 3:
    print("monika cooks food at 12",n)


elif n > 3:
    print("monika eats burger no cooking",n)

#Parenthesis is needed for multiline conditions 
        # and  && or =
n,m = 1,2
if ((n > 6 and
     n!= m or n == m)):
    n +=9
    print("n=",n)
    



