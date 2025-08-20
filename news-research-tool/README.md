# 📈 News Research Tool  

This is a **Streamlit-based research assistant** that:  
- Fetches and processes news articles from URLs.  
- Splits text into chunks for better context understanding.  
- Builds a **FAISS vector store** using **Google Gemini embeddings**.  
- Lets you **ask questions** about the articles with **retrieval-augmented generation (RAG)**.  

---

## 🚀 Features
- Enter up to 3 news article URLs.  
- Automatically load, clean, and split the content.  
- Build embeddings with **Google Generative AI**.  
- Store vectors locally with **FAISS**.  
- Ask natural language questions and get contextual answers with sources.  

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/news-research-tool.git
   cd news-research-tool
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Environment Setup  

1. Create a `.env` file in the project root.  
2. Add your **Google Gemini API Key**:  

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

---

## ▶️ Running the App  

Start the Streamlit app with:  

```bash
streamlit run main.py
```

Then open the link in your browser (usually `http://localhost:8501`).  

---

## 🖥️ Usage  

1. Enter up to 3 news article URLs in the sidebar.  
2. Click **"Process URLs"** to fetch and embed the data.  
3. Enter your **question** in the input box.  
4. Get an **AI-generated answer** along with **sources**.  

---

## 📁 Project Structure  

```
news-research-tool/
│── main.py               # Streamlit application
│── requirements.txt      # Python dependencies
│── .env                  # API key (ignored in git)
│── README.md             # Documentation
│── faiss_index_gemini/   # Local FAISS vector store (auto-created)
```

---

## ⚠️ Notes  

- `allow_dangerous_deserialization=True` is required in `FAISS.load_local()` due to LangChain’s new security check.  
  This is safe because you’re loading your **own locally created FAISS index**.  
- If you face issues, delete the `faiss_index_gemini/` folder and rebuild by reprocessing the URLs.  

---
news articles
  - https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html
  - https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html
  - https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html

