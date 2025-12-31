#!/usr/bin/env python3
# Error Handling System

import traceback
import logging
import sys

class ErrorHandler:
    def __init__(self, log_file='logs/errors.log'):
        self.log_file = log_file
        
        # إعداد logging
        logging.basicConfig(
            filename=log_file,
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """معالجة الاستثناءات غير المعالجة"""
        error_msg = ''.join(traceback.format_exception(
            exc_type, exc_value, exc_traceback
        ))
        
        # تسجيل الخطأ
        logging.error(f"Unhandled exception:\\n{error_msg}")
        
        # إخفاء الأخطاء من المستخدم
        print("[!] An unexpected error occurred. Continuing...")
        
    def safe_execute(self, func, *args, **kwargs):
        """تنفيذ آمن لدالة مع معالجة الأخطاء"""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self.handle_exception(
                type(e), e, e.__traceback__
            )
            return None
