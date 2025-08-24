"""
Professional Medical Reporting System
Automatic generation of clinical mammography reports
AI-powered medical documentation
"""

from datetime import datetime
from typing import Dict, Any
import json

class MedicalReporter:
    """
    Automatic medical report generation system
    Creates professional clinical documentation
    """
    
    def __init__(self):
        """Initialize medical reporter"""
        self.report_template = self._load_report_template()
    
    def generate_cancer_report(self, analysis_result: Dict[str, Any], patient_info: Dict[str, Any] = None) -> Dict[str, str]:
        """
        Generate comprehensive medical report automatically
        
        Args:
            analysis_result: Cancer analysis results from AI
            patient_info: Optional patient information
            
        Returns:
            Dict containing formatted medical reports
        """
        try:
            # Generate different report formats
            reports = {
                'executive_summary': self._generate_executive_summary(analysis_result),
                'detailed_report': self._generate_detailed_report(analysis_result),
                'clinical_summary': self._generate_clinical_summary(analysis_result),
                'bi_rads_report': self._generate_bi_rads_report(analysis_result),
                'recommendations': self._generate_recommendations(analysis_result)
            }
            
            # Add metadata
            reports['generated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reports['report_type'] = 'AI_Mammography_Analysis'
            reports['ai_confidence'] = f"{analysis_result.get('cancer_probability', 0)}%"
            
            return reports
            
        except Exception as e:
            return {
                'error': f"Report generation failed: {str(e)}",
                'executive_summary': 'Report generation error',
                'detailed_report': 'Unable to generate detailed report',
                'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def _generate_executive_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate executive summary for quick review"""
        
        probability = analysis.get('cancer_probability', 0)
        bi_rads = analysis.get('bi_rads_category', 1)
        risk_level = analysis.get('risk_level', 'LOW')
        urgency = analysis.get('urgency_level', 'ROUTINE')
        
        # Risk level emoji and color coding
        risk_emoji = {
            'LOW': '🟢',
            'MODERATE': '🟡', 
            'HIGH': '🔴'
        }.get(risk_level, '⚪')
        
        urgency_emoji = {
            'ROUTINE': '📅',
            'URGENT': '⚠️',
            'IMMEDIATE': '🚨'
        }.get(urgency, '📅')
        
        summary = f"""
🏥 **MAMMOGRAPHY AI ANALYSIS - EXECUTIVE SUMMARY**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **CLASSIFICATION:** BI-RADS {bi_rads}
🎯 **CANCER PROBABILITY:** {probability}%
{risk_emoji} **RISK LEVEL:** {risk_level}
{urgency_emoji} **URGENCY:** {urgency}

🔍 **KEY FINDINGS:**
{analysis.get('primary_findings', 'AI analysis completed')}

💡 **IMMEDIATE ACTION REQUIRED:**
{analysis.get('clinical_recommendations', 'Follow standard protocols')}

📅 **REPORT GENERATED:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
🤖 **AI ANALYSIS METHOD:** {analysis.get('method', 'Gemini AI')}
"""
        return summary.strip()
    
    def _generate_detailed_report(self, analysis: Dict[str, Any]) -> str:
        """Generate comprehensive detailed medical report"""
        
        report = f"""
🏥 **DETAILED MAMMOGRAPHY ANALYSIS REPORT**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 **CLINICAL INFORMATION:**
• Analysis Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
• AI Model: {analysis.get('ai_model', 'Gemini-1.5-Flash')}
• Analysis Type: {analysis.get('analysis_type', 'Automatic Cancer Detection')}

📊 **CLASSIFICATION RESULTS:**
• BI-RADS Category: {analysis.get('bi_rads_category', 1)}
• Cancer Probability: {analysis.get('cancer_probability', 0)}%
• Risk Stratification: {analysis.get('risk_level', 'LOW')}
• Clinical Urgency: {analysis.get('urgency_level', 'ROUTINE')}

🔍 **DETAILED FINDINGS:**

**Mass Detection:**
{analysis.get('mass_detected', 'No masses detected')}

**Calcification Analysis:**
{analysis.get('calcifications_detected', 'No significant calcifications')}

**Architectural Assessment:**
{analysis.get('architectural_distortion', 'No architectural distortion')}

**Symmetry Evaluation:**
{analysis.get('asymmetry_present', 'Bilateral symmetry maintained')}

📝 **PRIMARY OBSERVATIONS:**
{analysis.get('primary_findings', 'Standard mammographic appearance')}

💡 **CLINICAL RECOMMENDATIONS:**
{analysis.get('clinical_recommendations', 'Continue routine screening')}

📋 **ADDITIONAL NOTES:**
{analysis.get('additional_notes', 'No additional observations')}

⚠️ **DISCLAIMER:**
This AI analysis is for educational purposes and should be reviewed by qualified medical professionals.
"""
        return report.strip()
    
    def _generate_clinical_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate clinical summary for healthcare providers"""
        
        probability = analysis.get('cancer_probability', 0)
        bi_rads = analysis.get('bi_rads_category', 1)
        
        # Clinical interpretation
        if bi_rads <= 2:
            interpretation = "Negative or benign findings"
        elif bi_rads == 3:
            interpretation = "Probably benign - short interval follow-up suggested"
        elif bi_rads == 4:
            interpretation = "Suspicious abnormality - tissue sampling recommended"
        elif bi_rads == 5:
            interpretation = "Highly suggestive of malignancy - appropriate action required"
        else:
            interpretation = "Known malignancy - treatment planning indicated"
        
        summary = f"""
📋 **CLINICAL SUMMARY**

**Assessment:** BI-RADS {bi_rads} ({interpretation})
**Cancer Risk:** {probability}% probability
**Clinical Priority:** {analysis.get('urgency_level', 'ROUTINE')}

**Key Findings:**
{analysis.get('primary_findings', 'Standard mammographic findings')}

**Recommended Actions:**
{analysis.get('clinical_recommendations', 'Continue routine care')}
"""
        return summary.strip()
    
    def _generate_bi_rads_report(self, analysis: Dict[str, Any]) -> str:
        """Generate BI-RADS standardized report"""
        
        bi_rads = analysis.get('bi_rads_category', 1)
        probability = analysis.get('cancer_probability', 0)
        
        # BI-RADS descriptions
        bi_rads_descriptions = {
            1: "Negative - No significant abnormality",
            2: "Benign - Non-cancerous findings",
            3: "Probably Benign - <2% risk of malignancy",
            4: "Suspicious - 2-95% risk of malignancy",
            5: "Highly Suggestive of Malignancy - >95% risk",
            6: "Known Malignancy - Proven cancer"
        }
        
        description = bi_rads_descriptions.get(bi_rads, "Assessment pending")
        
        report = f"""
📊 **BI-RADS ASSESSMENT REPORT**

**BI-RADS Category:** {bi_rads}
**Description:** {description}
**Cancer Probability:** {probability}%

**Clinical Correlation:**
{analysis.get('clinical_recommendations', 'Standard follow-up recommended')}

**Next Steps:**
Based on BI-RADS {bi_rads} classification, {self._get_bi_rads_action(bi_rads)}
"""
        return report.strip()
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> str:
        """Generate clinical recommendations"""
        
        urgency = analysis.get('urgency_level', 'ROUTINE')
        bi_rads = analysis.get('bi_rads_category', 1)
        probability = analysis.get('cancer_probability', 0)
        
        recommendations = f"""
💡 **CLINICAL RECOMMENDATIONS**

**Immediate Actions:**
{analysis.get('clinical_recommendations', 'Continue standard care')}

**Follow-up Schedule:**
{self._get_followup_schedule(bi_rads, urgency)}

**Additional Considerations:**
{analysis.get('additional_notes', 'No additional recommendations')}

**Priority Level:** {urgency}
**Risk Assessment:** {analysis.get('risk_level', 'LOW')} ({probability}%)
"""
        return recommendations.strip()
    
    def _get_bi_rads_action(self, bi_rads: int) -> str:
        """Get recommended action for BI-RADS category"""
        actions = {
            1: "routine annual screening is recommended",
            2: "routine annual screening is recommended", 
            3: "short-term follow-up in 6 months is suggested",
            4: "tissue sampling (biopsy) should be considered",
            5: "tissue sampling (biopsy) is strongly recommended",
            6: "appropriate treatment planning is indicated"
        }
        return actions.get(bi_rads, "clinical correlation is recommended")
    
    def _get_followup_schedule(self, bi_rads: int, urgency: str) -> str:
        """Get follow-up schedule based on findings"""
        if urgency == 'IMMEDIATE':
            return "Immediate consultation within 24-48 hours"
        elif urgency == 'URGENT':
            return "Urgent follow-up within 1-2 weeks"
        elif bi_rads >= 4:
            return "Follow-up within 2-4 weeks for tissue sampling"
        elif bi_rads == 3:
            return "Short-term follow-up in 6 months"
        else:
            return "Routine annual screening"
    
    def _load_report_template(self) -> Dict[str, str]:
        """Load report templates"""
        return {
            'header': "🏥 MAMMOGRAPHY AI ANALYSIS REPORT",
            'footer': "⚠️ This AI analysis requires professional medical review",
            'separator': "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        }

def generate_medical_report(analysis_result: Dict[str, Any], patient_info: Dict[str, Any] = None) -> Dict[str, str]:
    """
    Main function to generate medical reports automatically
    
    Args:
        analysis_result: AI cancer analysis results
        patient_info: Optional patient information
        
    Returns:
        Dict containing all report formats
    """
    try:
        reporter = MedicalReporter()
        return reporter.generate_cancer_report(analysis_result, patient_info)
    except Exception as e:
        return {
            'error': f"Medical report generation failed: {str(e)}",
            'executive_summary': 'Report generation error',
            'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }