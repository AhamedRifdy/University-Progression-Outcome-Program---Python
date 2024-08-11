#------------Author --> Mohomed Ahamed------------#
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1987489 / 20223243
# Date: 21/04/2023

#-----------function to check the validity----------------------------
def input_check(message):
    """
        Getting the input & validating
    """
    while True:
        try:
            marks = int(input(message))
        except ValueError:
            print("Integer required")
            continue
        if marks not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range")
            continue
        break
    return marks


#-----------function to check whether to continue or quit --------------
def option_message():
    """
        display a prompt to  continue or quit
    """
    
    while True:
        print("\n") #print a newline
        option = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        
        print("\n") #print a newline
        if option.lower() in ['q', 'y']:
            return option.lower()
        else:
            print("\tPlease enter the correct option !")
    

#-----------function to print the histogram----------------------------                  
def histogram():
        print("------------------------------------------------------------------------------")
        print("Histogram")
        print("Progress", progress, " :", "*"*progress )
        print("Trailer", trailer, "  :", "*"*trailer )
        print("Retriever", retriever, ":", "*"*retriever )
        print("Excluded", excluded, " :", "*"*excluded )
        print("")
        print(student_count, "outcomes in total")
        print("------------------------------------------------------------------------------")


# -----Variable initialization-------- 
progress = 0
trailer = 0
excluded = 0
retriever = 0
student_count = 0
option = 'y'

# ------Student Details Dictionary--------
student_details = {}


while option == 'y':
    #asking for the student id 
    student_id = input("Enter your student ID: ")
    if len(student_id) != 8:
        print("Enter a valid ID")
        continue
    if student_id in student_details:
        print("The student id is already exists. Please try again!")
        print("\n")
        continue
    
    #getting the credits through the input_check function    
    pass_credit = input_check("Please enter your credits at pass: ")
    defer_credit = input_check("Please enter your credits at defer: ")
    fail_credit = input_check("Please enter your credits at fail: ")

    credit_details = [pass_credit, defer_credit, fail_credit] #adding the credits into the list
        
    #calculate the total
    if pass_credit + defer_credit + fail_credit != 120:
        print("Total incorrect")
        option = option_message()
        if option == 'q':
            histogram()
            break
                
    else:
        student_count += 1
                
        #checking the credits and assigning the progression outcome
                
        if pass_credit == 120:
            outcome = "Progress"
            progress += 1
        elif pass_credit == 100:
            outcome = "Progress(module trailer)"
            trailer += 1
        elif fail_credit >= 80:
            outcome = "Exclude"
            excluded += 1
        else: 
            outcome = "Do not Progress - module retriever"
            retriever += 1
        print(outcome)

        credit_details.append(outcome)
        student_details[student_id] = credit_details
        

        option = option_message()


        if option == 'q':
            #prints the details through the dictionary
            #reffered to https://www.w3schools.com/python/python_dictionaries.asp
            for key , value in student_details.items():
                    data = str(value[0:3]) 
                    data = data.replace("[","")
                    data = data.replace("]","")
                    print(key ,":",value[-1],"-", data)
            break

        
    

        
                
    
      
        
            
    
     
                    
       



    


