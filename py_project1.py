##### the collatz conjecture#####
## the unsloved problem 


#Try is used so that if something goes wrong, do not crash automatically(((it is kinda safty net)))


try:
    choice = "yes"
    while choice =="yes":
     number = int(input("enter any number"))
    #  above line is for taking input from a user
     if number <= 0 :
          print("enter  a positive number, other then one  ")
          #above line is a condition that if  the given number is less than equal
          #then, the give line will print 
          #  enter a numm.....
     elif number <= 1:
        print("enter other except 1") # if the user enters 1 then the given statment will print
     else:
          while number != 1:
              if number %2 == 0:
                  number = number //2 #to find the floor division
#above and below line are for the collatz  conjection         
                  
                  # tis is the formula by which we use to find whether the number is odd or even
              else:
                  number = 3* number +1 # it will multiply the number by 3 and add the multiplied number by 1
              print(number)
except ValueError: # to avoid the value error 
    #  choice = input("Do you want to continue? (yes/no): ")
     print("u have entered wrong value") #if the given number is wrong then it will print the above statement
     
    
    
    
    

        