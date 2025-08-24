"""
Configuration settings for Breast Cancer Detection System
Professional medical application for healthcare providers
"""

import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "src" / "models"
UPLOADS_DIR = BASE_DIR / "uploads"

# Application settings
APP_CONFIG = {
    "title": "Breast Cancer Detection AI Assistant",
    "subtitle": "Professional Medical Image Analysis System",
    "version": "1.0.0",
    "developer": "Medical AI Solutions",
    "target_users": "Healthcare Professionals"
}

# Model configuration
MODEL_CONFIG = {
    "input_shape": (224, 224, 3),  # Standard for medical image analysis
    "batch_size": 32,
    "epochs": 50,
    "learning_rate": 0.001,
    "confidence_threshold": 0.75,  # Higher threshold for medical applications
    "model_name": "breast_cancer_classifier.h5"
}

# Image processing settings
IMAGE_CONFIG = {
    "supported_formats": [".jpg", ".jpeg", ".png", ".dcm", ".dicom"],
    "max_file_size": 50 * 1024 * 1024,  # 50MB for high-res medical images
    "target_size": (224, 224),
    "preprocessing": {
        "normalize": True,
        "augmentation": True,
        "noise_reduction": True
    }
}

# Gemini AI configuration
GEMINI_CONFIG = {
    "model_name": "gemini-pro",
    "temperature": 0.3,  # Lower temperature for medical accuracy
    "max_tokens": 1000,
    "safety_settings": "high",  # Maximum safety for medical content
    "medical_context": True
}

# Classification labels
CLASSIFICATION_LABELS = {
    0: {
        "label": "Non-Cancerous",
        "description": "No malignant tissue detected",
        "color": "#28a745",  # Green
        "recommendation": "Continue regular screening"
    },
    1: {
        "label": "Cancerous",
        "description": "Potential malignant tissue detected",
        "color": "#dc3545",  # Red
        "recommendation": "Immediate further evaluation required"
    }
}

# Medical recommendations framework
MEDICAL_FRAMEWORK = {
    "risk_factors": [
        "Age", "Family history", "Genetic mutations (BRCA1/BRCA2)",
        "Personal history", "Lifestyle factors", "Hormonal factors"
    ],
    "screening_guidelines": {
        "age_40_49": "Annual mammography (individualized)",
        "age_50_74": "Biennial mammography recommended",
        "high_risk": "Enhanced screening with MRI"
    },
    "follow_up_protocols": {
        "normal": "Continue routine screening",
        "benign": "Short-term follow-up in 6 months",
        "suspicious": "Immediate biopsy recommended",
        "malignant": "Urgent oncology referral"
    }
}

# Database configuration for progress tracking
DATABASE_CONFIG = {
    "name": "breast_cancer_tracking.db",
    "tables": {
        "patients": ["id", "name", "age", "risk_factors", "created_date"],
        "scans": ["id", "patient_id", "image_path", "prediction", "confidence", "scan_date"],
        "reports": ["id", "patient_id", "scan_id", "ai_analysis", "recommendations", "report_date"]
    }
}

# Logging configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/medical_app.log",
    "max_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5
}

# Security and compliance
SECURITY_CONFIG = {
    "data_encryption": True,
    "audit_logging": True,
    "session_timeout": 30,  # minutes
    "max_login_attempts": 3,
    "hipaa_compliance": True,
    "data_retention_days": 2555  # 7 years as per medical standards
}

# Create necessary directories
def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [DATA_DIR, MODELS_DIR, UPLOADS_DIR, BASE_DIR / "logs"]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    create_directories()
    print("Configuration loaded successfully!")
    print(f"Base directory: {BASE_DIR}")
    print(f"Application: {APP_CONFIG['title']} v{APP_CONFIG['version']}")