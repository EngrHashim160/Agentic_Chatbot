# LangGraph Agentic Chatbot (End‑to‑End)

A production‑ready, **Streamlit** app that demonstrates **agentic AI** patterns with **LangGraph** and **LangChain**, powered by **Groq LLMs** and **Tavily** search. It includes multiple graphs (Basic Chatbot, Web‑augmented Chatbot, and AI News summarizer) behind a polished UI, with markdown exports.

---

## ✨ Use Cases
- **Basic Chatbot** — straight LLM conversational agent.
- **Chatbot with Web** — tool‑augmented agent that can search the web (Tavily) before answering.
- **AI News** — fetches AI news (Daily/Weekly/Monthly), summarizes with the LLM, and writes a markdown report to `AINews/<frequency>_summary.md` which is rendered inside the app.

---

## 🧱 Architecture
- **UI:** `streamlit` app (`Agentic_chatbot/app.py`) that calls `load_langgraph_agenticai_app()`.
- **Graphs:** `src/langgraphAgenticAi/graph/graph_builder.py` builds `StateGraph` variants per use case.
- **Nodes:** modular behaviors in `src/langgraphAgenticAi/nodes/` (basic chatbot, tool‑augmented, AI news).
- **Tools:** `src/langgraphAgenticAi/tools/search_tools.py` exposes Tavily search via LangGraph `ToolNode`.
- **Config:** `src/langgraphAgenticAi/ui/uiConfigUI.ini` controls page title, model and use‑case lists.

---

## 📦 Project Layout
```
Agentic_chatbot/
├── app.py
├── requirements.txt
└── src/langgraphAgenticAi/
    ├── main.py
    ├── graph/graph_builder.py
    ├── nodes/
    │   ├── basic_chatbot_node.py
    │   ├── chatbot_with_Tool_node.py
    │   └── ai_news_node.py
    ├── tools/search_tools.py
    ├── state/state.py
    └── ui/
        ├── streamlitui/loadUI.py
        ├── streamlitui/displayResult.py
        ├── uiConfigUI.ini
        └── uiConfigfile.py
```

---

## ⚙️ Requirements
See `Agentic_chatbot/requirements.txt`:
```
langchain
langgraph
langchain_community
langchain_core
langchain_groq
langchain_openai
faiss-cpu
streamlit
tavily-python
```
> Note: Only Groq + Tavily are required at runtime for the included graphs.

---

## 🔐 Environment Variables
Set the following before running (e.g., via `.env` or your shell):
```bash
export GROQ_API_KEY="your_groq_key"
export TAVILY_API_KEY="your_tavily_key"
```
The app also lets you paste keys in the sidebar controls.

---

## 🏃‍♀️ Run Locally
1) Create and activate a virtual environment (recommended).
2) Install deps:
```bash
pip install -r Agentic_chatbot/requirements.txt
```
3) Launch Streamlit:
```bash
streamlit run Agentic_chatbot/app.py
```
4) Open the browser link Streamlit prints (usually http://localhost:8501).

---

## 🖥️ Using the App
- Choose **LLM** (Groq) and model (e.g., `llama3-8b-8192`) in the sidebar.
- Pick a **Use Case**:
  - *Basic Chatbot*: enter a message and submit.
  - *Chatbot with Web*: enter a message; the agent may call Tavily tools.
  - *AI News*: choose *Daily*, *Weekly*, or *Monthly*, then **Fetch Latest AI News**.
- Results stream in the center panel; AI News also saves a markdown file under `AINews/` and renders it.

---

## 🧪 Extending
- Add nodes in `src/langgraphAgenticAi/nodes/` and register them in `graph_builder.py`.
- Add tools in `src/langgraphAgenticAi/tools/` and wire them via `create_tool_node()`.
- Edit UI choices in `src/langgraphAgenticAi/ui/uiConfigUI.ini`.

---

## 🛠 Troubleshooting
- **Keys not found**: ensure `GROQ_API_KEY`/`TAVILY_API_KEY` are set or entered in the sidebar.
- **Streamlit import errors**: verify the virtual environment and that `pip install -r requirements.txt` completed.
- **No news output**: confirm your Tavily key and internet access; check `AINews/<frequency>_summary.md`.

---

## 📄 License
MIT
