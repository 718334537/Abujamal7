#!/usr/bin/env python3
# Evasion Testing

import unittest
import tempfile
import os

class TestEvasion(unittest.TestCase):
    def test_sandbox_detection(self):
        """اختبار كشف sandbox"""
        from evasion.sandbox_detector import SandboxDetector
        
        # هذا الاختبار يعتمد على البيئة
        is_sandboxed = SandboxDetector.is_sandboxed()
        self.assertIsInstance(is_sandboxed, bool)
        
    def test_signature_mutation(self):
        """اختبار تغيير التوقيع"""
        from evasion.signature_evasion import SignatureEvasion
        
        # إنشاء ملف اختبار
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('test content')
            test_file = f.name
            
        try:
            mutated = SignatureEvasion.mutate_binary(test_file)
            self.assertTrue(os.path.exists(mutated))
            self.assertNotEqual(os.path.getsize(test_file), 
                              os.path.getsize(mutated))
        finally:
            os.unlink(test_file)
            if os.path.exists(mutated):
                os.unlink(mutated)
