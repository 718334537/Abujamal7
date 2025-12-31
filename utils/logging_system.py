#!/usr/bin/env python3
# Encrypted Logging System

import json
import base64
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

class SecureLogger:
    def __init__(self, log_file='logs/encrypted.log'):
        self.log_file = log_file
        self.key = hashlib.sha256(
            datetime.now().strftime("%Y%m%d%H").encode()
        ).digest()
        
    def encrypt(self, message):
        """تشفير الرسالة"""
        cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(
            message.encode() if isinstance(message, str) else message
        )
        
        return {
            'timestamp': datetime.now().isoformat(),
            'nonce': base64.b64encode(cipher.nonce).decode(),
            'tag': base64.b64encode(tag).decode(),
            'data': base64.b64encode(ciphertext).decode()
        }
        
    def log(self, level, module, message):
        """تسجيل مدخل جديد"""
        entry = {
            'level': level,
            'module': module,
            'message': message,
            'pid': os.getpid()
        }
        
        encrypted = self.encrypt(json.dumps(entry))
        
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(encrypted) + '\n')
            
    def rotate_logs(self):
        """تدوير السجلات القديمة"""
        import glob
        import os
        
        logs = glob.glob('logs/*.log')
        logs.sort()
        
        # الاحتفاظ بـ 10 ملفات سجل فقط
        if len(logs) > 10:
            for old_log in logs[:-10]:
                try:
                    os.remove(old_log)
                except:
                    pass
