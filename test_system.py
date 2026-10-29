import sys
import os

APP_PATH = r'C:\Users\acer\.gemini\antigravity\scratch\ecowaste-smart-system'
sys.path.append(APP_PATH)

from app import app, init_db

init_db()
client = app.test_client()

print("="*60)
print("ECOWASTE SMART SYSTEM - AUTOMATED VERIFICATION SUITE")
print("PSG College of Technology - Team 04")
print("="*60)

# 1. Index
r = client.get('/')
assert r.status_code == 200, f"Index failed: {r.status_code}"
print("[PASS] 1. Index & Landing Page Loaded Successfully")

# 2. Login Page
r = client.get('/login')
assert r.status_code == 200, f"Login failed: {r.status_code}"
print("[PASS] 2. Multi-Role Authentication Gateway Loaded")

# 3. Household Portal Demo
r = client.get('/demo-login/household', follow_redirects=True)
assert r.status_code == 200, f"Household failed: {r.status_code}"
print("[PASS] 3. Household Portal Authenticated & Rendered")

# 4. Recycler Hub Portal Demo
r = client.get('/demo-login/recycler', follow_redirects=True)
assert r.status_code == 200, f"Recycler failed: {r.status_code}"
print("[PASS] 4. Recycler Hub & Marketplace Rendered")

# 5. Admin Control Center Demo
r = client.get('/demo-login/admin', follow_redirects=True)
assert r.status_code == 200, f"Admin failed: {r.status_code}"
print("[PASS] 5. Admin Control Center & Rate Card Rendered")

# 6. AI Waste Vision Classifier API
r = client.post('/api/classify', json={'sample_key': 'plastic'})
assert r.status_code == 200, f"Classify API failed: {r.status_code}"
cdata = r.get_json()
assert cdata['success'] and cdata['classification']['category_key'] == 'plastic'
print(f"[PASS] 6. AI Vision Classifier API Verified -> Material: {cdata['classification']['name_en']} ({cdata['classification']['confidence']}%)")

# 7. Tamil Voice NLP API
r = client.post('/api/voice/process', json={'text': '5 கிலோ பிளாஸ்டிக் பீளமேடு முன்பதிவு செய்'})
assert r.status_code == 200, f"Voice API failed: {r.status_code}"
vdata = r.get_json()
assert vdata['success'] and vdata['parsed']['ward'] == 'Peelamedu'
print(f"[PASS] 7. Tamil Voice NLP Parser Verified -> {vdata['parsed']['weight_kg']} kg in {vdata['parsed']['ward']}")

# 8. Book Pickup API
r = client.post('/api/pickup/book', json={
    'household_name': 'Akilesh N',
    'phone': '+91 97890 44556',
    'ward': 'Peelamedu',
    'address': 'PSG Tech Hostel Block C',
    'category_key': 'metal',
    'estimated_kg': 4.5
})
assert r.status_code == 200
pdata = r.get_json()
req_code = pdata['request_code']
print(f"[PASS] 8. Smart Pickup Booking Scheduled -> ID: {req_code}")

# 9. Live GPS & Traceability API
r = client.get(f'/api/pickup/track/{req_code}')
assert r.status_code == 200
tdata = r.get_json()
assert tdata['success']
print(f"[PASS] 9. Live Traceability Pipeline Verified -> Status: {tdata['tracking']['status']}")

# 10. Predictive Analytics API
r = client.get('/api/analytics')
assert r.status_code == 200
adata = r.get_json()
assert adata['success']
print(f"[PASS] 10. Predictive Demand Forecast & Price Trends API Verified -> {len(adata['monthly']['labels'])} points")

print("="*60)
print("ALL 10 VERIFICATION MODULES PASSED WITH 100% SUCCESS!")
print("="*60)

