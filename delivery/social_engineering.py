#!/usr/bin/env python3
# Social Engineering Templates

import random

class SocialEngineering:
    @staticmethod
    def generate_messages():
        """توليد رسائل هندسة اجتماعية"""
        templates = [
            {
                "title": "🎁 FREE 50,000 SABA COINS!",
                "message": "Limited time offer! Click to claim your free coins: {link}",
                "urgency": "HURRY! Offer expires in 24 hours!"
            },
            {
                "title": "⚠️ SECURITY ALERT: Your Account",
                "message": "Saba Live detected suspicious activity. Verify now: {link}",
                "urgency": "VERIFY NOW TO PREVENT BAN!"
            },
            {
                "title": "📱 SABA LIVE 5.3 UPDATE AVAILABLE",
                "message": "New features + 30,000 free coins. Update now: {link}",
                "urgency": "Update required to continue using app"
            },
            {
                "title": "🏆 YOU WON A PRIZE!",
                "message": "Congratulations! You won 100,000 coins. Claim: {link}",
                "urgency": "Claim within 1 hour"
            }
        ]
        return random.choice(templates)
        
    @staticmethod
    def generate_phishing_email():
        """توليد إيميل تصيد محترف"""
        email_template = """
        From: Saba Live Support <support@sabalive.com>
        Subject: Important Security Update Required
        
        Dear Saba Live User,
        
        Our security team has detected unusual activity on your account.
        To protect your coins and account, please verify your identity:
        
        🔗 VERIFY NOW: {phishing_link}
        
        This verification must be completed within 24 hours to avoid
        temporary suspension of your account.
        
        After verification, you will receive:
        • 25,000 FREE coins as compensation
        • VIP status for 30 days
        • Priority support
        
        Thank you,
        Saba Live Security Team
        
        ⚠️ This is an automated message. Please do not reply.
        """
        return email_template
