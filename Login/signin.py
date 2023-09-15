from main import users


# CHECKING FOR USER
def hasUser(username):
    exists  = False
    index =""
    for user in users :
        if user["username"] == username:
            exists = True
            index = users.index(user)
            
            break
    return exists,index
   

# AUTHENTICATING PASSWORD
def password_auth(username,password,index):
    valid= False
    if users[index]["password"] == password:
        valid=True

    return valid



# LOGIN FUNCTION
def login(username,password):
   exists , index = hasUser(username)
   if not exists:
       print("User does not exist")
   else:
       valid = password_auth(username, password,index)

       if not valid:
           print("Something went wrong please try again later")
       else:
           print(f"Welcome {username}")


login("katty","loveod")