# 🧠 Experience Extraction from Job Descriptions using LangChain + ChatGroq

This Streamlit app extracts **experience requirements** from job descriptions using a Generative AI model (ChatGroq via LangChain). It identifies either total required experience or per-skill experience if total isn't mentioned.

---

## 🚀 Features

- Extracts total or per-skill experience from job descriptions.
- Built using Streamlit and LangChain.
- Uses Groq's `ChatGroq` LLM model (compound-beta-mini).
- Clean, simple UI with Groq API key integration.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq LLM (via `langchain_groq`)

---

## 📦 Installation & Local Setup

### 1. Clone this repository


    git clone https://github.com/your-username/experience-extractor.git
    
    cd experience-extractor


### 2. Install the requirements

    pip install -r requirements.txt

### 3. 🔑 Groq API Key Setup

- Visit Groq Console.

- Generate an API key.

- Paste the key into the sidebar of the Streamlit app when prompted.

### 4. ▶️ Running the App

        streamlit run app.py

### ✍️ Example Job Description Input

    We are looking for a backend engineer with 5+ years of experience in total. Experience with Python (3+ years), Docker (2 years), and AWS (2-3 years) is a plus.
### Expected Output (if total experience is mentioned):
    experience: 5+ years

### Expected Output (if no total experience is mentioned):

    experience_by_skill:
        - Python: 3+ years
        - Docker: 2 years
        - AWS: 2-3 years


