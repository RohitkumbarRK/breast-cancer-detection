"""
Environment Setup Script for Breast Cancer Detection AI Project
Automated setup for Python 3.11 environment with all dependencies
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}:")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Breast Cancer Detection AI Project Environment")
    print("=" * 60)
    
    # Check if we're in the right directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    print(f"📁 Project directory: {project_root}")
    
    # Step 1: Create new conda environment with Python 3.11
    print("\n📋 Step 1: Creating Python 3.11 Environment")
    if not run_command(
        "conda create -n breast_cancer_ai python=3.11 -y",
        "Creating conda environment 'breast_cancer_ai'"
    ):
        print("❌ Failed to create environment. Please run manually:")
        print("conda create -n breast_cancer_ai python=3.11 -y")
        return False
    
    # Step 2: Activate environment and install dependencies
    print("\n📋 Step 2: Installing Dependencies")
    
    # For Windows, we need to use conda run to execute in the environment
    install_commands = [
        ("conda run -n breast_cancer_ai pip install --upgrade pip", "Upgrading pip"),
        ("conda run -n breast_cancer_ai pip install streamlit", "Installing Streamlit"),
        ("conda run -n breast_cancer_ai pip install tensorflow", "Installing TensorFlow"),
        ("conda run -n breast_cancer_ai pip install google-generativeai", "Installing Google Gemini AI"),
        ("conda run -n breast_cancer_ai pip install opencv-python", "Installing OpenCV"),
        ("conda run -n breast_cancer_ai pip install Pillow", "Installing Pillow"),
        ("conda run -n breast_cancer_ai pip install numpy pandas scikit-learn", "Installing core ML libraries"),
        ("conda run -n breast_cancer_ai pip install matplotlib seaborn plotly", "Installing visualization libraries"),
        ("conda run -n breast_cancer_ai pip install python-dotenv requests", "Installing utilities"),
    ]
    
    for command, description in install_commands:
        if not run_command(command, description):
            print(f"⚠️ Warning: {description} failed. You may need to install manually.")
    
    # Step 3: Verify installation
    print("\n📋 Step 3: Verifying Installation")
    verification_script = '''
import sys
print(f"Python version: {sys.version}")
try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("❌ TensorFlow not installed")

try:
    import streamlit as st
    print(f"Streamlit version: {st.__version__}")
except ImportError:
    print("❌ Streamlit not installed")

try:
    import google.generativeai as genai
    print("✅ Google Gemini AI available")
except ImportError:
    print("❌ Google Gemini AI not installed")

try:
    import cv2
    print(f"OpenCV version: {cv2.__version__}")
except ImportError:
    print("❌ OpenCV not installed")

print("\\n🎉 Environment verification completed!")
'''
    
    with open("verify_setup.py", "w") as f:
        f.write(verification_script)
    
    run_command(
        "conda run -n breast_cancer_ai python verify_setup.py",
        "Verifying installation"
    )
    
    # Step 4: Instructions
    print("\n" + "=" * 60)
    print("🎉 SETUP COMPLETED!")
    print("=" * 60)
    print("\n📋 Next Steps:")
    print("1. Activate the environment:")
    print("   conda activate breast_cancer_ai")
    print("\n2. Run the application:")
    print("   streamlit run src/app.py")
    print("\n3. Get your Google Gemini API key:")
    print("   - Visit: https://makersuite.google.com/app/apikey")
    print("   - Create API key")
    print("   - Copy .env.example to .env")
    print("   - Add your API key to .env file")
    print("\n🔧 Environment Details:")
    print("   - Environment name: breast_cancer_ai")
    print("   - Python version: 3.11")
    print("   - AI Framework: TensorFlow + Google Gemini")
    print("   - Web Interface: Streamlit")
    print("\n⚠️ Important:")
    print("   - Always activate the environment before working")
    print("   - This is a medical AI system - use responsibly")
    print("   - For educational purposes only")
    
    # Clean up
    if os.path.exists("verify_setup.py"):
        os.remove("verify_setup.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ Setup completed successfully!")
    else:
        print("\n❌ Setup encountered errors. Please check the messages above.")
        sys.exit(1)