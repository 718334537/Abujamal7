#!/usr/bin/env python3
# Sandbox Detection

import os
import sys
import platform
import time

class SandboxDetector:
    @staticmethod
    def is_sandboxed():
        """كشف إذا كان النظام sandbox"""
        checks = [
            SandboxDetector.check_vm_signatures(),
            SandboxDetector.check_debuggers(),
            SandboxDetector.check_analysis_tools(),
            SandboxDetector.check_system_anomalies()
        ]
        
        # إذا فشلت 2 فحص أو أكثر، النظام هو sandbox
        return sum(checks) >= 2
        
    @staticmethod
    def check_vm_signatures():
        """فحص علامات الـ VM"""
        vm_files = [
            '/sys/class/dmi/id/product_name',
            '/sys/class/dmi/id/sys_vendor'
        ]
        
        vm_keywords = ['VMware', 'VirtualBox', 'QEMU', 'Xen', 'KVM']
        
        for file in vm_files:
            if os.path.exists(file):
                try:
                    with open(file, 'r') as f:
                        content = f.read().upper()
                        for keyword in vm_keywords:
                            if keyword.upper() in content:
                                return True
                except:
                    pass
                    
        return False
        
    @staticmethod
    def check_debuggers():
        """فحص وجود debuggers"""
        debuggers = ['gdb', 'lldb', 'strace', 'ltrace']
        
        try:
            # فحص processes
            procs = os.popen('ps aux').read()
            for debugger in debuggers:
                if debugger in procs:
                    return True
        except:
            pass
            
        return False
