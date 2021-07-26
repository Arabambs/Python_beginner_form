#Q10 Write a Python program to build a sign_Up and login forms for users. Your program should validate/authenticate entered credentials for existing users or create new accounts for new users
#1 Create "Credentials.txt" file
#2 Add the following information into your Credentials.txt file <Name, Password>
    # Sarah,12ssr
    # Lisa,pass
    # Donna,D00N
#3 Create login function that takes two inputs (name,password)
    #3.1 Ask the user to enter their username and password
    #3.2 search if the names exist in the Credentials.txt file
        #3.2.1 if the name was found, check if the password is correct
        #3.2.2 return "Welcome <persons name> if the name and password were correct"
        #3.2.3 else return "wrong name or password"
    #3.2 if the name doesn't exist return "your name doesn't exist, please create a new account"
#4 Create sign_Up function that takes two inputs(newName,newPassword)
    #Ask user to enter their name and password
    #append the new information into the Credentials.txt file, follow the same format "name,password"
#5 Test your program by logging in using the new account


########################   SOLUTION   #####################


text_list = ["Sarah,12ssr","Lisa,pass","Donna,D00N"]

#1 Create "Credentials.txt" file
my_file = open("Credentials.txt", "w")

#2 Add the following information into your Credentials.txt file <Name, Password>
    # Sarah,12ssr
    # Lisa,pass
    # Donna,D00N
for line in text_list:
  # write line to output file
    my_file.write(line)
    my_file.write("\n")
my_file.close()
# QUESTION 3 , 4 AND 5
authorized = False
def authorize():
#     calling the global variable authorized
    global authorized
    authorized = True

def login_function(name,password):
    success = False
    file = open("Credentials.txt", "r")
    for i in file:
#       var = "a,b" .var.split(",")  gives(["a", "b"]).
#       applying that idea         
        user_input1,user_input2 = i.split(",")
        user_input2 = user_input2.strip()
        if(user_input1==name and user_input2==password):
            success = True
            break      
    file.close()
    if(success):
        print("Login successful ")
        authorize()
    else:
        print("wrong username or password")

def Signup_function(name,password):
#     using the with statement you do not need to close the file it does that automaticaly
    with open("Credentials.txt", "a") as file:
         file.write(name+","+password+"\n")
    print("Signup successful ")
    authorize()


def access_begin_form(option):
    global name
    #using an if else statement to check if the name is 
    #in login option or else willbe registered
    if(option=="Login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
         #calling login function to accept name and password
        login_function(name,password)
    else:
        name = input("Enter your Newname:")
        password = input("Enter your Newpassword:")
        #calling register function to accept name and password
        Signup_function(name,password)
        

def begin_Form():
    global option
#   print("This is a function that collects to inputs from the user\"Name & Password\")
    option = input("Start by Inputing(Login or Signup):")  
    #making input first letter capitalized using the capitalize method
    option = option.capitalize()
    if(option!="Login" and option!="Signup"):
        begin_Form()
          
begin_Form()
# print(option)
access_begin_form(option)
if(authorized):
    print("Welcome to your new form ",name )
    print("Form creation still in progress")
    