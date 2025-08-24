# breast-cancer-detection

A comprehensive breast cancer detection system that combines machine learning for image classification with Google Gemini AI for intelligent health recommendations and user interaction.

## Features (Planned)
- 🔬 Breast cancer image classification (cancerous vs non-cancerous)
- 🤖 AI-powered health recommendations using Google Gemini
- 📊 Progress visualization and tracking
- 💬 Interactive AI chat for health guidance
- 📈 Risk assessment and prevention suggestions

## Project Structure
```
breast-cancer-detection/
├── src/
│   ├── models/          # ML models for classification
│   ├── ai/              # Gemini AI integration
│   ├── utils/           # Utility functions
│   └── app.py           # Main Streamlit application
├── data/                # Dataset storage
├── requirements.txt     # Python dependencies
└── config/              # Configuration files
```

## Development Status
- [x] Project setup
- [ ] Basic ML model for classification
- [ ] Gemini AI integration
- [ ] Streamlit web interface
- [ ] Progress visualization
- [ ] Testing and optimization

## Getting Started

### 🚀 Quick Setup (Recommended)
1. **Automated Setup**: `python setup_environment.py`
2. **Activate Environment**: `conda activate breast_cancer_ai`
3. **Run Application**: `streamlit run src/app.py`

### 🔧 Manual Setup
1. **Create Environment**: `conda create -n breast_cancer_ai python=3.11 -y`
2. **Activate Environment**: `conda activate breast_cancer_ai`
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Run Application**: `streamlit run src/app.py`

### 🎯 System Requirements
- **Python**: 3.11+ (recommended for optimal AI performance)
- **Memory**: 8GB+ RAM (for TensorFlow and AI models)
- **Storage**: 2GB+ free space
- **Internet**: Required for Google Gemini AI API

### 🔑 API Setup
1. Get Google Gemini API key: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Copy `.env.example` to `.env`
3. Add your API key: `GOOGLE_API_KEY=your_key_here`

---
*This project is for educational purposes and should not replace professional medical advice.*