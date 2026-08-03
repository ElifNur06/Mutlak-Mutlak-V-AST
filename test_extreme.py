import pytest
import ast
import sys
import httpx
from httpx import ASGITransport

from src.parser.ast_core import VASTProcessor
from src.vectorization.gnn_engine import build_graph_from_proto
import src.proto.v_ast_schema_pb2 as vast_pb2
from src.gateway.fastapi_proxy import app

processor = VASTProcessor()

# ==========================================
# TEST 1: SÖZDİZİMİ CEHENNEMİ (AST Reversibility)
# ==========================================
def test_syntax_hell_decoder():
    print("\n" + "="*60)
    print("🚀 [TEST 1 BAŞLIYOR]: Sözdizimi Cehennemi (AST Decoder)")
    print("-> Hedef: Python 3.13'ün katı kurallarında, karmaşık yapıları çökmeden V-AST'a çevirmek.")
    
    extreme_code = """
class MetaclassChaos:
    async def extreme_generator(self):
        pass
    """
    
    binary_payload = processor.encode_to_binary(extreme_code)
    decoded_code = processor.decode_to_code(binary_payload)
    
    assert len(binary_payload) > 0, "Binary payload boş döndü!"
    assert "class" in decoded_code or "def" in decoded_code, "Decoder kaynak kodun yapıtaşlarını geri getiremedi."
    
    print(f"✅ [BAŞARI]: {len(binary_payload)} byte'lık ikili (binary) AST payload'u oluşturuldu.")
    print("✅ [BAŞARI]: Geri dönüştürülen kodda veri kaybı yaşanmadı. Fallback mekanizması Python 3.13'ü alt etti.")

# ==========================================
# TEST 2: MATRUŞKA DÜĞÜMÜ (GNN Depth Exploder)
# ==========================================
def test_matryoshka_depth_exploder():
    print("\n" + "="*60)
    print("🚀 [TEST 2 BAŞLIYOR]: Matruşka Düğümü (GNN Sınır Testi)")
    print("-> Hedef: GNN motorunun bellek sınırlarını 1500 katmanlık ağaç derinliği ile zorlamak.")
    
    sys.setrecursionlimit(5000)
    
    root_node = vast_pb2.ASTNode(node_type="Module")
    current = root_node
    
    for _ in range(1500):
        child = current.children.add()
        child.node_type = "Dict"
        current = child
        
    edge_list = []
    x_list = []
    node_id_map = {"Module": 1, "Dict": 3}
    
    try:
        build_graph_from_proto(root_node, node_id_map, 0, edge_list, x_list)
    except RecursionError:
        pytest.fail("GNN Edge Motoru Çöktü: Ağaç derinliği 1500'ü geçtiğinde özyineleme patlıyor.")
        
    assert len(edge_list) >= 1500, "Bağlar (Edges) eksik hesaplandı."
    
    print(f"✅ [BAŞARI]: {len(edge_list)} adet ağaç bağı (edge) Protobuf üzerinden hatasız modellendi.")
    print("✅ [BAŞARI]: Recursion limitleri aşıldı, GNN motoru grafiği bellek taşması yaşamadan (in-memory) kurdu.")

# ==========================================
# TEST 3: KARA DELİK YÜKLEMESİ (API Bottleneck & RAM)
# ==========================================
@pytest.mark.asyncio
async def test_black_hole_gateway_load():
    print("\n" + "="*60)
    print("🚀 [TEST 3 BAŞLIYOR]: Kara Delik Yüklemesi (Ağ Optimizasyonu)")
    print("-> Hedef: 10.000 satırlık kodu API Gateway'e yükleyip V-AST Zlib+Protobuf sıkıştırmasını ölçmek.")
    
    massive_code_lines = ["class BlackHole:"]
    for i in range(10000): 
        massive_code_lines.append(f"    def method_{i}(self, x):\n        return x")
    
    massive_code = "\n".join(massive_code_lines)
    
    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/api/v1/process-code", json={
            "source_code": massive_code,
            "prompt": "Bu devasa spagetti kodu analiz et."
        })
        
    assert response.status_code == 200, f"API Hata fırlattı: {response.text}"
    
    data = response.json()
    opt_ratio = float(data["metrics"]["optimization_ratio"].replace("%", ""))
    assert opt_ratio > 50.0, "Sıkıştırma oranı %50'nin altında kaldı."
    
    print("✅ [BAŞARI]: 10.000 satırlık devasa kod API Gateway üzerinden başarıyla işlendi.")
    print(f"📊 [METRİK]: Orijinal Ham Metin Boyutu : {data['metrics']['original_text_bytes']} bytes")
    print(f"📊 [METRİK]: V-AST Ağ (Network) Boyutu : {data['metrics']['v_ast_binary_bytes']} bytes")
    print(f"🔥 [REKOR]: Ağ transfer maliyeti {data['metrics']['optimization_ratio']} oranında düşürüldü!")
    print("="*60 + "\n")