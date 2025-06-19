import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
from plyer import notification

# ➤ Kendi OpenWeatherMap API KEY'inizi buraya yazın:
API_KEY = "d4c8b7836cbcaa9d5ed2b2075d71011a"

# ➤ IP tabanlı konum bulma
def get_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        if data["status"] == "success":
            return data["city"]
        else:
            return None
    except:
        return None

# ➤ Anlık hava durumu
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        sys = data['sys']

        sunrise = datetime.datetime.fromtimestamp(sys['sunrise']).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(sys['sunset']).strftime('%H:%M')

        info = (
            f"📍 Şehir: {city}\n"
            f"🌡️ Sıcaklık: {main['temp']}°C\n"
            f"🤗 Hissedilen: {main['feels_like']}°C\n"
            f"☁️ Durum: {weather['description']}\n"
            f"💧 Nem: {main['humidity']}%\n"
            f"💨 Rüzgar: {wind['speed']} m/s\n"
            f"🌅 Gün Doğumu: {sunrise}\n"
            f"🌇 Gün Batımı: {sunset}\n"
        )
        return info
    else:
        return "Hava durumu alınamadı."

# ➤ 5 günlük tahmin
def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    forecast_text = "\n📅 5 Günlük Tahmin:\n"
    if response.status_code == 200:
        data = response.json()
        for forecast in data['list'][:5]:  # İlk 5 tahmin (~1 gün)
            dt_txt = forecast['dt_txt']
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            forecast_text += f"{dt_txt} | {temp}°C | {description}\n"
        return forecast_text
    else:
        return "Tahmin alınamadı."

# ➤ Dosyaya kaydet
def save_to_file(content):
    with open("hava_durumu.txt", "w", encoding="utf-8") as f:
        f.write(content)

# ➤ Masaüstü bildirim gönder
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # saniye
    )

# ➤ Butona basınca çalışacak ana fonksiyon
def show_weather():
    city = entry_city.get()
    if not city:
        city = get_location()
        if not city:
            messagebox.showerror("Hata", "Şehir bulunamadı!")
            return
    current = get_current_weather(city)
    forecast = get_forecast(city)
    full_report = current + "\n" + forecast

    result.delete(1.0, tk.END)
    result.insert(tk.END, full_report)

    save_to_file(full_report)
    send_notification(f"{city} Hava Durumu", f"{current.splitlines()[1]} | {current.splitlines()[3]}")

# ➤ Geliştirilmiş arayüz
root = tk.Tk()
root.title("🌦️ Hava Durumu Uygulaması")
root.geometry("600x600")
root.configure(bg="#87CEEB")  # Gökyüzü mavisi

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)

label = tk.Label(root, text="Şehir Girin (Boş bırakılırsa otomatik bulunur):", bg="#87CEEB", font=("Arial", 12))
label.pack(pady=10)

entry_city = ttk.Entry(root, font=("Arial", 12), width=30)
entry_city.pack(pady=5)

btn = ttk.Button(root, text="Hava Durumunu Göster", command=show_weather)
btn.pack(pady=10)

result = tk.Text(root, height=25, width=70, font=("Consolas", 10))
result.pack(pady=10)

root.mainloop()
