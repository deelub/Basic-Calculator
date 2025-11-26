
def on_load():
    """_summary_
    """
    
    global user_ans
      
    calculation_opts=["Addition","Subtraction","Division","Multiplication"]
    print("Welcome to THEE calculator ,please select the number of what type of calculation you would like to do?")
    
    count=0
    for i in calculation_opts:
        count += 1
        print (f"{count}.{i}")
    
          
    while True:
        try:
            user_ans= int(input("Enter a number  ") ) #error handling should be if it's greater than the range raise invalid option
            if 1 <= user_ans <= 4 : 
               return calculations(user_ans)
            else:       
                print("Invalid number entered, please select a number on the list")      
                new_ans=int(input("Enter a number  ") ) #add in condtitional checker that checks if it is  adigit or not
        except ValueError:              #problem solve for changing the value after multiple wrong entries
                new_ans=int(input("Enter a number  ") )     
                return "Invalid charcater, please input a number",new_ans
                
def calculations(user_ans):
    num1= float(input("Enter the first number"))
    num2= float(input("Enter the second number")) #cannot restict this to two numn=bers only they can enter as many numbers
    
    #doing basic calculations seek to doing more complex calculations like an actual calculator
    if user_ans==1:
        return num1 + num2
    elif user_ans==2:
        return num1-num2
    elif user_ans==3:
        if num2==0:
            num2=float(input("Cannot divide by zero, enter a different number"))     #see if this is viable and we can add it to the above case
            raise ZeroDivisionError(num2)
        else:
            return num1/num2
    elif user_ans==4:
        return num1*num2
        
    
 


print(on_load())