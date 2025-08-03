# Chat with PDF

Ask questions from your PDF files using a conversational Gemini-powered chatbot built with Streamlit.

---

## ✨ Features

- Upload one or multiple PDF files  
- Convert into text → chunk → embed using Gemini  
- Store embeddings locally with FAISS  
- Ask questions and get context-based answers  

---

## 🔧 Installation

```bash
git clone <repo_url>
cd chat-with-pdf
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

Download your **service_account.json** from Google Cloud and update this line in `app.py`:

```python
Credentials.from_service_account_file("path/to/your/service_account.json")
```

---

## 🚀 Run

```bash
streamlit run app.py
```

---

## 📌 How to Use

1. Open the Streamlit sidebar → upload PDFs  
2. Click **Submit & Process**  
3. Ask questions in the input box  
4. Get answers fetched from the uploaded documents  

---

## 📦 Tech Stack

| Component          | Library                          |
|-------------------|-----------------------------------|
| UI                | Streamlit                         |
| PDF Parsing       | PyPDF2                            |
| Embeddings        | Google Generative AI (Gemini)     |
| Vector Store      | FAISS                             |
| LLM Orchestration | LangChain                         |

---

## 📁 File Structure

```
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .env                 # API key
└── service_account.json # Google credentials
```

---
