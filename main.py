#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ระบบทำนายช่องโหว่ในซอร์สโค้ด (Vulnerability Prediction in Source Code)
Main entry point

พัฒนาโดย: AI Assistant
เวอร์ชัน: 1.0
"""

import sys
import os

def check_dependencies():
    """ตรวจสอบ dependencies ที่จำเป็น"""
    required_packages = [
        'numpy',
        'scikit-learn', 
        'pandas',
        'matplotlib',
        'seaborn',
        'joblib'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ พบ packages ที่ขาดหายไป:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\nกรุณาติดตั้ง packages ที่ขาดหายไปด้วยคำสั่ง:")
        print("python -m pip install -r requirements.txt")
        print("หรือติดตั้งทีละตัว:")
        print("python -m pip install scikit-learn")
        print("python -m pip install numpy pandas matplotlib seaborn joblib")
        return False
    
    print("✅ Dependencies ทั้งหมดพร้อมใช้งาน")
    return True

def check_tkinter():
    """ตรวจสอบการติดตั้ง tkinter"""
    try:
        import tkinter
        print("✅ tkinter พร้อมใช้งาน")
        return True
    except ImportError:
        print("❌ ไม่พบ tkinter")
        print("กรุณาติดตั้ง tkinter หรือใช้ Python ที่มี tkinter รวมอยู่")
        return False

def main():
    """ฟังก์ชันหลัก"""
    print("=" * 60)
    print("ระบบทำนายช่องโหว่ในซอร์สโค้ด")
    print("Vulnerability Prediction in Source Code")
    print("=" * 60)
    
    # ตรวจสอบ dependencies
    print("\n🔍 กำลังตรวจสอบ dependencies...")
    if not check_dependencies():
        sys.exit(1)
    
    # ตรวจสอบ tkinter
    print("\n🔍 กำลังตรวจสอบ tkinter...")
    if not check_tkinter():
        sys.exit(1)
    
    print("\n🚀 กำลังเริ่มระบบ...")
    
    try:
        # Import และรัน GUI
        from vulnerability_gui import main as run_gui
        run_gui()
    except ImportError as e:
        print(f"❌ ไม่สามารถ import modules ได้: {e}")
        print("กรุณาตรวจสอบว่าไฟล์ทั้งหมดอยู่ในโฟลเดอร์เดียวกัน")
        sys.exit(1)
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
