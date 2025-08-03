Chat with PDF
Ask questions from your PDF files like you’re chatting with them — powered by Google Gemini, LangChain, and Streamlit.

✨ Features
Upload one or multiple PDF files

Automatically chunks and embeds text using Gemini embeddings

Stores embeddings using FAISS for fast retrieval

Ask free-form questions and get context-aware answers

Built with a simple Streamlit interface

🛠️ Installation
Clone the repo:

bash
Copy
Edit
git clone <repo_url>
cd chat-with-pdf
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Set up Google credentials:

Create a .env file with your Google API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
Download your Service Account JSON file from Google Cloud and update its path in the script at:

python
Copy
Edit
Credentials.from_service_account_file("path/to/your/service_account.json")
🚀 Launch the App
bash
Copy
Edit
streamlit run app.py
📌 How to Use
Open the Streamlit sidebar → upload PDF files.

Click Submit & Process to embed and index your documents.

In the main chat box, type your question related to the uploaded PDFs.

Receive answers sourced directly from your documents.

📚 Tech Stack
Component	Library
UI	Streamlit
PDF Parsing	PyPDF2
Embeddings	Google Generative AI (Gemini)
Vector Store	FAISS
LLM Orchestration	LangChain

🔧 File Structure
bash
Copy
Edit
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .env                 # API key
└── service_account.json 
