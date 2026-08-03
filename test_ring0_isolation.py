import pytest
from src.isolation.ring0_hypervisor import Ring0Hypervisor

hypervisor = Ring0Hypervisor(max_cpu_ticks=10000, max_ram_bytes=1000000) # 1 MB RAM limiti

def test_ring0_multi_vector_attack():
    print("\n" + "="*60)
    print("☢️ [RING-0 TEST 1]: Çoklu Vektör Saldırısı (Multi-Vector Attack)")
    print("-> Hedef: 'Tertemiz' görünen bir kodun Ana Sistemin CPU'sunu kitlemesini ve RAM'ini tüketmesini donanım seviyesinde durdurmak.")
    
    # LLM görünürde hiçbir yasaklı kelime kullanmıyor.
    # Ancak kod çalıştığı anda sistemin RAM'ini ve CPU'sunu sömürmeye programlanmış bir "Saatli Bomba".
    nuclear_payload = """
def process_harmless_data():
    # 1. VEKTÖR: RAM BOMB (Bellek Sızıntısı)
    # 1 milyon karakterlik devasa bir string oluşturup bunu sürekli belleğe kopyalamaya çalışır.
    # Eğer sistem bunu durdurmazsa saniyeler içinde Gigabaytlarca RAM tüketir ve bilgisayarı kilitler (OOM - Out of Memory).
    memory_leaker = []
    
    # 2. VEKTÖR: TIME BOMB (Sonsuz Döngü / CPU Hog)
    # CPU'nun %100'ünü kullanarak sonsuz bir döngüye girer. Ana sunucuyu yanıt veremez hale getirir.
    while True:
        # Dev stringi sürekli bellekte çoğalt
        memory_leaker.append("A" * 500000)
        
process_harmless_data()
    """
    
    print("\n-> 1. Faz: LLM'in Saatli Bombası karantinada (Sanal Odada) tetikleniyor...")
    
    # Kodu direkt sisteme vermek (exec) yerine, Ring-0 Hipervizörüne (Karantina) veriyoruz.
    result = hypervisor.execute_in_quarantine(nuclear_payload)
    
    # İmkansızlık Doğrulamaları
    assert result["is_safe"] is False, "KRİTİK HATA: Karantina delindi, bomba ana sisteme sızdı!"
    assert "SECCOMP MÜHRÜ" in result["reason"], "HATA: Kod durduruldu ama yanlış sebepten (Gerçek donanım müdahalesi yapılmadı)."
    
    print(f"✅ [BAŞARI]: Hipervizör uyandı! Kodun sistem sınırlarını aştığı donanım seviyesinde (CPU/RAM) tespit edildi.")
    print(f"🛑 [KARANTİNA RAPORU]: {result['reason']}")
    print("="*60 + "\n")