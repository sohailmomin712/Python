# if and else should be ek ke niche ek 
# elif means else if 

# correct email - sohail@gmail.com
# password -1234

email = input("Enter the email")

if "@" in email:
    password = input ("Enter the password")

    if email == "sohail@gmail.com" and password == "1234":
        print("Welcome") 

    elif email == "sohail@gmail.com" and password != "1234":
        print("Incorrect Password")

        password = input ("Enter correct password")
        if password == "1234":
            print("Finally Correct")
        else:
         print("Still Incorrect")

    else:
        print("Try Again")

else:
    print("Email is incorrect. Enter a valid email")       



