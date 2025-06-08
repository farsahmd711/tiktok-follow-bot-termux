#!/bin/bash

echo "🔧 جاري تثبيت المتطلبات..."
pkg install python -y > /dev/null
pip install requests > /dev/null

echo "🚀 تشغيل البوت..."
python tiktok_bot.py
