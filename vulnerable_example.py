# ตัวอย่างโค้ดที่มีช่องโหว่ด้านความปลอดภัย
# ไฟล์นี้ใช้สำหรับทดสอบระบบทำนายช่องโหว่

import os
import subprocess
import pickle
import sqlite3

def vulnerable_function_1():
    
    user_input = input("Enter code to execute: ")
    result = eval(user_input)  
    return result

def vulnerable_function_2():
    
    user_id = input("Enter user ID: ")
    query = f"SELECT * FROM users WHERE id = {user_id}"  
    return query

def vulnerable_function_3():
    
    user_command = input("Enter command: ")
    os.system(user_command)  

def vulnerable_function_4():
    
    filename = input("Enter filename: ")
    with open(filename, 'r') as f:  
        content = f.read()
    return content

def vulnerable_function_5():
    
    user_data = input("Enter serialized data: ")
    obj = pickle.loads(user_data)  
    return obj

def vulnerable_function_6():
    
    url = input("Enter URL: ")
    import urllib.request
    response = urllib.request.urlopen(url)  
    return response.read()

def vulnerable_function_7():
    
    password = input("Enter password: ")
    print(f"Password received: {password}")  
    return password

def vulnerable_function_8():
    
    directory = input("Enter directory: ")
    files = os.listdir(directory)  
    return files

def vulnerable_function_9():
    
    command = input("Enter command: ")
    result = subprocess.call(command, shell=True)  
    return result

def vulnerable_function_10():
    
    code = input("Enter Python code: ")
    exec(code)  

