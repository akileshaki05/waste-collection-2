# ECOWASTE - SMART SYSTEM FOR HOUSEHOLD WASTE COLLECTION, RECYCLING AND VALUE ESTIMATION
**PSG COLLEGE OF TECHNOLOGY, COIMBATORE-641 004**  
*Department of Computer Applications | Academic Year 2026-2027*  
*Course: 26MX17 - Web Application Development*  
**Team No: 04**  
- **Aishwaryaa S.K** (26MX303)  
- **Akilesh N** (26MX304)  
- **Ashritaa N** (26MX306)  
- **Guide**: **Dr. Bhama S**

---

## 🌟 Project Overview
EcoWaste is an AI-powered web-based waste management and circular economy ecosystem developed specifically for Coimbatore municipal wards (Peelamedu, Gandhipuram, RS Puram, Singanallur, Saibaba Colony, etc.). It addresses the limitations of manual waste collection by connecting **Households**, **Recyclers / Scrap Dealers**, and **Administrators** through an intelligent, automated, and interactive platform.

---

## 🤖 Futuristic AI & Interactive Features
1. **AI Vision Waste Classifier**:
   - Deep learning computer vision simulation with real-time bounding boxes, confidence scoring, purity grading, and instant resale valuation.
   - Dual input: Live camera stream, file upload, or 5 built-in high-res sample presets (Plastic PET, Cardboard, Aluminium Cans, E-Waste PCB, Glass Bottles).
2. **Tamil Voice Assistant ("EcoBot / எக்கோபாட்")**:
   - Multilingual voice booking via Web Speech API supporting Tamil (`ta-IN`) and English (`en-IN`).
   - Authentic Tamil voice synthesis and NLP extraction of waste category, weight, and Coimbatore ward.
3. **Consolidated Neighbourhood Pickups & Route Optimization**:
   - Groups nearby household requests within wards (e.g. Peelamedu PSG Tech cluster) to reduce transport distance, saving fuel and carbon emissions.
4. **Live GPS Telemetry & 6-Stage Traceability Pipeline**:
   - `[Booked] ➔ [Assigned] ➔ [En Route] ➔ [Weighed & Paid] ➔ [Recycler Hub] ➔ [Recycled]`
   - Generates an official, verifiable **Green Recycling Certificate** with digital seal.
5. **Dynamic Value Estimator & Scrap Dealer Comparison**:
   - Live rates for PET Plastic, Cardboard, Aluminium, Iron, E-Waste, and Glass.
   - Side-by-side comparison with local scrap services (*Green Bhoomi*, *Namma Kailan Kadai*, *EcoWaste Direct*).
6. **Predictive Price Forecasting & Analytics**:
   - Interactive Chart.js visualizations showing 6-month historical collections + 3-month predictive ML demand curve and commodity scrap price trajectories.
7. **Cyber-Eco AI User Experience**:
   - Glassmorphic dark UI, animated neural network particle canvas, procedural audio sound effects (Web Audio API synthesizers), and instant one-click demo role switching.

---

## 🔑 User Roles & Pre-Seeded Credentials

| Portal Role | Demo Email | Password | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **🏠 Household** | `household@ecowaste.ai` | `user123` | AI Scanner, Tamil Voice Booking, Doorstep Pickup, Live GPS Tracking, Wallet Earnings, Green Certificate |
| **🏭 Recycler Hub** | `recycler@ecowaste.ai` | `recycler123` | Scrap Marketplace, Batch Bidding, Digital Weighing Station, Material Recovery Logger (Yield %) |
| **🛡️ Admin Control** | `admin@ecowaste.ai` | `admin123` | Ward Demand Clustering, Live Rate Card Editor, Pickup Dispatch Table, User Directory |

*(Note: You can also use the **"⚡ Quick Switch"** buttons in the navigation bar or login screen to jump into any role with zero typing!)*

---

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.10+ (Tested on Python 3.14)
- Web browser (Chrome, Edge, Firefox, or Safari)

### 2. Run the Application
Open PowerShell or Terminal in the project directory:
```bash
cd C:\Users\acer\.gemini\antigravity\scratch\ecowaste-smart-system
python app.py
```

### 3. Open in Browser
Navigate to:
```
http://localhost:5000
```
or
```
http://127.0.0.1:5000
```

---

## 📁 System Architecture
```
ecowaste-smart-system/
├── app.py                     # Flask application, REST APIs, SQLite DB models & seeders
├── ecowaste.db                # SQLite database (auto-generated)
├── requirements.txt           # Project dependencies
├── static/
│   ├── css/
│   │   └── style.css          # Futuristic cyber-eco styling & glassmorphism
│   ├── js/
│   │   ├── app.js             # Web Audio sound fx, neural particle canvas, voice assistant
│   │   ├── scanner.js         # Canvas-based AI bounding box vision classifier
│   │   ├── map.js             # Live GPS route visualizer & certificate generator
│   │   ├── charts.js          # Chart.js demand forecast & price trends
│   │   └── translations.js    # English & Tamil localization dictionary
│   └── samples/               # Pre-generated sample waste images for 1-click testing
│       ├── plastic_bottles.jpg
│       ├── cardboard_box.jpg
│       ├── metal_can.jpg
│       ├── ewaste_circuit.jpg
│       └── glass_bottle.jpg
└── templates/
    ├── base.html              # Cyber navbar, role switcher, system beacon, footer & modals
    ├── index.html             # Landing page, AI hero, scanner preview, live analytics
    ├── login.html             # Role-based sign in / registration gateway
    ├── household.html         # Household dashboard: Scanner, booking, tracking, wallet
    ├── recycler.html          # Recycler dashboard: Marketplace, weighing, recovery logger
    └── admin.html             # Admin dashboard: Rate card, route optimizer, user directory
```

