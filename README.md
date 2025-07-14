Brain Tumor Detection Web App:

Bu proje, bir beyin tümörü sınıflandırma modelini temel alan web tabanlı bir tahmin sistemidir. Kullanıcı bir MRI veya beyin görüntüsü yükler, model resmi analiz eder ve tümör olup olmadığını tahmin eder.

Özellikler:

CNN tabanlı TensorFlow modeli ile yüksek doğruluklu tahmin
Gradio ile hazırlanmış arayüz
Görsel yükleme sonrası anlık tahmin ve sonuç gösterimi
Sunucuda biriken dosyalar tahmin sonrası otomatik silinir


Kurulum:

bash:
pip install -r requirements.txt


Model:
Model `cnn.py` dosyasında eğitilmiştir ve `models/cnn2_model.h5` olarak kaydedilmiştir.

