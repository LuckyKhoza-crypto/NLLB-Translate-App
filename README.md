# Translation Web App 🌍

This is a web-based translation application that allows users to translate text between various languages. Built using **Python (Flask)** for the backend and **Bootstrap** for the frontend, the app leverages **PyTorch**, **Hugging Face Transformers**, and the **Pipeline API** to deliver machine learning-powered translations using the **NLLB-200 model**.

---

## Features
- 🌐 Translate text between a wide range of languages.
- 🚀 User-friendly interface with Bootstrap design.
- 🎨 Dynamic language selection in plain English.
- 🔄 Loading animation to enhance the user experience during translation.
- 📦 Preloaded with NLLB-200 for high-quality translations.
- 💻 Powered by **PyTorch**, **Transformers**, and the **Pipeline API** for seamless machine learning integration.

---

## Requirements
Make sure you have the following installed:
- Python 3.8 or above
- `pip` (Python package manager)

### Python Libraries
Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## Setup and Run
### 1. Clone the repo
```bash
git clone https://github.com/yourusername/translation-app.git
cd translation-app
```

### 2. Initialize the Translation Model
The translation model will be initialized once when you start the app. This might take a few seconds as it loads the facebook/nllb-200-1.3B model.
```bash
python app.py
```

## Credits
- Frontend: Bootstrap
- Backend: Flask, Transformers Library
- Model: NLLB-200 by Meta AI
- Core Technologies: PyTorch, Hugging Face Pipelines


