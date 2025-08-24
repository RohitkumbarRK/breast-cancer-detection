@echo off
echo 🚀 Activating Breast Cancer Detection AI Environment
echo ================================================

echo 📋 Activating conda environment...
call conda activate breast_cancer_ai

echo 🔍 Checking Python version...
python --version

echo 🌐 Starting Streamlit application...
echo 📱 The app will open in your browser automatically
echo 🛑 Press Ctrl+C to stop the application

streamlit run src/app.py

pause