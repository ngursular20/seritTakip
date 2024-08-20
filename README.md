Şerit Değişikliği Tespit Sistemi

Bu proje, video akışında şerit değiştirmeyi tespit etmek için bir görüntü işleme algoritması kullanmaktadır. Yol şeritlerini algılayarak, kullanıcıya şerit değişikliği olup olmadığını belirtir.

Özellikler

Şerit Algılama: Video akışında yol şeritlerini tespit eder.

Şerit Değişikliği Tespiti: Şerit değişikliği olup olmadığını belirler ve ekranda belirtir.

Teknolojiler

Python: Programlama dili.

OpenCV: Görüntü işleme için kullanıldı.

NumPy: Matematiksel işlemler ve dizi işlemleri için kullanıldı.

Kurulum ve Çalıştırma

Gereksinimler:

Python 3.x

OpenCV ve NumPy paketlerini yüklemek için:

pip install opencv-python numpy

Video Dosyası: yol.mp4 adlı video dosyasının bulunduğundan emin olun veya cap = cv2.VideoCapture('video_dosyası.mp4') satırını uygun video dosya adı ile değiştirin.
Kodun Çalıştırılması:

python script_adı.py

Kullanım

Video akışını başlatır ve her çerçevede yol şeritlerini algılar.

Şerit değişikliği algılandığında, ekranda "Şerit Değişikliği!" mesajını görüntüler.
