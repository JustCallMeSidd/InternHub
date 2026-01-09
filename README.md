# 🧩 InternHub AI Evaluator
![showcase](https://github.com/user-attachments/assets/97c35006-4f9a-4d94-aa17-93ee86903ecf)

<div align="center">
  <img src="favicon.png" width="100" />
  <h1>InternHub AI</h1>
  <p><strong>A Premium AI-Powered Internship Matching Platform</strong></p>
</div>

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

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Review the `task.md` for upcoming features.
3.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
4.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5.  Push to the Branch (`git push origin feature/AmazingFeature`)
6.  Open a Pull Request

---
<div align="center">
  <p>Powered by <strong>InternHub AI</strong> | OpenRouter</p>
</div>
