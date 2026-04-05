import google.generativeai as genai
import os

# API Anahtarını buraya tırnak içine yapıştır
API_KEY = "AIzaSyBWhqDOOUoVDSnZJC8m8lvEoj2Tst_V80E"

genai.configure(api_key=API_KEY)

# Model ayarları
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

def baslat():
    # ARAS AI Kimliği
    chat = model.start_chat(history=[])
    
    print("-" * 30)
    print("ARAS AI SİSTEMİ ÇEVRİMİÇİ")
    print("Çıkmak için 'exit' yazabilirsin.")
    print("-" * 30)

    while True:
        user_input = input("Sen: ")
        
        if user_input.lower() == 'exit':
            print("Aras AI kapatılıyor...")
            break
            
        try:
            # Burası yapay zekaya "sen Aras AI'sın" talimatını verir
            response = chat.send_message(f"Senin adın ARAS AI. Bir Türk yapay zeka asistanısın. Kullanıcı şunu sordu: {user_input}")
            print(f"\nARAS AI: {response.text}\n")
        except Exception as e:
            print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    baslat()
