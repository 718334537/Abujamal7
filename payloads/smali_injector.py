#!/usr/bin/env python3
# Smali Code Injector for Android APKs

import re
import os

class SmaliInjector:
    def __init__(self):
        self.smali_templates = {
            'coin_injector': self.get_coin_injector_smali(),
            'data_stealer': self.get_data_stealer_smali(),
            'root_check': self.get_root_check_smali()
        }
        
    def get_coin_injector_smali(self):
        """كود Smali لحقن العملات"""
        return """
        .class public Lcom/saba/exploit/CoinManager;
        .super Ljava/lang/Object;
        
        .field private static final TARGET_BALANCE:I = 0x1869f  # 99999
        
        .method public static injectCoins()V
            .locals 3
            
            .prologue
            const-string v0, "coin_balance"
            
            sget v1, Lcom/saba/exploit/CoinManager;->TARGET_BALANCE:I
            
            invoke-static {v0, v1}, Lcom/saba/exploit/CoinManager;->setPreference(Ljava/lang/String;I)V
            
            return-void
        .end method
        
        .method private static setPreference(Ljava/lang/String;I)V
            .locals 3
            
            .prologue
            const-string v0, "user_prefs"
            
            const/4 v1, 0x0
            
            invoke-static {v0, v1}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;
            
            move-result-object v0
            
            invoke-interface {v0}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;
            
            move-result-object v0
            
            invoke-interface {v0, p0, p1}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;
            
            invoke-interface {v0}, Landroid/content/SharedPreferences$Editor;->apply()V
            
            return-void
        .end method
        """
        
    def inject_into_smali(self, smali_file, injection_code):
        """حقن كود في ملف Smali"""
        try:
            with open(smali_file, 'r') as f:
                content = f.read()
                
            # البحث عن مكان الحقن (عادة بعد .locals)
            lines = content.split('\\n')
            injection_point = -1
            
            for i, line in enumerate(lines):
                if '.locals' in line and injection_point == -1:
                    injection_point = i + 1
                    break
                    
            if injection_point != -1:
                lines.insert(injection_point, injection_code)
                new_content = '\\n'.join(lines)
                
                with open(smali_file, 'w') as f:
                    f.write(new_content)
                    
                return True
                
        except Exception as e:
            print(f"[-] Smali injection failed: {e}")
            
        return False
