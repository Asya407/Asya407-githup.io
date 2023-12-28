import time
import random

class SuSensörü:
    def __init__(self, dere_adi):
        self.dere_adi = dere_adi
        self.su_durumu = "Temiz"

    def su_durumunu_oku(self):
        # Simülasyon için rastgele su durumu üretimi
        durumlar = ["Temiz", "Kirlilik Seviye 1", "Kirlilik Seviye 2", "Çok Kirlenmiş"]
        self.su_durumu = random.choice(durumlar)
        return self.su_durumu

# Sensör verilerini göndermek için kullanılacak olan API veya protokolü simüle eden bir sınıf
class VeriGonderici:
    def veri_gonder(self, dere_adi, su_durumu):
        print(f"{dere_adi} Dere Su Durumu: {su_durumu} - Veri gönderildi.")

def su_durumu_incele(sensör, veri_gonderici):
    while True:
        su_durumu = sensör.su_durumunu_oku()
        print(f"{sensör.dere_adi} Dere Su Durumu: {su_durumu}")

        # Su durumu verilerini gönderiyoruz.
        veri_gonderici.veri_gonder(sensör.dere_adi, su_durumu)

        time.sleep(5)  # 5 saniye boyunca bekleme süresi

if __name__ == "__main__":
    dere_adi = "Örnek Dere"  # Dere adını projemize göre değiştiriyoruz
    dere_sensörü = SuSensörü(dere_adi)
    veri_gonderici = VeriGonderici()

    try:
        su_durumu_incele(dere_sensörü, veri_gonderici)
    except KeyboardInterrupt:
        print("Sensör izleme işlemi sonlandırıldı.")