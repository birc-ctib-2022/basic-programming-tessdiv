
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).
n= input("Do you want to stop? ") #asks the initial question
while n!='yes': #if n is not equal to yes, it will ask the question again 
   n= input("Do you want to stop? ")
while n =='yes': #if n is yes, it will stop
    break
 
#ALSO WORKS
#n= input("Do you want to stop? ") #asks the initial question
#answer= input("Do you want to stop?")
#while answer != "yes":
#   answer= input("Do you want to stop?")

#ALSO WORKS 
#while input("Do you want to stop?") != "yes":
#    pass 