import requests
import time

def follow_account(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"✅ تم الوصول إلى حساب @{username}")
            print("📲 إرسال طلب متابعة (تمثيلي)...")
            time.sleep(1)
            print("✔️ متابعة تمت (وهمية)")
        else:
            print("❌ الحساب غير موجود أو تم الحظر.")
    except Exception as e:
        print(f"حدث خطأ: {e}")

def main():
    username = input("أدخل اسم المستخدم لحساب التيك توك: @")
    times = int(input("كم مرة تريد المحاولة؟ "))
    for i in range(times):
        print(f"🔁 محاولة رقم {i+1}")
        follow_account(username)
        time.sleep(2)

if __name__ == "__main__":
    main()
