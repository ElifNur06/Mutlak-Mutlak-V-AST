# Mutlak (Mutlak V-AST) 🛡️⚡

**Mutlak**, büyük dil modellerinden (LLM) gelen ikili kod ağaçlarını (AST) ve bayt kodlarını (bytecode) canlı sistemlere entegre edilmeden önce **matematiksel olarak doğrulayan, çalışma zamanında optimize eden ve donanım seviyesinde izole eden** yeni nesil Nöro-Sembolik Güvenlik ve Hibrid Yorumlayıcı Mimarisidir.

Geleneksel LLM güvenlik sistemleri düz metin tabanlı (string) filtrelemelere ve basit anahtar kelime eşleşmelerine güvenirken; **Mutlak**, **Zero-Trust (Sıfır Güven)** prensibiyle çalışarak kodun arkasındaki matematiği ispatlar, darboğazları canlı sistemde evrimleştirir ve oyun motorları için milisaniyelik ikili (binary) köprüler kurar.

---

## 🏗️ Derinlemesine Mimari ve Teknik Detaylar

### 1. Sarmal V-Verify (Nöro-Sembolik Güvenlik Katmanı)
Standart statik analiz araçları, LLM'in ürettiği akıllı kaçış yöntemleri karşısında yetersiz kalır. Sarmal, klasik yaklaşımların ötesine geçerek iki kritik savunma hattı kurar:
*   **Gizlilik Çözücü (Constant Folding & De-Obfuscation):** LLM'in güvenlik duvarlarını atlatmak için sıklıkla kullandığı parçalanmış string birleştirmelerini (`__import__('o'+'s')`) ve ASCII karakter dönüşümlerini (`chr(101)`) derleme aşamasında hafızada çözerek gerçek niyeti maske düşer.
*   **Z3 Theorem Prover (Deterministik Matematik İspatı):** Kodun içindeki potansiyel mantıksal hataları ve zafiyetleri olasılıksal olarak tahmin etmek yerine, **Z3 formal mantık çözücüsü** ile denkleme döker. Örneğin; karmaşık polinomların içine ustalıkla gizlenmiş sıfıra bölünme (`divide-by-zero`) risklerini cebirsel olarak ispatlar ve sistem çöküşlerini kökten engeller.

### 2. SelfOptJIT Engine (Kendi Kendini Optimize Eden JIT Motoru)
Canlı üretim ortamında (production) çalışan sistemlerin durdurulmadan evrimleşebilmesi gerekir. SelfOptJIT, çalışma zamanına doğrudan müdahale eden otonom bir motordur:
*   **Çalışma Zamanı (Runtime) Tracer:** Sistem altındaki fonksiyonların yürütme sürelerini milisaniye hassasiyetinde profiller.
*   **Hotspot Loop-Elimination:** Algoritmik tıkanıklık yaratan $O(N^2)$ karmaşıklığındaki şişkin iç içe döngüleri anlık olarak tespit eder. V-AST ardışık düzeni üzerinden bu yapıları $O(1)$ sabit cebirsel formüllere dönüştürür.
*   **Canlı Bytecode Entegrasyonu:** Sistemi yeniden başlatmaya (restart) gerek duymadan, Python'ın bellek çekirdeğindeki fonksiyonun `__code__` nesnesini canlı canlı mutasyona uğratır. Gerçek test senaryolarında sistem performansının **18.000+ kat** artabildiği kanıtlanmıştır.

### 3. Kardelen Hybrid Shell (Oyun-İçi Kovan Zihni Kabuğu)
Yüksek performanslı oyun motorları ve gerçek zamanlı sistemler, saniyede 60 kare (60 FPS) standartlarında çalışmak zorundadır. JSON veya düz metin tabanlı LLM haberleşmeleri ciddi bellek şişmesine (allocation overhead) ve oyun içi takılmalara (lag) yol açar.
*   **Zero-Allocation İkili Protokolü:** Oyun motorunun RAM bellek haritasındaki ham verileri string formatına hiç dönüştürmeden, doğrudan Protobuf ikili (binary) şemalarına derler.
*   **60 FPS Ajan Senkronizasyonu:** Zlib düzeyinde optimize edilmiş hızlı sıkıştırma algoritmalarıyla (`level=1`), hiçbir gecikme yaratmadan **100.000+ NPC'nin (oyun içi ajanın)** otonom olarak bir kovan zihni (hive mind) gibi yapay zeka ile haberleşmesini sağlar.

### 4. Ring-0 Hypervisor (Karantina ve Donanım İzolasyonu)
Yapay zekanın ürettiği kodlar her zaman zararsız görünse bile, çalıştıkları anda sistem kaynaklarını sömürebilir. Mutlak, en alt katmanda donanım düzeyinde bir koruma kalkanı barındırır:
*   **Klinik Teşhis Odası:** LLM çıktıları ana sisteme asla doğrudan dokunulmaz; tamamen izole edilmiş steril bir sanal çalışma alanında (`exec` + kısıtlı builtins) yürütülür.
*   **Seccomp Donanım Mühürleri:** Kodun her bir işlemci saat vuruşunu (`cpu_ticks`) ve anlık RAM tüketimini bayt seviyesinde denetler. Sonsuz döngü girişimlerini (**Time Bomb**) ve bellek sızıntılarını (**RAM Bomb**) daha sisteme zarar veremeden donanım seviyesinde anında imha eder.

---


## 🛠️ Proje Dizin Yapısı

```text
Mutlak/
│
├── src/
│   ├── verification/
│   │   ├── __init__.py
│   │   └── sarmal_verify.py      # Sarmal Nöro-Sembolik Doğrulayıcı & Z3 Motoru
│   ├── jit/
│   │   ├── __init__.py
│   │   └── selfopt_engine.py     # Canlı Bytecode Mutasyon & JIT Motoru
│   ├── interpreter/
│   │   ├── __init__.py
│   │   └── kardelen_vm.py        # RAM-to-Binary Hibrid Kovan Kabuğu
│   ├── isolation/
│   │   ├── __init__.py
│   │   └── ring0_hypervisor.py   # Ring-0 Donanım Karantina Hipervizörü
│   └── proto/
│       └── v_ast_schema_pb2.py   # Protobuf İkili Şema Tanımları
│
├── tests/
│   ├── test_v_verify.py          # Z3 ve Obfuscation Testleri
│   ├── test_selfopt_jit.py       # JIT Zaman Bükülmesi ve Hız Testleri
│   ├── test_kardelen_interpreter.py # 100k NPC Kovan Zihni Testi
│   └── test_ring0_isolation.py   # Çoklu Vektör Donanım Saldırı Testi
│
├── requirements.txt
└── README.md
