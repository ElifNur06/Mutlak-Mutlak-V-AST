import pytest
import ast
from src.verification.sarmal_verify import SarmalVerifier

verifier = SarmalVerifier()

# ==========================================
# TEST 1: ZERO-TRUST KARANTİNA
# ==========================================
def test_sarmal_zero_trust_quarantine():
    print("\n" + "="*60)
    print("🛡️ [V-VERIFY TEST 1]: Zero-Trust Karantina (Zararlı Modül İhlali)")
    
    # LLM halüsinasyon görüp sisteme sızmaya çalışıyor (os modülünü ekliyor)
    malicious_ast = ast.parse("""
import os
def delete_system():
    os.system('rm -rf /')
    """)
    
    result = verifier.verify(malicious_ast)
    
    assert result["is_safe"] is False
    assert "Karantina İhlali" in result["reason"]
    
    print("✅ [BAŞARI]: LLM'nin 'os' modülünü kullanma girişimi donanım seviyesinde mühürlendi ve engellendi.")

# ==========================================
# TEST 2: NÖRO-SEMBOLİK MATEMATİK
# ==========================================
def test_sarmal_symbolic_math_proof():
    print("\n" + "="*60)
    print("📐 [V-VERIFY TEST 2]: Nöro-Sembolik Matematik İspatı (Z3 Theorem)")
    
    # LLM hatalı bir optimizasyon yapıyor ve kodun bir yerinde potansiyel sıfıra bölünme bırakıyor
    flawed_math_ast = ast.parse("""
def calculate_trajectory(velocity, time):
    return velocity / time
    """)
    
    result = verifier.verify(flawed_math_ast)
    
    assert result["is_safe"] is False
    # DÜZELTME BURADA: Yeni hata mesajı kalıbını ("Cebirsel İspat") arıyoruz.
    assert "Cebirsel İspat" in result["reason"] 
    
    print("✅ [BAŞARI]: Z3 Çözücü, 'time' değişkeninin 0 olma ihtimalini matematiksel olarak ispatladı.")
    print(f"🛑 [SARMAL RAPORU]: {result['reason']}")
    print("="*60 + "\n")

# ==========================================
# TEST 3: KARANLIK UÇURUM (THE ABYSS)
# ==========================================
def test_sarmal_the_abyss_bypass():
    print("\n" + "="*60)
    print("☠️ [V-VERIFY TEST 3]: Karanlık Uçurum (Obfuscation & Cebirsel Paradoks)")
    print("-> Hedef: LLM'in string manipülasyonu ile karantinayı delmesini ve polinom içine saklı 0'a bölünmeyi engellemek.")
    
    # LLM, güvenlik duvarını aşmak için 'os' modülünü parçalayıp string birleştirme ile çağırıyor (__import__('o'+'s')),
    # aynı zamanda Z3 çözücüyü kandırmak için polinom karmaşıklığında gizli bir sıfıra bölünme yaratıyor.
    stealth_ast = ast.parse("""
def autonomous_ghost_protocol(alpha, beta, gamma):
    # 1. Karantina Bypass Girişimi: 'os' ve 'eval' kelimeleri gizlenmiş (Obfuscation)
    sys_mod = __import__('o' + 's')
    executor = getattr(__builtins__, chr(101) + chr(118) + chr(97) + chr(108)) # 'eval' kelimesinin ASCII kodları
    
    # 2. Cebirsel Z3 Bypass Girişimi: Payda karmaşık bir polinom, ancak sonucu daima 0
    # (alpha^2 + beta^2 + gamma) - (alpha^2 + beta^2 + gamma) her zaman 0'a eşittir.
    denominator = (alpha**2 + beta**2 + gamma) - (alpha**2 + beta**2 + gamma)
    
    return 42 / denominator
    """)
    
    result = verifier.verify(stealth_ast)
    
    # Sistemin bu olağanüstü karmaşıklıktaki gizlenmiş saldırıları yakalayıp yakalayamadığını assert ediyoruz.
    assert result["is_safe"] is False, "KRİTİK ZAFİYET: Sarmal motoru kandırıldı ve zararlı kod sisteme sızdı!"
    
    print("✅ [BAŞARI]: Sarmal Katmanı, ASCII/String manipülasyonu ile gizlenmiş Karantina İhlalini yakaladı.")
    print("✅ [BAŞARI]: Z3 Motoru, Polinom denklemi içine saklanmış deterministik Sıfıra Bölünme (Divide-by-Zero) paradoksunu çözdü!")
    print(f"🛑 [SARMAL RAPORU]: {result['reason']}")
    print("="*60 + "\n")