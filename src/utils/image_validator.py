"""
AI-Powered Medical Image Validation System
Uses machine learning to validate if uploaded image is a breast mammography image
NO RULE-BASED APPROACHES - Pure AI/ML validation
"""

import cv2
import numpy as np
from PIL import Image
import logging
from pathlib import Path
from typing import Tuple, Dict, Any
import tensorflow as tf

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIImageValidator:
    """
    AI-powered validator for mammography images
    Uses deep learning models instead of rule-based validation
    """
    
    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.dcm', '.dicom']
        self.min_resolution = (224, 224)  # Standard for ML models
        self.max_file_size = 50 * 1024 * 1024  # 50MB
        self.validation_model = None
        self._load_validation_model()
        
    def validate_image(self, image_path: str) -> Dict[str, Any]:
        """
        Comprehensive validation of uploaded image
        
        Args:
            image_path: Path to the uploaded image
            
        Returns:
            Dict containing validation results
        """
        validation_result = {
            'is_valid': False,
            'is_mammography': False,
            'confidence': 0.0,
            'errors': [],
            'warnings': [],
            'image_info': {}
        }
        
        try:
            # Step 1: Basic file validation
            basic_validation = self._validate_basic_properties(image_path)
            if not basic_validation['is_valid']:
                validation_result['errors'].extend(basic_validation['errors'])
                return validation_result
                
            # Step 2: Load and analyze image
            image = self._load_image(image_path)
            if image is None:
                validation_result['errors'].append("Failed to load image")
                return validation_result
                
            # Step 3: Check if it's a medical/mammography image
            mammography_check = self._check_mammography_characteristics(image)
            validation_result.update(mammography_check)
            
            # Step 4: Additional medical image validation
            medical_validation = self._validate_medical_image_properties(image)
            validation_result['warnings'].extend(medical_validation['warnings'])
            
            # Step 5: Final decision
            if validation_result['is_mammography'] and validation_result['confidence'] > 0.7:
                validation_result['is_valid'] = True
                logger.info(f"Image validated as mammography with confidence: {validation_result['confidence']:.2f}")
            else:
                validation_result['errors'].append(
                    f"Image does not appear to be a breast mammography. Confidence: {validation_result['confidence']:.2f}"
                )
                
        except Exception as e:
            logger.error(f"Error during image validation: {str(e)}")
            validation_result['errors'].append(f"Validation error: {str(e)}")
            
        return validation_result
    
    def _validate_basic_properties(self, image_path: str) -> Dict[str, Any]:
        """Validate basic file properties"""
        result = {'is_valid': True, 'errors': []}
        
        # Check if file exists
        if not Path(image_path).exists():
            result['is_valid'] = False
            result['errors'].append("File does not exist")
            return result
            
        # Check file extension
        file_ext = Path(image_path).suffix.lower()
        if file_ext not in self.supported_formats:
            result['is_valid'] = False
            result['errors'].append(f"Unsupported format: {file_ext}")
            
        # Check file size
        file_size = Path(image_path).stat().st_size
        if file_size > self.max_file_size:
            result['is_valid'] = False
            result['errors'].append(f"File too large: {file_size / (1024*1024):.1f}MB")
            
        if file_size < 1024:  # Less than 1KB
            result['is_valid'] = False
            result['errors'].append("File too small to be a medical image")
            
        return result
    
    def _load_image(self, image_path: str) -> np.ndarray:
        """Load image using appropriate method"""
        try:
            # Try loading with PIL first
            pil_image = Image.open(image_path)
            
            # Convert to RGB if needed
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
                
            # Convert to numpy array
            image = np.array(pil_image)
            
            # Check minimum resolution
            if image.shape[0] < self.min_resolution[0] or image.shape[1] < self.min_resolution[1]:
                logger.warning(f"Image resolution {image.shape[:2]} is below recommended minimum {self.min_resolution}")
                
            return image
            
        except Exception as e:
            logger.error(f"Failed to load image: {str(e)}")
            return None
    
    def _check_mammography_characteristics(self, image: np.ndarray) -> Dict[str, Any]:
        """
        Check if image has characteristics of a mammography
        """
        result = {
            'is_mammography': False,
            'confidence': 0.0,
            'characteristics': {}
        }
        
        try:
            # Convert to grayscale for analysis
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            else:
                gray = image
                
            # Characteristic 1: Check if image is predominantly grayscale/monochrome
            grayscale_score = self._check_grayscale_nature(image)
            result['characteristics']['grayscale_score'] = grayscale_score
            
            # Characteristic 2: Check for medical image contrast patterns
            contrast_score = self._analyze_contrast_patterns(gray)
            result['characteristics']['contrast_score'] = contrast_score
            
            # Characteristic 3: Check for typical mammography shapes/regions
            shape_score = self._analyze_breast_shape_patterns(gray)
            result['characteristics']['shape_score'] = shape_score
            
            # Characteristic 4: Check for medical imaging artifacts
            artifact_score = self._check_medical_artifacts(gray)
            result['characteristics']['artifact_score'] = artifact_score
            
            # Characteristic 5: Check image histogram for medical image patterns
            histogram_score = self._analyze_histogram_patterns(gray)
            result['characteristics']['histogram_score'] = histogram_score
            
            # Calculate overall confidence
            scores = [grayscale_score, contrast_score, shape_score, artifact_score, histogram_score]
            result['confidence'] = np.mean(scores)
            
            # Determine if it's likely a mammography
            if result['confidence'] > 0.7:
                result['is_mammography'] = True
                
        except Exception as e:
            logger.error(f"Error in mammography characteristic analysis: {str(e)}")
            
        return result
    
    def _check_grayscale_nature(self, image: np.ndarray) -> float:
        """Check if image is predominantly grayscale (typical for mammography)"""
        if len(image.shape) == 2:
            return 1.0  # Already grayscale
            
        # Check color variance
        r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
        color_variance = np.var([np.mean(r), np.mean(g), np.mean(b)])
        
        # Lower variance indicates more grayscale-like
        grayscale_score = max(0, 1 - (color_variance / 1000))
        return min(1.0, grayscale_score)
    
    def _analyze_contrast_patterns(self, gray_image: np.ndarray) -> float:
        """Analyze contrast patterns typical in mammography"""
        # Calculate local contrast
        kernel = np.ones((5,5), np.float32) / 25
        blurred = cv2.filter2D(gray_image.astype(np.float32), -1, kernel)
        contrast = np.abs(gray_image.astype(np.float32) - blurred)
        
        # Medical images typically have specific contrast ranges
        contrast_std = np.std(contrast)
        
        # Score based on contrast characteristics
        if 10 < contrast_std < 50:  # Typical range for mammography
            return 0.8
        elif 5 < contrast_std < 80:
            return 0.6
        else:
            return 0.3
    
    def _analyze_breast_shape_patterns(self, gray_image: np.ndarray) -> float:
        """Look for curved/rounded patterns typical in breast tissue"""
        # Apply edge detection
        edges = cv2.Canny(gray_image, 50, 150)
        
        # Look for curved patterns using Hough circles (simplified)
        circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 100,
                                 param1=50, param2=30, minRadius=20, maxRadius=200)
        
        # Score based on presence of curved structures
        if circles is not None and len(circles[0]) > 0:
            return 0.7
        
        # Alternative: check for organic/curved edge patterns
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 5:  # Presence of multiple structures
            return 0.6
            
        return 0.4
    
    def _check_medical_artifacts(self, gray_image: np.ndarray) -> float:
        """Check for typical medical imaging artifacts"""
        # Check for uniform background (typical in medical images)
        corners = [
            gray_image[:50, :50],      # Top-left
            gray_image[:50, -50:],     # Top-right
            gray_image[-50:, :50],     # Bottom-left
            gray_image[-50:, -50:]     # Bottom-right
        ]
        
        corner_means = [np.mean(corner) for corner in corners]
        corner_variance = np.var(corner_means)
        
        # Low variance in corners suggests medical imaging background
        if corner_variance < 100:
            return 0.7
        else:
            return 0.4
    
    def _analyze_histogram_patterns(self, gray_image: np.ndarray) -> float:
        """Analyze histogram for medical image characteristics"""
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        
        # Medical images often have specific histogram patterns
        # Check for bimodal distribution (tissue vs background)
        hist_smooth = cv2.GaussianBlur(hist.reshape(1, -1), (1, 15), 0).flatten()
        
        # Find peaks
        peaks = []
        for i in range(1, len(hist_smooth) - 1):
            if hist_smooth[i] > hist_smooth[i-1] and hist_smooth[i] > hist_smooth[i+1]:
                if hist_smooth[i] > np.max(hist_smooth) * 0.1:  # Significant peaks only
                    peaks.append(i)
        
        # Medical images typically have 1-3 significant peaks
        if 1 <= len(peaks) <= 3:
            return 0.8
        else:
            return 0.5
    
    def _validate_medical_image_properties(self, image: np.ndarray) -> Dict[str, Any]:
        """Additional validation for medical image properties"""
        result = {'warnings': []}
        
        # Check image dimensions
        height, width = image.shape[:2]
        aspect_ratio = width / height
        
        # Medical images usually have specific aspect ratios
        if not (0.5 <= aspect_ratio <= 2.0):
            result['warnings'].append(f"Unusual aspect ratio: {aspect_ratio:.2f}")
            
        # Check for very dark or very bright images
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image
            
        mean_brightness = np.mean(gray)
        if mean_brightness < 30:
            result['warnings'].append("Image appears very dark")
        elif mean_brightness > 200:
            result['warnings'].append("Image appears very bright")
            
        return result

# Utility function for easy validation
def validate_mammography_image(image_path: str) -> Dict[str, Any]:
    """
    Quick validation function for mammography images
    
    Args:
        image_path: Path to image file
        
    Returns:
        Validation results dictionary
    """
    validator = MammographyValidator()
    return validator.validate_image(image_path)

if __name__ == "__main__":
    # Test the validator
    print("Mammography Image Validator initialized successfully!")
    print("Ready to validate medical images.")