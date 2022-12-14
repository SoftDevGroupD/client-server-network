import socket
from pathlib import Path
import pickle
import json
from dict2xml import dict2xml
from cryptography.fernet import Fernet
from functions import creat_dictionary,serialize,dump_json,dict_2_xml,send_text_to_server,send_file_to_server,creat_file,send_to_server,decrypt_file,load_key
import os


if __name__ == '__main__':

    host = socket.gethostname()  # as both code is running on same pc
    port = 5050  # socket server port number
    #Staring a TCP socket
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    # connecting to the server
    socket_client.connect((host, port))  # connect to the server
    format = "utf-8"
    #creat_file()

    #creat_dictionary()
    #Serialize_the_dictionary()
    #creat_dictionary()


    # TASK NUMBER ONE
    # the task is to input a message from the client and send to the server
    # and the server should have an option to choose from print and to creat a file
    message = input("task 1: please input the content you want to send to ther server>>> ")
    socket_client.send(message.encode(format))

    # TASK NUMBER TWO
    # the task is to creat a text file from the client and send to the server
    message = input("task 2: creat a text file from the client and send to the server, input the file name you want:>>> ")
    creat_file_name = message
    creat_file(creat_file_name)
    send_to_server(creat_file_name,socket_client,format)


    # TASK NUMBER THREE
    #Create a dictionary, populate it, serialize it and send it to a server,
    #With the dictionary, the user should be able to set the pickling format 
    #to one of the following: binary, JSON and XML.    
    
    dic = {'TeamD': 'SoftwareDevelopment'}
    print(f'This dictionary is for demonstration purposes: {dic} ')
    config = input("Task 3 Please input the method of serialization and deserialization for the dictionary: binary, json, xml    ")
    # creat a new dictionary
    
    #MADE I CORRECTION LUIS
        
    response = input("Transform it in JSON XML or Binary")
    if response == "json":
       class example_class:
         data = {
            "user":{"name":"TeamD",
                  "Subject":"SoftwareDevelopment"
            }
         }

       my_object = example_class()

       my_pickled_object = pickle.dumps(my_object)  # Pickling the object
       print(f"This is my pickled object:\n{my_pickled_object}\n")
       my_object.a_dict = None

       my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
       print(
         f"This is a_dict of the unpickled object:\n{my_unpickled_object.data}\n")
      
    if response == "binary":
        file_to_write = open("dictionary.pickle", "wb")
        pickle.dump(dic,file_to_write)
        print(f'This is my pickled object : {file_to_write}')
        file_to_write.close()
        
        file_to_read= open("dictionary.pickle","rb")
        dictionary_2 = pickle.load(file_to_read)
        print(f'This is a_dict of the unpickled object for binary : {dictionary_2}')
     
     # MADE CORRECTION LUIS
     
    question = input("Are you Encrypting or Decrypting?: Type 1 for Encrypting and 2 for Decrypting ")
    file_path = input('Enter the file path for the file decrypting: ')
    
    print(file_path)
    
    if os.path.exists(file_path):
      print('The file exists')

      with open(file_path, 'r', encoding='utf-8-sig') as file_encrypt:
        lines = file_encrypt.readlines()
        print(lines)
        
    else:
      print('The specified file does NOT exist')

    if question == '1' and os.path.exists(file_path):
      def generate_key():
        # key generation
        key = Fernet.generate_key()
        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
      generate_key()

      def encrypt_file(): 
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
      encrypt_file()
 
