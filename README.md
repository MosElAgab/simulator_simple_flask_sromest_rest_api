# simulator_simple_flask_sromest_rest_api

This project is a simulator tool designed to generate test data for the [`simple_flask_sromest_rest_api`](https://github.com/MosElAgab/simple-flask-smorest-rest-api.git) REST API. It can simulate stores, items, and tags with fake data and automatically interact with the API via HTTP requests.

---

## 📦 Features

- ✅ Register and authenticate a user
- 🏪 Create fake **stores**
- 🛒 Create fake **items** for stores
- 🏷️ Create fake **tags** for stores
- 🔁 Simulate bulk creation of stores, items, and tags
- 🧪 Useful for testing and seeding your REST API

---

## 🧰 Requirements

- Python 3.8+
- `pip` or `venv`
- REST API server running (`simple_flask_sromest_rest_api`)

---

## 📁 Project Structure

```bash
.
├── README.md
├── item_simulator.py
├── query_base.py
├── requirements.txt
├── run_simulator.py
├── store_simulator.py
├── .env
├── .env.example
└── tag_simulator.py
```

---

## 🔧 Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/simulator_simple_flask_sromest_rest_api.git
   cd simulator_simple_flask_sromest_rest_api
   ```

---

## 🔧 Create venv
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

---

## 🔧 Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configure environment variables
   ```bash
   cp .env.example .env #check .env.example for further details
   ```

---
