# ตัวอย่างโค้ดที่ปลอดภัยด้านความปลอดภัย
# ไฟล์นี้ใช้สำหรับทดสอบระบบทำนายช่องโหว่

import re
import hashlib
import secrets
from typing import Optional
import os

def safe_function_1():
    """ฟังก์ชันที่ปลอดภัย - ตรวจสอบข้อมูลก่อนประมวลผล"""
    user_input = input("Enter a number: ")
    
    # ตรวจสอบว่าข้อมูลเป็นตัวเลขหรือไม่
    if user_input.isdigit():
        number = int(user_input)
        result = number * 2
        return result
    else:
        return "Invalid input: Please enter a number"

def safe_function_2():
    """ฟังก์ชันที่ปลอดภัย - ใช้ parameterized query"""
    user_id = input("Enter user ID: ")
    
    # ตรวจสอบว่าข้อมูลเป็นตัวเลขหรือไม่
    if not user_id.isdigit():
        return "Invalid user ID"
    
    # ใช้ parameterized query (ตัวอย่าง)
    query = "SELECT * FROM users WHERE id = ?"
    params = [user_id]
    
    return f"Query: {query}, Params: {params}"

def safe_function_3():
    """ฟังก์ชันที่ปลอดภัย - ตรวจสอบ path ก่อนเปิดไฟล์"""
    filename = input("Enter filename: ")
    
    # ตรวจสอบว่า filename ไม่มี path traversal
    if '..' in filename or '/' in filename or '\\' in filename:
        return "Invalid filename: Path traversal not allowed"
    
    # ตรวจสอบว่าไฟล์อยู่ในโฟลเดอร์ที่อนุญาต
    allowed_directory = "./data"
    full_path = f"{allowed_directory}/{filename}"
    
    try:
        with open(full_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error reading file: {e}"

def safe_function_4():
    """ฟังก์ชันที่ปลอดภัย - ใช้ hashlib แทน pickle"""
    user_data = input("Enter data to hash: ")
    
    # สร้าง hash แทนการ serialize
    hash_object = hashlib.sha256(user_data.encode())
    hash_value = hash_object.hexdigest()
    
    return f"Hash of '{user_data}': {hash_value}"

def safe_function_5():
    """ฟังก์ชันที่ปลอดภัย - ตรวจสอบ URL ก่อนเปิด"""
    url = input("Enter URL: ")
    
    # ตรวจสอบว่า URL ปลอดภัย
    if not url.startswith(('http://', 'https://')):
        return "Invalid URL: Must start with http:// or https://"
    
    # ตรวจสอบว่าไม่ใช่ localhost
    if 'localhost' in url or '127.0.0.1' in url:
        return "Invalid URL: Localhost not allowed"
    
    return f"URL '{url}' is safe"

def safe_function_6():
    """ฟังก์ชันที่ปลอดภัย - ไม่แสดงข้อมูลที่สำคัญ"""
    password = input("Enter password: ")
    
    # ไม่แสดงรหัสผ่าน
    if len(password) >= 8:
        return "Password is strong"
    else:
        return "Password is too short"

def safe_function_7():
    """ฟังก์ชันที่ปลอดภัย - ตรวจสอบ directory ก่อนเข้าถึง"""
    directory = input("Enter directory: ")
    
    # ตรวจสอบว่า directory ไม่มี path traversal
    if '..' in directory or '/' in directory or '\\' in directory:
        return "Invalid directory: Path traversal not allowed"
    
    # ตรวจสอบว่า directory อยู่ในโฟลเดอร์ที่อนุญาต
    allowed_base = "./data"
    full_path = f"{allowed_base}/{directory}"
    
    try:
        files = os.listdir(full_path)
        return f"Files in {directory}: {files}"
    except FileNotFoundError:
        return "Directory not found"
    except Exception as e:
        return f"Error accessing directory: {e}"

def safe_function_8():
    """ฟังก์ชันที่ปลอดภัย - ใช้ subprocess อย่างปลอดภัย"""
    command = input("Enter command: ")
    
    # ตรวจสอบว่า command ปลอดภัย
    allowed_commands = ['ls', 'dir', 'echo', 'date']
    if command not in allowed_commands:
        return f"Command '{command}' not allowed"
    
    try:
        # ใช้ subprocess.run แทน subprocess.call
        import subprocess
        result = subprocess.run([command], capture_output=True, text=True, shell=False)
        return f"Output: {result.stdout}"
    except Exception as e:
        return f"Error executing command: {e}"

def safe_function_9():
    """ฟังก์ชันที่ปลอดภัย - ตรวจสอบข้อมูลก่อนประมวลผล"""
    user_code = input("Enter a simple expression: ")
    
    # ตรวจสอบว่าเป็น expression ที่ปลอดภัย
    allowed_chars = set('0123456789+-*/(). ')
    if not all(c in allowed_chars for c in user_code):
        return "Invalid expression: Contains disallowed characters"
    
    try:
        # ใช้ eval() เฉพาะกับ expression ที่ปลอดภัย
        result = eval(user_code)
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

def safe_function_10():
    """ฟังก์ชันที่ปลอดภัย - สร้าง token ที่ปลอดภัย"""
    # สร้าง token แบบสุ่ม
    token = secrets.token_urlsafe(32)
    return f"Generated secure token: {token}"

def validate_email(email: str) -> bool:
    """ตรวจสอบความถูกต้องของ email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password: str) -> bool:
    """ตรวจสอบความแข็งแกร่งของรหัสผ่าน"""
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    return True

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    print("✅ ไฟล์นี้เป็นโค้ดที่ปลอดภัยด้านความปลอดภัย")
    print("ใช้สำหรับทดสอบระบบทำนายช่องโหว่")
    
    # ทดสอบฟังก์ชันที่ปลอดภัย
    try:
        print("\n=== ทดสอบฟังก์ชันที่ปลอดภัย ===")
        print(safe_function_1())
        print(safe_function_2())
        print(safe_function_3())
        print(safe_function_4())
        print(safe_function_5())
        print(safe_function_6())
        print(safe_function_7())
        print(safe_function_8())
        print(safe_function_9())
        print(safe_function_10())
        
        print("\n=== ทดสอบการตรวจสอบข้อมูล ===")
        email = "test@example.com"
        print(f"Email '{email}' is valid: {validate_email(email)}")
        
        password = "SecurePass123"
        print(f"Password '{password}' is strong: {validate_password(password)}")
        
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
