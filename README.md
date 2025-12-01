# AI Question Answering App

A powerful, generative Question Answering application built with **FastAPI** and **Hugging Face Transformers**.
This app uses the **FLAN-T5** model to provide natural, summarized, and reasoning-based answers to your questions based on provided context.

## 🚀 Features
- **Generative QA**: Can summarize, reason, and explain answers (powered by `google/flan-t5-base`).
- **Modern UI**: Clean, dark-themed web interface for easy interaction.
- **FastAPI Backend**: High-performance API serving the model and static files.
- **Production Ready**: Structured project layout with tests and documentation.

## 📋 Prerequisites
- **Python 3.8+**
- **Pip**
- **Microsoft Visual C++ Redistributable** (for PyTorch/TensorFlow on Windows)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd qa_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ How to Run

1. **Start the Server**
   Run the following command from the project root:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 5000
   ```

2. **Access the App**
   Open your browser and navigate to:
   - **Local**: [http://localhost:5000/](http://localhost:5000/)
   - **Network**: `http://<your-lan-ip>:5000/`

## 🧪 Testing

We provide a dedicated `tests/` folder with scripts to verify the application.

### For Team Leader / QA (Rahul Sir)
👉 **[View the QA Testing Guide](QA_TESTING_GUIDE.md)** for a step-by-step verification scenario.

1. **Python Test**
   ```bash
   cd tests
   python test_api.py
   ```

2. **Curl Test**
   ```bash
   cd tests
   test_curl.bat
   ```

## 🧠 Model Selection
We experimented with several models before selecting **FLAN-T5**.
See [models_tried.md](models_tried.md) for a detailed log of our experiments, including why we moved away from DistilBERT and BERT-Large.

## 📂 Project Structure
```
qa_app/
├── app/
│   ├── main.py          # FastAPI application
│   ├── model_loader.py  # Model loading and inference logic
│   └── ui/              # Frontend files (index.html)
├── tests/               # Test scripts (Python, Curl)
├── docs/                # Additional documentation
├── models_tried.md      # Experimentation log
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 📞 Contact
**Owner**: Kaushik Chaturvedi
**GitHub**: [Link to Profile]
