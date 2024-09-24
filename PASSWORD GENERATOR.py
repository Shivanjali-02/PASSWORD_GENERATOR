#Password Generator Application using  python
import random,string
#function to generate a password
def password_generator():

    #Prompt the user to specify the desired length of the password  in length variable
    length=int(input("Password must be greater than zero (exculsive) Enter the length of the password :"))
    if length==0:
        print("invalid length  '/n' enter  positive integer as length ")
        password_generator()
    #Generates a random password with all the characters or literals
    else:
         gen_pass="".join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(length))
    return gen_pass   
     
   
#Generate and display the  password 
print("Generated Password :",password_generator())


