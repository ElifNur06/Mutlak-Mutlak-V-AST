import pytest
import time
from src.jit.selfopt_engine import SelfOptJITEngine

# Eşik değerini senin hızlı işlemcine göre 10 milisaniyeye düşürdük
jit_engine = SelfOptJITEngine(threshold_ms=10.0)

# ==========================================
# İMKANSIZ SENARYO: ZAMAN BÜKÜLMESİ (CHRONOS)
# ==========================================
# Bu fonksiyon kasıtlı olarak devasa bir darboğaza (O(N^2)) sahiptir.
# 1^2 + 2^2 + 3^2... işlemini saçma sapan bir iç içe döngüyle hesaplar.
@jit_engine.jit_track
def chronos_singularity(n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == i:
                total += i**2
    return total

def test_chronos_hotspot_loop_elimination():
    print("\n" + "="*60)
    print("⏳ [JIT TEST 1]: Zaman Bükülmesi (O(N^2) -> O(1) Loop Elimination)")
    print("-> Hedef: Canlı çalışan yavaş bir kodu anında tespit edip bytecode'unu mutasyona uğratmak.")
    
    n_val = 4000 # 4000x4000 iterasyon = Eşiği kesin olarak aşacak ciddi bir işlemci yükü
    
    # -----------------------------------------------------
    # 1. FAZ: SPAGETTİ KODUN İLK ÇALIŞMASI (ISINMA)
    # -----------------------------------------------------
    print("\n-> 1. Faz: Orijinal Spagetti Kod Çalışıyor (Uzun sürecek)...")
    start_time = time.perf_counter()
    res1 = chronos_singularity(n_val)
    first_run_ms = (time.perf_counter() - start_time) * 1000
    
    print(f"-> 1. Faz Sonucu: {first_run_ms:.2f} ms sürdü. (Hesaplanan Sonuç: {res1})")
    
    # Sistem eşiği aştığı için JIT motoru şu an araya girdi ve fonksiyonu canlı olarak değiştirdi!
    
    # -----------------------------------------------------
    # 2. FAZ: MUTASYONA UĞRAMIŞ KODUN ÇALIŞMASI
    # -----------------------------------------------------
    print("\n-> 2. Faz: V-AST LLM Tarafından Mutasyona Uğratılmış Kod Çalışıyor...")
    start_time = time.perf_counter()
    res2 = chronos_singularity(n_val) # Aynı fonksiyonu çağırıyoruz ama içi değişti!
    second_run_ms = (time.perf_counter() - start_time) * 1000
    
    print(f"-> 2. Faz Sonucu: {second_run_ms:.2f} ms sürdü. (Hesaplanan Sonuç: {res2})")
    
    # -----------------------------------------------------
    # İMKANSIZLIK DOĞRULAMALARI (ASSERTIONS)
    # -----------------------------------------------------
    assert res1 == res2, "KRİTİK HATA: JIT Motoru kodu hızlandırayım derken matematiği bozdu!"
    assert first_run_ms > 10.0, "Test mantığı hatası: İlk kod JIT'i tetikleyecek kadar yavaş değildi."
    assert second_run_ms < 5.0, "KRİTİK HATA: JIT Motoru döngüyü yok edemedi, kod hala yavaş!"
    
    speedup = first_run_ms / max(0.001, second_run_ms)
    print(f"\n🚀 [JIT REKORU]: Performans anlık olarak {speedup:,.1f} KAT artırıldı!")
    print("="*60 + "\n")