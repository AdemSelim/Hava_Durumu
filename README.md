# Hava_Durumu


# 🌦️ Gelişmiş Hava Durumu Uygulaması

## Tanım
Bu Python tabanlı uygulama, **OpenWeatherMap API** ve **IP tabanlı konum algılama** ile birlikte anlık hava durumu ve 5 günlük tahmin bilgilerini alarak kullanıcıya görsel arayüz üzerinden sunar. Ayrıca verileri `.txt` dosyasına kaydeder ve masaüstü bildirimi gösterir.

## Özellikler

- 📍 IP tabanlı şehir algılama (boş bırakılırsa otomatik bulunur)
- 🌡️ Anlık hava durumu bilgisi (sıcaklık, hissedilen, rüzgar, nem, vb.)
- 📅 5 günlük hava durumu tahmini
- 💾 Bilgileri `hava_durumu.txt` dosyasına kaydetme
- 🔔 Masaüstü bildirimi ile bilgilendirme
- 🖼️ Kullanıcı dostu, Tkinter tabanlı arayüz

## Ekran Görüntüsü

```
+----------------------------------------------------+
| 🌦️ Gelişmiş Hava Durumu Uygulaması               |
| Şehir Girin (Boş bırakılırsa otomatik bulunur):   |
| [__________________________] [Göster Butonu]       |
|                                                    |
| 📍 Şehir: İstanbul                                 |
| 🌡️ Sıcaklık: 24°C                                 |
| 🤗 Hissedilen: 26°C                                |
| ...                                                |
| 📅 5 Günlük Tahmin:                                |
| 2025-06-19 12:00 | 26°C | açık                     |
+----------------------------------------------------+
```

## Gereksinimler

Aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

```bash
pip install requests plyer
```

Python yerleşik kütüphaneleri dışında yalnızca:
- `requests`
- `plyer`
kullanılmaktadır.

## Kurulum ve Çalıştırma

1. Kod dosyasını (`WeatherAdvance.py`) indirin.
2. API anahtarınızı bu satıra ekleyin:
   ```python
   API_KEY = "SENİN_API_ANAHTARIN"
   ```
3. Terminalden veya bir IDE'den dosyayı çalıştırın:
   ```bash
   python WeatherAdvance.py
   ```

## Notlar

- OpenWeatherMap API anahtarınızı almak için: https://openweathermap.org/api
- Masaüstü bildirimleri Windows, Linux ve macOS'ta çalışır; ancak bildirim izinleri sistem ayarlarına bağlı olarak değişebilir.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
