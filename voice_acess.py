import pyttsx3
username = "Krish Raj"
passcode = "#Error_code21"
# This program allows a user to log in with a user ID and password, and then access information based on keys.
# If the login is successful, the user can search for keys in a predefined dictionary.
print("Welcome to the voice access program!")
say = pyttsx3.init()
say.say("Welcome to the voice access program!")
say.runAndWait()

chance = 3
while chance != 0:
    userID = input("Enter your user ID: ")
    password = input("Enter your password: ")
    if userID == username and password == passcode:
        print("Login successful!")
        say = pyttsx3.init()
        say.say("Login successful!")
        say.runAndWait()
        info ={
            "name": "krish raj",
            "age": 19,
            "gender": "male",
            "city": "Purnea",
            "email": "krishrajkcc@gmail.com"
        }
        while True:
            print("Available keys: ", list(info.keys()))
            print("Type 'exit' to quit.")
            choice = input("Enter the key you want to search: ")
            if choice == "exit":
                print("Exiting the program.")
                say.say("Exiting the program.")
                say.runAndWait()
                chance = 0
                break
            elif choice in info:
                print(info[choice])
            else:
                print("Key not found.")
                say = pyttsx3.init()
                say.say("Key not found.")
                say.runAndWait()
                
    else:
    
        print("Invalid user ID or password.\n Please try again.")
        chance -= 1
        print(f"You have {chance} chances left.")
        
        say = pyttsx3.init()
        say.say("Invalid user ID or password. Please try again.")
        say.runAndWait()
        if chance == 0:
            print("You have exhausted all your chances. Exiting the program.")
            say = pyttsx3.init()
            say.say("You have exhausted all your chances. Exiting the program.")
            say.runAndWait()
            break


    