# Resim İşleme Uygulaması

Bu proje, kullanıcıların resimleri yükleyip çeşitli işlemler (boyutlandırma, döndürme, çevirme, kırpma) yapabilecekleri bir web uygulamasıdır.

## Özellikler

- Resim yükleme
- Resim boyutunu değiştirme
- Resmi döndürme
- Resmi yatay veya dikey çevirme
- Resmi kırpma
- İşlenmiş resmi indirme

## Kurulum

### Ön Koşullar

- Node.js ve npm
- Python 3.6 veya üzeri

### Frontend (React)

```bash
# frontend klasörüne gidin
cd frontend

# Bağımlılıkları yükleyin
npm install

# Uygulamayı başlatın
npm start
```

### Backend (Python/Flask)

```bash
# backend klasörüne gidin
cd backend

# Sanal ortamı etkinleştirin (Windows)
venv\Scripts\activate

# Sanal ortamı etkinleştirin (Linux/Mac)
source venv/bin/activate

# Bağımlılıkları yükleyin
pip install flask flask-cors Pillow

# Sunucuyu başlatın
python app.py
```

## Kullanım

1. Tarayıcınızda `http://localhost:3000` adresine gidin
2. "Resim Seç" butonuna tıklayarak bir resim seçin
3. "Yükle" butonuna tıklayarak resmi yükleyin
4. İstediğiniz düzenleme ayarlarını yapın:
   - Boyutlandırma: Yeni genişlik ve yükseklik belirleyin
   - Döndürme: Resmi belirli bir açıda döndürün
   - Çevirme: Resmi yatay veya dikey olarak çevirin
   - Kırpma: Resmin belirli bir bölgesini seçin
5. "Resmi İşle" butonuna tıklayın
6. İşlenmiş resmi görüntüleyin ve isterseniz indirin

## Teknolojiler

- Frontend: React
- Backend: Flask
- Resim İşleme: Pillow (Python) #   O p e n C V  
 #   O p e n C v - r e a c t  
 #   O p e n C v - r e a c t  
 