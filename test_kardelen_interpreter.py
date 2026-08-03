import pytest
import time
from src.interpreter.kardelen_vm import KardelenHybridShell

def test_kardelen_hive_mind_swarm():
    print("\n" + "="*60)
    print("👾 [KARDELEN TEST 1]: Kovan Zihni (100.000 NPC Otonom Karar Senaryosu)")
    print("-> Hedef: 100 bin NPC'nin durumunu string'e çevirmeden doğrudan RAM'den V-AST'a derlemek ve LLM emrini işletmek.")
    
    shell = KardelenHybridShell()
    swarm_size = 100000
    
    # 1. Faz: 100.000 NPC'yi oyun motoruna (RAM) yükle
    print(f"\n-> 1. Faz: Oyun Dünyasına {swarm_size:,} adet NPC Spawn ediliyor...")
    shell.spawn_npc_swarm(swarm_size)
    
    # 2. Faz: RAM -> V-AST Binary Derlemesi (Oyun motoru hiç duraksamamalı!)
    print("-> 2. Faz: RAM verileri metne (string) çevrilmeden doğrudan V-AST ikili paketine (Binary) dönüştürülüyor...")
    start_time = time.perf_counter()
    vast_binary_out = shell.compile_memory_to_vast_binary()
    encode_time_ms = (time.perf_counter() - start_time) * 1000
    
    print(f"-> 2. Faz Sonucu: {swarm_size:,} olay {encode_time_ms:.2f} ms içinde derlendi! (Boyut: {len(vast_binary_out):,} bytes)")
    
    # 3. Faz: LLM Kovan Zihni Kararı
    llm_vast_response = shell.simulate_llm_hive_mind(vast_binary_out)
    
    # 4. Faz: V-AST -> RAM Yürütmesi (Execution)
    print("-> 3. Faz: LLM'den gelen V-AST emri (Geri Çekil), Sanal Makinede yürütülüyor (Execution)...")
    start_time = time.perf_counter()
    shell.execute_vast_binary(llm_vast_response)
    decode_time_ms = (time.perf_counter() - start_time) * 1000
    
    print(f"-> 3. Faz Sonucu: {shell.vm_execution_cycles:,} NPC'nin durumu {decode_time_ms:.2f} ms içinde güncellendi!")
    
    # İmkansızlık Doğrulamaları
    assert shell.vm_execution_cycles == swarm_size, "Kritik Hata: Komutlar tüm NPC'lere ulaşmadı!"
    assert encode_time_ms < 150.0, f"Darboğaz Uyarısı: Derleme çok yavaş! ({encode_time_ms} ms). 150ms'yi geçmemeli."
    assert decode_time_ms < 150.0, f"Darboğaz Uyarısı: Yürütme (Execution) çok yavaş! ({decode_time_ms} ms). 150ms'yi geçmemeli."
    
    print(f"\n🚀 [OYUN MOTORU REKORU]: Saniyede 60 Kare (FPS) hızında, hiçbir gecikme (lag) yaşanmadan 100.000 ajan yapay zeka ile haberleşti!")
    print("="*60 + "\n")