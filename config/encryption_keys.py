#!/usr/bin/env python3
# Encryption Key Management

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json
import hashlib
import os

class EncryptionManager:
    def __init__(self):
        self.key_dir = "config/keys"
        os.makedirs(self.key_dir, exist_ok=True)
        
    def generate_rsa_keys(self):
        """توليد مفاتيح RSA"""
        key = RSA.generate(2048)
        
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        with open(f"{self.key_dir}/private.pem", "wb") as f:
            f.write(private_key)
            
        with open(f"{self.key_dir}/public.pem", "wb") as f:
            f.write(public_key)
            
        return private_key, public_key
        
    def generate_aes_key(self, key_name="master"):
        """توليد مفتاح AES"""
        key = get_random_bytes(32)  # 256-bit
        iv = get_random_bytes(16)   # 128-bit
        
        key_data = {
            'key': base64.b64encode(key).decode(),
            'iv': base64.b64encode(iv).decode(),
            'algorithm': 'AES-256-CBC',
            'created': '2024-01-01'
        }
        
        with open(f"{self.key_dir}/{key_name}.json", 'w') as f:
            json.dump(key_data, f)
            
        return key, iv
        
    def rotate_keys(self):
        """تدوير المفاتيح لأسباب أمنية"""
        import time
        
        # توليد مفتاح جديد
        new_key = get_random_bytes(32)
        
        # تشفير المفاتيح القديمة بالمفتاح الجديد
        old_keys = self.load_all_keys()
        
        for key_name in old_keys:
            cipher = AES.new(new_key, AES.MODE_CBC)
            encrypted_key = cipher.encrypt(
                base64.b64decode(old_keys[key_name]['key'])
            )
            
            # حفظ المفتاح المشفر
            with open(f"{self.key_dir}/{key_name}.enc", 'wb') as f:
                f.write(cipher.iv + encrypted_key)
