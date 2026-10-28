#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra Abartılı Hesap Makinesi
Bu kod gerçekten çalışır. Gerçekten.
Ama çıktılar abartılıdır. Çok abartılı.
"""

import time
import random

def dramatik_hesapla(a, b, islem):
    print("\n" + "="*50)
    print("DRAMATİK HESAPLAMA BAŞLIYOR...")
    print("Lütfen yerinizden kalkmayın. Evren titriyor.")
    time.sleep(1)
    
    for i in range(5):
        print(f"Hesaplanıyor... {'.' * (i+1)} (gerilim artıyor)")
        time.sleep(0.5)
    
    print("\nSONUÇ GELİYOR!")
    time.sleep(1)
    
    if islem == "+":
        sonuc = a + b
        mesaj = f"{a} ile {b}'nin birleşmesi evreni sarstı! Sonuç: {sonuc} (ama bu sadece görünen kısım)"
    elif islem == "-":
        sonuc = a - b
        mesaj = f"{a}'dan {b} çıkarıldı. Kalan acı: {sonuc}"
    elif islem == "*":
        sonuc = a * b
        mesaj = f"ÇARPIM! {a} kere {b}... Bu işin sonu yok: {sonuc}"
    elif islem == "/":
        if b == 0:
            mesaj = "BÖLME HATASI! Sıfıra böldünüz. Evren çöktü. Tekrar dene."
            sonuc = None
        else:
            sonuc = a / b
            mesaj = f"Bölündü... Parçalandı... Sonuç: {sonuc:.2f}"
    else:
        mesaj = "Bilinmeyen işlem. Matematik seninle konuşmuyor."
        sonuc = None
    
    print(mesaj)
    print("="*50 + "\n")
    
    # Gizli not: bazen sistemler de böyle abartılı çalışır
    return sonuc

def main():
    print("ULTRA ABARTILI HESAP MAKİNESİ'NE HOŞ GELDİNİZ!")
    print("Bu makine sıradan hesaplamaları epik bir maceraya çevirir.")
    print("Dikkat: Sonuçlar doğru olabilir ama sunum abartılıdır.\n")
    
    try:
        a = float(input("Birinci sayıyı gir (abartısız): "))
        b = float(input("İkinci sayıyı gir (yine abartısız): "))
        islem = input("İşlem (+, -, *, /): ").strip()
        
        dramatik_hesapla(a, b, islem)
    except ValueError:
        print("Sayı girmedin! Bu makine sadece sayılarla konuşur. Şaka yapma.")
    except KeyboardInterrupt:
        print("\nKaçtın. Hesap yarıda kaldı. Evren bekliyor.")

if __name__ == "__main__":
    main()
