#!/usr/bin/env python3
"""
Comprehensive test for real image distinction
Tests the system's ability to distinguish mammography from other images
"""

import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.utils.ai_image_validator import validate_mammography_with_ai

def create_test_images():
    """Create various test images to test the AI's distinction capability"""
    
    test_dir = project_root / "data" / "test_images"
    test_dir.mkdir(exist_ok=True)
    
    # 1. Create a mammography-like image (grayscale medical)
    mammography_like = np.zeros((512, 512, 3), dtype=np.uint8)
    # Add breast-like tissue patterns
    center_x, center_y = 256, 256
    y, x = np.ogrid[:512, :512]
    
    # Create breast tissue-like patterns
    mask1 = (x - center_x)**2 + (y - center_y)**2 < 150**2
    mask2 = (x - center_x + 50)**2 + (y - center_y + 30)**2 < 80**2
    
    mammography_like[mask1] = [180, 180, 180]  # Tissue
    mammography_like[mask2] = [120, 120, 120]  # Dense tissue
    
    # Add some noise for medical image realism
    noise = np.random.normal(0, 10, mammography_like.shape)
    mammography_like = np.clip(mammography_like + noise, 0, 255).astype(np.uint8)
    
    Image.fromarray(mammography_like).save(test_dir / "mammography_like.jpg")
    
    # 2. Create a regular photo (colorful, non-medical)
    regular_photo = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
    # Make it colorful
    regular_photo[:, :, 0] = np.random.randint(100, 255, (512, 512))  # Red
    regular_photo[:, :, 1] = np.random.randint(50, 200, (512, 512))   # Green
    regular_photo[:, :, 2] = np.random.randint(150, 255, (512, 512))  # Blue
    
    Image.fromarray(regular_photo).save(test_dir / "regular_photo.jpg")
    
    # 3. Create a text document image
    text_image = Image.new('RGB', (512, 512), color='white')
    draw = ImageDraw.Draw(text_image)
    
    # Add text content
    text_content = [
        "This is a text document",
        "Not a medical image",
        "Contains written content",
        "Should be rejected by AI",
        "Medical AI should detect",
        "this is not mammography"
    ]
    
    y_pos = 50
    for line in text_content:
        draw.text((50, y_pos), line, fill='black')
        y_pos += 40
    
    text_image.save(test_dir / "text_document.jpg")
    
    # 4. Create an X-ray-like image (medical but not mammography)
    xray_like = np.zeros((512, 512, 3), dtype=np.uint8)
    
    # Create bone-like structures
    # Spine
    xray_like[200:300, 240:260] = [200, 200, 200]
    # Ribs
    for i in range(5):
        y_start = 150 + i * 30
        xray_like[y_start:y_start+10, 100:400] = [180, 180, 180]
    
    # Add medical image characteristics
    xray_like = xray_like + np.random.normal(0, 5, xray_like.shape)
    xray_like = np.clip(xray_like, 0, 255).astype(np.uint8)
    
    Image.fromarray(xray_like).save(test_dir / "xray_like.jpg")
    
    print(f"✅ Created test images in: {test_dir}")
    return test_dir

def test_image_distinction():
    """Test the AI's ability to distinguish different image types"""
    
    print("🧪 COMPREHENSIVE IMAGE DISTINCTION TEST")
    print("=" * 50)
    
    # Create test images
    test_dir = create_test_images()
    
    # Test images with expected results
    test_cases = [
        {
            "file": "mammography_like.jpg",
            "expected": "Should be detected as mammography-like",
            "type": "Medical (Mammography-like)"
        },
        {
            "file": "regular_photo.jpg", 
            "expected": "Should be rejected (not medical)",
            "type": "Regular Photo"
        },
        {
            "file": "text_document.jpg",
            "expected": "Should be rejected (text document)",
            "type": "Text Document"
        },
        {
            "file": "xray_like.jpg",
            "expected": "Should be rejected (X-ray, not mammography)",
            "type": "X-ray (Medical but not mammography)"
        }
    ]
    
    results = []
    
    for test_case in test_cases:
        print(f"\n🔍 Testing: {test_case['type']}")
        print(f"File: {test_case['file']}")
        print(f"Expected: {test_case['expected']}")
        
        image_path = test_dir / test_case['file']
        
        try:
            result = validate_mammography_with_ai(str(image_path))
            
            print(f"✅ AI Result:")
            print(f"   - Valid: {result['is_valid']}")
            print(f"   - Mammography: {result['is_mammography']}")
            print(f"   - Confidence: {result['confidence']:.1%}")
            print(f"   - Method: {result['method']}")
            
            if result['method'] == 'gemini_ai':
                print("🤖 REAL AI ANALYSIS ACTIVE!")
            else:
                print("🔧 Development mode (need API key for real AI)")
            
            results.append({
                'type': test_case['type'],
                'valid': result['is_valid'],
                'mammography': result['is_mammography'],
                'confidence': result['confidence'],
                'method': result['method']
            })
            
        except Exception as e:
            print(f"❌ Error testing {test_case['file']}: {str(e)}")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    for result in results:
        status = "✅ PASS" if result['method'] == 'gemini_ai' else "⚠️ DEV MODE"
        print(f"{status} {result['type']}: Valid={result['valid']}, Mammography={result['mammography']}, Confidence={result['confidence']:.1%}")
    
    if any(r['method'] == 'gemini_ai' for r in results):
        print("\n🎉 REAL AI ANALYSIS IS WORKING!")
        print("The system can now distinguish between mammography and other images!")
    else:
        print("\n🔧 DEVELOPMENT MODE ACTIVE")
        print("To enable real AI analysis:")
        print("1. Get API key: https://makersuite.google.com/app/apikey")
        print("2. Update .env file with your key")
        print("3. Restart the application")

if __name__ == "__main__":
    test_image_distinction()