---
description: Repository Information Overview
alwaysApply: true
---

# Breast Cancer Detection AI Assistant Information

## Summary
A comprehensive breast cancer detection system that combines machine learning for image classification with Google Gemini AI for intelligent health recommendations and user interaction. The project is designed for healthcare professionals to analyze mammography images, detect cancerous tissue, and provide AI-powered medical recommendations.

## Structure
- **src/**: Main application code including models, AI integration, and utilities
  - **models/**: ML models for classification (in development)
  - **ai/**: Gemini AI integration components
  - **utils/**: Utility functions including image validation
  - **app.py**: Main Streamlit application entry point
- **config/**: Configuration files and settings
- **data/**: Dataset storage and test images
- **uploads/**: Directory for user-uploaded images
- **logs/**: Application logs

## Language & Runtime
**Language**: Python
**Version**: 3.11+ (recommended for optimal AI performance)
**Build System**: pip
**Package Manager**: conda (environment) + pip (dependencies)

## Dependencies
**Main Dependencies**:
- tensorflow>=2.13.0 (Deep learning framework)
- google-generativeai>=0.8.0 (Google Gemini AI)
- streamlit>=1.28.0 (Web interface)
- opencv-python>=4.8.0 (Image processing)
- Pillow>=10.0.0 (Image handling)
- numpy>=1.24.0, pandas>=2.0.0 (Data processing)
- scikit-learn>=1.3.0 (Machine learning utilities)
- pydicom>=2.4.0, SimpleITK>=2.3.0 (Medical image processing)

**Development Dependencies**:
- pytest>=7.4.0 (Testing)
- jupyter>=1.0.0 (Development notebooks)

## Build & Installation
```bash
# Automated setup (recommended)
python setup_environment.py

# Manual setup
conda create -n breast_cancer_ai python=3.11 -y
conda activate breast_cancer_ai
pip install -r requirements.txt
```

## Usage & Operations
**Running the Application**:
```bash
# Development mode
conda activate breast_cancer_ai
streamlit run src/app.py

# Production mode
conda activate breast_cancer_ai
streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0
```

**API Configuration**:
1. Get Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Copy `.env.example` to `.env`
3. Add API key: `GOOGLE_API_KEY=your_key_here`

## Testing
**Framework**: pytest
**Test Files**: 
- test_validator.py (Tests AI image validation)
- test_real_images.py (Tests with real mammography images)

**Run Command**:
```bash
# Run specific test
python test_validator.py

# Run all tests with pytest
pytest
```

## Development Status
- ✅ Project setup and foundation (completed)
- 🔄 AI Image Validation (in progress)
- ⏳ Cancer Classification (planned)
- ⏳ Gemini AI Integration (planned)
- ⏳ Professional Interface (planned)

## Performance Targets
- **AI Accuracy**: >95% for image validation, >90% sensitivity for cancer detection
- **Response Time**: <3 seconds for image analysis
- **Memory Usage**: <4GB RAM during operation
- **Confidence Threshold**: 0.75 (75%) for medical decisions