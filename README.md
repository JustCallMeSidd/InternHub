<div align="center">
  <img src="favicon.png" width="100" />
  <h1>InternHub AI</h1>
  <p><strong>A Premium AI-Powered Internship Matching Platform</strong></p>
</div>

---
<div align="center">
  <p><strong>🌐InternHub Ai Link </strong></p>
</div>

[https://github.com/user-attachments/assets/c8d2b2bc-3796-44c3-a868-96e1a55c55bb](https://internh.streamlit.app/)

---
<div align="center">
  <p><strong>🎬 Demo Video </strong></p>
</div>

https://github.com/user-attachments/assets/c8d2b2bc-3796-44c3-a868-96e1a55c55bb

---
## 🚀 About The Project

**InternHub AI Evaluator** is a cutting-edge Streamlit application designed to bridge the gap between students and internships. Using advanced Large Language Models (LLMs) via OpenRouter, it intelligently analyzes student resumes and internship job descriptions to provide a comprehensive match analysis.

### ✨ Key Features

-   **📄 Resume Parsing**: Automatically extracts skills, interests, and experience from PDF and TXT resumes.
-   **🤖 AI-Powered Matching**: Uses "Reasoning" LLMs to semantically match student profiles with job requirements.
-   **📊 Visual ATS Score**: Displays a beautiful, color-coded circular gauge representing the ATS confidence score (0-100%).
-   **🌓 Premium Dark Mode**: A sophisticated "blackish" dark theme with glassmorphism effects for a modern UI.
-   **🔒 Secure**: Uses environment variables for API keys and secure file handling.

## 🛠️ Built With

-   **[Streamlit](https://streamlit.io/)** - The fastest way to build data apps in Python.
-   **[OpenRouter](https://openrouter.ai/)** - Unified interface for top-tier LLMs.
-   **[Python](https://www.python.org/)** - Core programming language.
-   **PDFPlumber** - Robust PDF text extraction.
-   **Regex & JSON** - For structured data parsing and score extraction.

## 🏁 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

-   Python 3.8+
-   An API Key from [OpenRouter](https://openrouter.ai/)

### Installation

1.  **Clone the repository** (or download the files):
    ```sh
    git clone https://github.com/yourusername/InternHub.git
    cd InternHub
    ```

2.  **Create a virtual environment** (recommended):
    ```sh
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file in the root directory and add your OpenRouter key:
    ```env
    OPENROUTER_API_KEY=your_api_key_here
    OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
    MODEL_NAME=your_preferred_model_name
    ```

### ▶️ Running the App

Run the Streamlit application:
```sh
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

## 📂 Project Structure

```
e:\internHub\
├── .env                # API Keys & Configuration
├── app.py              # Main Streamlit Application
├── llm.py              # LLM Interface Logic
├── requirements.txt    # Python Dependencies
├── favicon.png         # Custom Logo
├── showcase.png        # App Showcase Image
├── prompts/            # System Prompts
│   ├── internship_match_prompt.py
│   └── resume_parser_prompt.py
└── utils/              # Helper Utilities
    └── resume_reader.py
```
Here’s a clean, professional version you can **directly add to your README**, written in clear product-quality language:

---

## ⚠️ Note on LLM API Availability

In rare cases, you may experience errors during usage due to **LLM API traffic, rate limits, or temporary service issues** from the model provider. This is expected behavior when using free or shared-tier APIs.

If you encounter any such issue, please **refer to the demo video linked in the README** to see the full working flow of the application.

🔒 **Important Notes**:

* These issues can be fully resolved by using a **paid, high-throughput LLM API plan**, which offers better reliability and speed.
* All API keys are securely managed using **Streamlit Secrets**, ensuring that sensitive credentials are never exposed in the codebase.

This design keeps the application **secure, scalable, and production-ready** when deployed with a premium API.

---

