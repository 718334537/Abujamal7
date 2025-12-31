#!/usr/bin/env python3
# System Compatibility Check

import platform
import os
import sys

class SystemCheck:
    @staticmethod
    def check_requirements():
        """فحص متطلبات النظام"""
        requirements = {
            'python_version': '3.8+',
            'os': ['Linux', 'Darwin'],
            'ram': 2048,  # 2GB minimum
            'disk': 100   # 100MB free space
        }
        
        results = {
            'python': sys.version_info >= (3, 8),
            'os': platform.system() in requirements['os'],
            'ram': SystemCheck.check_ram(requirements['ram']),
            'disk': SystemCheck.check_disk(requirements['disk'])
        }
        
        return all(results.values()), results
        
    @staticmethod
    def check_ram(min_mb):
        """فحص الذاكرة"""
        try:
            if platform.system() == 'Linux':
                with open('/proc/meminfo', 'r') as f:
                    for line in f:
                        if 'MemTotal' in line:
                            kb = int(line.split()[1])
                            mb = kb // 1024
                            return mb >= min_mb
        except:
            pass
        return True  # Assume sufficient if check fails
        
    @staticmethod
    def check_disk(min_mb):
        """فحص مساحة التخزين"""
        try:
            stat = os.statvfs('/')
            free_mb = (stat.f_bavail * stat.f_frsize) // (1024 * 1024)
            return free_mb >= min_mb
        except:
            return True
