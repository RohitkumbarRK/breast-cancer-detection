#!/usr/bin/env python3
"""
Quick test script for AI Image Validator
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.utils.ai_image_validator import validate_mammography_with_ai

def test_ai_validator():
    """Test the AI image validator"""
    print("🤖 Testing AI Image Validator...")
    
    # Test image path
    test_path = project_root / "data" / "test_mammography.jpg"
    
    if not test_path.exists():
        print(f"❌ Test image not found: {test_path}")
        return
    
    # Run validation
    try:
        result = validate_mammography_with_ai(str(test_path))
        
        print("✅ Validation Result:")
        print(f"   - Valid: {result['is_valid']}")
        print(f"   - Mammography: {result['is_mammography']}")
        print(f"   - Confidence: {result['confidence']:.1%}")
        print(f"   - Method: {result['method']}")
        print(f"   - Warnings: {len(result['warnings'])} items")
        
        if result['warnings']:
            print("   - Warning Details:")
            for warning in result['warnings']:
                print(f"     • {warning}")
        
        print("🎉 AI Validator working perfectly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing validator: {str(e)}")
        return False

if __name__ == "__main__":
    test_ai_validator()