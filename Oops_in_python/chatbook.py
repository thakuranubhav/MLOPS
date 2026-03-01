class chatbook:
    __user_id =0
    def __init__(self):
        self.__name ='Anuraj k'
        self.id=chatbook.__user_id
        chatbook.__user_id +=1
        # __ is used to apply encapsulation
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.post = ''
        #self.menu() # function calling inside a constructor

    @staticmethod
    def get_id(self):
        return chatbook.__user_id
    

    @staticmethod
    def set_id(self,val):
        chatbook.__user_id = val

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value

    @staticmethod # decorator
    def college():
        print("This is the class of the decorator")



    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed 
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        if user_input == "1":
           self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input ==  "3":
            self.write_post()
        elif user_input == "4":
            self.message_friend()
        else:
            exit()
    
    def signup(self):
        email = input("Enter your email here ->")
        passw = input("Enter your password here ->")
        self.username=email
        self.password=passw
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
            self.menu()
        else:
            uname = input("Enter your email/username here ->")
            passw = input("Enter your password here ->")
            if self.username == uname and self.password ==passw:
                print("You have signed in sucessfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials..")

            print("\n")
            self.menu()
    def write_post(self):
        if self.loggedin == True:
            post = input("Enter your post here\n")
            self.post=post
            print("Following text has been posted successfully \n",post)
            print("\n")
            self.menu()


        else:
            print('Please logged in before to write a post\n')
            self.menu()

    def message_friend(self):
        if self.loggedin == True:
            name_of_friend =  input("Enter the name of your friend\n")
            msg = input("Write a message to your friend")

            print(f'message has been successfully sended to {name_of_friend}, message:{msg}')
            
        else:
            print("Please signedin to use the functionality of messaging\n")
        
        self.menu()



#obj=chatbook()

        
