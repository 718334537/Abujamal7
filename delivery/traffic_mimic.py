#!/usr/bin/env python3
# Traffic Mimicry

import random
import time

class TrafficMimic:
    @staticmethod
    def mimic_google_traffic():
        """محاكاة حركة مرور Google"""
        google_patterns = [
            {
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'referers': [
                    'https://www.google.com/',
                    'https://www.google.com/search?q=saba+live',
                    'https://www.google.com/search?q=free+coins'
                ],
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            },
            {
                'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
                'referers': [
                    'https://m.google.com/',
                    'https://www.google.com/mobile/'
                ],
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
        ]
        return random.choice(google_patterns)
        
    @staticmethod
    def mimic_android_app_traffic():
        """محاكاة حركة مرور تطبيق Android"""
        app_headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G975F Build/QP1A.190711.020)',
            'X-Requested-With': 'com.saba.live',
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive'
        }
        return app_headers
