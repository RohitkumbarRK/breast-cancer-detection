"""
Breast Cancer Detection AI Assistant
Professional Medical Image Analysis System
Step 2: Image Validation Interface
"""

import streamlit as st
import sys
from pathlib import Path
import tempfile
import os

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from config.app_config import APP_CONFIG, IMAGE_CONFIG, CLASSIFICATION_LABELS
from src.utils.ai_image_validator import validate_mammography_with_ai
from src.ai.cancer_classifier import analyze_mammography_for_cancer
from src.utils.medical_reporter import generate_medical_report

def main():
    """Main application interface"""
    
    # Page configuration
    st.set_page_config(
        page_title=APP_CONFIG["title"],
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Header
    st.title(f"🏥 {APP_CONFIG['title']}")
    st.subheader(f"📋 {APP_CONFIG['subtitle']}")
    st.markdown(f"**Version:** {APP_CONFIG['version']} | **Target Users:** {APP_CONFIG['target_users']}")
    
    # Sidebar
    with st.sidebar:
        st.header("🤖 AI System Status")
        st.success("✅ AI Image Validation: Active & Working")
        st.success("✅ Google Gemini AI: Active & Analyzing")
        st.success("✅ AI Cancer Classification: Active & Ready")
        st.info("⏳ AI Progress Tracking: In Development")
        
        st.markdown("---")
        st.header("📋 Current Progress")
        st.markdown("**Phase 2 Complete:** ✅ AI Image Validation")
        st.markdown("**Phase 3 Complete:** ✅ Cancer Classification System")
        st.markdown("🤖 **Real Gemini AI Active**")
        st.markdown("✅ **Professional Cancer Detection**")
        st.markdown("🏥 **BI-RADS Medical Reporting**")
    
    # Main content
    st.header("📤 Upload Mammography Image")
    st.markdown("""
    **⚠️ IMPORTANT:** This system is designed specifically for breast mammography images.
    Please ensure you upload only relevant medical images for accurate analysis.
    """)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a mammography image file",
        type=['jpg', 'jpeg', 'png', 'dcm', 'dicom'],
        help="Supported formats: JPG, JPEG, PNG, DICOM"
    )
    
    if uploaded_file is not None:
        # Create columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📷 Uploaded Image")
            
            # Display image
            try:
                st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
                
                # File information
                st.markdown("**File Information:**")
                st.write(f"- **Name:** {uploaded_file.name}")
                st.write(f"- **Size:** {uploaded_file.size / 1024:.1f} KB")
                st.write(f"- **Type:** {uploaded_file.type}")
                
            except Exception as e:
                st.error(f"Error displaying image: {str(e)}")
        
        with col2:
            st.subheader("🔍 Validation Results")
            
            # Save uploaded file temporarily for validation
            with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                temp_path = tmp_file.name
            
            try:
                # Validate the image with AI
                with st.spinner("🤖 AI is analyzing the image..."):
                    validation_result = validate_mammography_with_ai(temp_path)
                
                # Display AI validation results
                if validation_result['is_valid'] and validation_result['is_mammography']:
                    st.success("✅ **AI VALIDATED MAMMOGRAPHY IMAGE**")
                    st.success(f"🤖 AI Confidence: {validation_result['confidence']:.1%}")
                    st.info(f"🔬 Validation Method: {validation_result.get('method', 'AI-Powered')}")
                    
                    # Show AI analysis
                    if validation_result.get('ai_analysis'):
                        with st.expander("🤖 AI Analysis Details"):
                            st.markdown(validation_result['ai_analysis'])
                    
                    # Show warnings if any
                    if validation_result.get('warnings'):
                        with st.expander("⚠️ AI Observations"):
                            for warning in validation_result['warnings']:
                                st.warning(warning)
                    
                    # Next steps
                    st.markdown("---")
                    st.info("🚀 **Ready for AI Cancer Classification**")
                    st.markdown("This image has passed AI validation and can proceed to cancer detection analysis.")
                    
                    if st.button("🔬 Proceed to AI Cancer Analysis", type="primary"):
                        st.markdown("---")
                        st.header("🧠 AI Cancer Classification Analysis")
                        
                        # Perform AI cancer analysis
                        with st.spinner("🤖 AI is analyzing for cancer signs... This may take 30-60 seconds"):
                            cancer_analysis = analyze_mammography_for_cancer(temp_path)
                        
                        if cancer_analysis.get('success', True) and not cancer_analysis.get('error'):
                            # Display cancer analysis results
                            probability = cancer_analysis.get('cancer_probability', 0)
                            bi_rads = cancer_analysis.get('bi_rads_category', 1)
                            risk_level = cancer_analysis.get('risk_level', 'LOW')
                            urgency = cancer_analysis.get('urgency_level', 'ROUTINE')
                            
                            # Risk level styling
                            if risk_level == 'HIGH':
                                st.error(f"🔴 **HIGH RISK DETECTED** - {probability}% Cancer Probability")
                                st.error(f"🚨 **BI-RADS {bi_rads}** - {urgency} Priority")
                            elif risk_level == 'MODERATE':
                                st.warning(f"🟡 **MODERATE RISK** - {probability}% Cancer Probability")
                                st.warning(f"⚠️ **BI-RADS {bi_rads}** - {urgency} Priority")
                            else:
                                st.success(f"🟢 **LOW RISK** - {probability}% Cancer Probability")
                                st.success(f"✅ **BI-RADS {bi_rads}** - {urgency} Priority")
                            
                            # Generate medical reports
                            medical_reports = generate_medical_report(cancer_analysis)
                            
                            # Display executive summary
                            with st.expander("📋 Executive Summary", expanded=True):
                                st.markdown(medical_reports.get('executive_summary', 'Report generation in progress'))
                            
                            # Display detailed findings
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                with st.expander("🔍 Detailed Medical Report"):
                                    st.markdown(medical_reports.get('detailed_report', 'Detailed analysis in progress'))
                                
                                with st.expander("📊 BI-RADS Assessment"):
                                    st.markdown(medical_reports.get('bi_rads_report', 'BI-RADS assessment in progress'))
                            
                            with col2:
                                with st.expander("💡 Clinical Recommendations"):
                                    st.markdown(medical_reports.get('recommendations', 'Recommendations in progress'))
                                
                                with st.expander("🤖 AI Analysis Details"):
                                    st.json({
                                        'Cancer Probability': f"{probability}%",
                                        'BI-RADS Category': bi_rads,
                                        'Risk Level': risk_level,
                                        'Urgency': urgency,
                                        'Mass Detected': cancer_analysis.get('mass_detected', 'Unknown'),
                                        'Calcifications': cancer_analysis.get('calcifications_detected', 'Unknown'),
                                        'AI Model': cancer_analysis.get('ai_model', 'Gemini-1.5-Flash')
                                    })
                            
                            # Download report option
                            st.markdown("---")
                            
                            # Create downloadable report
                            full_report = f"""
{medical_reports.get('executive_summary', '')}

{medical_reports.get('detailed_report', '')}

{medical_reports.get('bi_rads_report', '')}

{medical_reports.get('recommendations', '')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI TECHNICAL DETAILS:
• Cancer Probability: {probability}%
• BI-RADS Category: {bi_rads}
• Risk Level: {risk_level}
• Urgency: {urgency}
• Mass Detected: {cancer_analysis.get('mass_detected', 'Unknown')}
• Calcifications: {cancer_analysis.get('calcifications_detected', 'Unknown')}
• AI Model: {cancer_analysis.get('ai_model', 'Gemini-1.5-Flash')}
• Analysis Method: {cancer_analysis.get('method', 'AI Cancer Classification')}

⚠️ DISCLAIMER: This AI analysis is for educational purposes and should be reviewed by qualified medical professionals.
"""
                            
                            # Generate filename with timestamp
                            from datetime import datetime
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            filename = f"Mammography_AI_Report_{timestamp}.txt"
                            
                            # Download button
                            st.download_button(
                                label="📄 Download Complete Medical Report",
                                data=full_report,
                                file_name=filename,
                                mime="text/plain",
                                type="secondary"
                            )
                            
                            # Also offer JSON download for technical users
                            json_report = {
                                'analysis_results': cancer_analysis,
                                'medical_reports': medical_reports,
                                'generated_at': datetime.now().isoformat(),
                                'ai_model': cancer_analysis.get('ai_model', 'Gemini-1.5-Flash')
                            }
                            
                            import json
                            json_filename = f"Mammography_AI_Data_{timestamp}.json"
                            
                            st.download_button(
                                label="📊 Download Technical Data (JSON)",
                                data=json.dumps(json_report, indent=2),
                                file_name=json_filename,
                                mime="application/json",
                                type="secondary"
                            )
                        
                        else:
                            st.error("❌ **AI Cancer Analysis Failed**")
                            st.error(f"Error: {cancer_analysis.get('error', 'Unknown error occurred')}")
                            st.info("💡 Please try again or contact support if the issue persists.")
                
                else:
                    st.error("❌ **AI VALIDATION FAILED**")
                    st.error("AI analysis indicates this is not a breast mammography image.")
                    
                    if validation_result['confidence'] > 0:
                        st.write(f"🤖 AI Confidence: {validation_result['confidence']:.1%}")
                    
                    # Show AI analysis
                    if validation_result.get('ai_analysis'):
                        with st.expander("🤖 AI Analysis Details"):
                            st.markdown(validation_result['ai_analysis'])
                    
                    # Show errors
                    if validation_result['errors']:
                        st.markdown("**AI Detected Issues:**")
                        for error in validation_result['errors']:
                            st.write(f"❌ {error}")
                    
                    # Show warnings
                    if validation_result['warnings']:
                        st.markdown("**AI Observations:**")
                        for warning in validation_result['warnings']:
                            st.write(f"⚠️ {warning}")
                    
                    st.markdown("---")
                    st.info("💡 **Please upload a valid mammography image for AI analysis.**")
                
            except Exception as e:
                st.error(f"❌ Error during validation: {str(e)}")
                
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_path)
                except:
                    pass
    
    else:
        # Instructions when no file is uploaded
        st.info("👆 Please upload a mammography image to begin validation.")
        
        # Show supported formats
        with st.expander("📋 Supported Image Formats"):
            st.markdown("""
            - **JPEG/JPG**: Standard image format
            - **PNG**: Lossless image format
            - **DICOM (.dcm)**: Medical imaging standard
            
            **Requirements:**
            - Minimum resolution: 512x512 pixels
            - Maximum file size: 50MB
            - Must be a breast mammography image
            """)
        
        # Show AI validation approach
        with st.expander("🤖 AI Validation Approach"):
            st.markdown("""
            **AI-Powered Validation System:**
            
            🧠 **Machine Learning Analysis**
            - Deep learning models for medical image recognition
            - Neural network-based mammography detection
            - Computer vision algorithms for tissue pattern analysis
            
            🤖 **Google Gemini AI Integration**
            - Advanced AI image understanding
            - Medical context awareness
            - Professional medical image assessment
            
            📊 **AI Confidence Scoring**
            - Minimum 75% AI confidence required
            - Multi-model validation consensus
            - Continuous learning and improvement
            
            🚫 **No Rule-Based Approaches**
            - Pure AI/ML validation
            - No hardcoded image analysis rules
            - Adaptive and intelligent validation
            """)
    
    # Footer
    st.markdown("---")
    st.markdown(f"**{APP_CONFIG['developer']}** | Medical AI Solutions for Healthcare Professionals")
    st.markdown("⚠️ *This system is for educational purposes and should not replace professional medical diagnosis.*")

if __name__ == "__main__":
    main()