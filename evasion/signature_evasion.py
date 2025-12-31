#!/usr/bin/env python3
# Signature Evasion Techniques

import hashlib
import random
import string

class SignatureEvasion:
    @staticmethod
    def mutate_binary(binary_path):
        """تغيير توقيع binary"""
        with open(binary_path, 'rb') as f:
            data = f.read()
            
        # إضافة bytes عشوائية في نهاية الملف
        padding = bytes([random.randint(0, 255) for _ in range(1024)])
        mutated = data + padding
        
        new_path = binary_path + '.mutated'
        with open(new_path, 'wb') as f:
            f.write(mutated)
            
        return new_path
        
    @staticmethod
    def change_hash(file_path):
        """تغيير hash الملف"""
        # قراءة الملف
        with open(file_path, 'rb') as f:
            content = f.read()
            
        # إضافة تعليقات عشوائية إذا كان ملف نصي
        if file_path.endswith(('.py', '.js', '.txt')):
            random_comment = f"# Random: {''.join(random.choices(string.ascii_letters, k=32))}\\n"
            content = random_comment.encode() + content
            
        # كتابة النسخة المعدلة
        new_path = file_path + '.evaded'
        with open(new_path, 'wb') as f:
            f.write(content)
            
        return new_path
