Agentic Multi-Video Study Assistant with Fact-Checking & Q&A

An autonomous multi-agent system that turns one or more YouTube videos into synthesized, fact-checked study material — study notes, a publishable blog article, and a quiz — using LangGraph for agent orchestration and RAG for content retrieval.

Built as a B.Tech final-year project (AI & Data Science), Dr. N.G.P. Institute of Technology, Coimbatore.

What it does

Unlike single-video summarizer tools (Eightify, NoteGPT, Noiz), this system:

Handles multiple videos on the same topic and synthesizes one combined, deduplicated output instead of separate per-video summaries
Adapts its workflow to video type — a lecture/tutorial is processed differently from a podcast/review
Fact-checks claims made in the video against external web sources
Self-reviews its own output via a Critic Agent, regenerating content that doesn't meet quality criteria before finalizing
Produces an actual publishable blog post, not just bullet-point summaries
How it works
User submits 1–5 YouTube links (same topic)
          ↓
Transcript Extraction Agent
  (youtube-transcript-api → falls back to yt-dlp + Whisper if no captions)
          ↓
Content Analysis Agent
  (classifies each video: tutorial/lecture vs. podcast/review)
          ↓
Chunking + Embedding → Vector Store (ChromaDB)
          ↓
Router Agent (LangGraph)
    ↙                    ↓                    ↘
Study Notes Agent   Blog Writing Agent    Key-Insights Agent
Quiz Agent          (always runs;         Fact-Check Agent
                     synthesizes across
                     all input videos)
    ↘                    ↓                    ↙
              Critic Agent
    (checks draft against an accuracy/completeness/
     structure rubric; sends specific feedback back
     for regeneration — capped at 3 retries)
          ↓ (approved)
     Output Agent → Markdown/HTML
          ↓
   FastAPI backend (POST /process-videos)
          ↓
    Streamlit frontend
Tech stack
Layer	Tool
Agent orchestration	LangGraph
Transcript extraction	youtube-transcript-api, yt-dlp, openai-whisper
Vector store / RAG	ChromaDB
Fact-checking / web search	Tavily API
Backend	FastAPI
Frontend	Streamlit
LLM	TBD — see Open Items below
Project status
✅ Academic documentation complete (problem statement, objectives, SDG mapping, existing-system analysis, proposed methodology, system architecture)
✅ 15-week execution plan finalized (5 phases, Review 1 at Week 5, Review 2 at Week 10)
🔲 LLM selection — deciding between API-based (Claude/GPT) vs. local (Ollama/Llama 3)
🔲 Critic Agent rubric — concrete evaluation criteria and LangGraph feedback-loop implementation
🔲 Implementation — pipeline not yet built (see plan below)
15-week plan (summary)
Phase	Weeks	Focus
1. Foundations & Setup	1–3	Repo setup, LangGraph learning, transcript extraction, chunking/embedding
2. Core Agent Pipeline	4–7	Content classification, Router, Study Notes/Quiz/Blog/Key-Insights agents
3. Multi-Video, Fact-Check, Critique	8–11	Multi-video synthesis, Fact-Check Agent, Critic Agent + feedback loop
4. Full-Stack Integration	12–13	FastAPI backend, Streamlit frontend
5. Polish & Submission	14–15	Testing, evaluation metrics, final report, demo

Review 1 milestone: Week 5 (single-video pipeline working end-to-end). Review 2 milestone: Week 10 (multi-video, fact-checked, self-corrected pipeline working end-to-end).

Why this matters (SDG alignment)

Primarily mapped to SDG 4 — Quality Education: converts unstructured video content into structured, accessible study material, lowering the barrier to self-paced learning from freely available video resources. Secondary alignment with SDG 9 (applied AI innovation) and SDG 16 (access to verified information via fact-checking).

Getting started (once implementation begins)
bash
git clone <repo-url>
cd <repo-name>
pip install -r requirements.txt
# configure API keys (.env): LLM provider, Tavily
uvicorn app.main:app --reload      # start backend
streamlit run frontend/app.py      # start frontend
Team


References
Yao et al. (2023), ReAct: Synergizing Reasoning and Acting in Language Models, ICLR
Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, NeurIPS
LangGraph official documentation — https://langchain-ai.github.io/langgraph/
Radford et al. (2022), Robust Speech Recognition via Large-Scale Weak Supervision (Whisper), OpenAI
Douze et al. (2024), The FAISS Library, Meta AI Research

# 🎬 YouTube Chatbot AI

<div align="center">

![YouTube Chatbot AI](https://img.shields.io/badge/AI-Chatbot-red?style=for-the-badge&logo=youtube)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

**An AI-powered chatbot that lets you have conversations with any YouTube video.**  
Just paste a YouTube URL — ask anything about the video content!

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Environment Variables](#-environment-variables)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About the Project

**YouTube Chatbot AI** extracts transcripts from any YouTube video and uses a **RAG (Retrieval-Augmented Generation)** pipeline to answer questions based on the video content.

No more scrubbing through long videos — just **ask and get answers instantly!**

### How it works:
```
YouTube URL  →  Transcript Extraction  →  Chunking & Embedding
     →  Vector Store (FAISS/ChromaDB)  →  LLM (Gemini/OpenAI)  →  Answer
```

---

## ✨ Features

- 🔗 **Paste any YouTube URL** and start chatting
- 🤖 **AI-powered Q&A** using Gemini / OpenAI GPT
- 🧠 **Conversation Memory** — supports follow-up questions
- 📑 **Transcript Preview** — view the full video transcript
- ⚡ **Caching** — avoids re-processing the same video
- 🌍 **Multi-language** transcript support
- 🖥️ **Clean UI** built with Streamlit

---

## 🛠️ Tech Stack

| Layer          | Technology                          |
|----------------|-------------------------------------|
| Language       | Python 3.10+                        |
| AI/LLM         | Google Gemini / OpenAI GPT-4o       |
| RAG Framework  | LangChain                           |
| Embeddings     | Google Generative AI / OpenAI       |
| Vector Store   | FAISS / ChromaDB                    |
| Transcript API | youtube-transcript-api              |
| Frontend       | Streamlit                           |
| Version Control| Git + GitHub                        |

---

## 📁 Project Structure

```
Youtube_Chatbot_AI/
│
├── .env                    # API keys (DO NOT commit)
├── .gitignore              # Git ignore rules
├── PROJECT_PLAN.md         # Week-by-week development plan
├── README.md               # Project documentation (this file)
├── requirements.txt        # Python dependencies
│
├── src/
│   ├── transcript.py       # YouTube transcript extraction
│   ├── embeddings.py       # Embedding generation
│   ├── retriever.py        # Vector store & retrieval logic
│   ├── chatbot.py          # Chatbot logic & memory
│   └── utils.py            # Helper functions
│
├── frontend/
│   └── app.py              # Streamlit UI
│
├── tests/
│   ├── test_transcript.py
│   ├── test_chatbot.py
│   └── test_retriever.py
│
└── data/
    └── cache/              # Cached transcripts & embeddings
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip
- Git
- Google Gemini API Key **or** OpenAI API Key

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Youtube_Chatbot_AI.git
cd Youtube_Chatbot_AI
```

### Step 2 — Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up Environment Variables

Create a `.env` file in the root folder:

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here   # optional
```

### Step 5 — Run the Application

```bash
streamlit run frontend/app.py
```

Open your browser at: **http://localhost:8501**

---

## 🎮 Usage

1. **Open the app** in your browser
2. **Paste a YouTube URL** in the input field
3. **Click "Process Video"** — the transcript will be extracted
4. **Ask any question** about the video in the chat box
5. **Get instant AI-powered answers!**

### Example Questions:
```
"What is the main topic of this video?"
"Summarize the key points"
"What did the speaker say about X?"
"Give me the steps mentioned in the video"
```

---

## 🔐 Environment Variables

| Variable         | Description                  | Required |
|-----------------|------------------------------|----------|
| `GEMINI_API_KEY` | Google Gemini API Key        | ✅ Yes   |
| `OPENAI_API_KEY` | OpenAI API Key (alternative) | ⚠️ Optional |

> ⚠️ **Never commit your `.env` file to Git!** It is already listed in `.gitignore`.

---

## 📦 Requirements

```
langchain
langchain-google-genai
youtube-transcript-api
faiss-cpu
streamlit
python-dotenv
chromadb
tiktoken
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🗺️ Roadmap

- [x] Project setup & Git initialization
- [x] `.gitignore` and `PROJECT_PLAN.md`
- [ ] YouTube transcript extraction
- [ ] RAG pipeline with embeddings
- [ ] Chatbot with memory
- [ ] Streamlit UI
- [ ] Deployment (Streamlit Cloud / Render)
- [ ] Playlist support
- [ ] Export chat as PDF

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Karunakaran**  
📧 [your-email@example.com](mailto:karunakaranguru2006.com)  
🔗 [GitHub](https://github.com/Karuna212006)  

---

<div align="center">
⭐ If you found this project useful, please give it a star!
</div>
