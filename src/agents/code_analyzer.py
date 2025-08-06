
from ..models.analysis_models import AnalysisRequest, AnalysisResponse
from ..config.settings import load_config
from groq import Groq

class CodeAnalyzer:
    def __init__(self):
        self.config = load_config()
        self.client = Groq(api_key=self.config.GROQ_API_KEY)
    
    def analyze_code(self, request: AnalysisRequest) -> AnalysisResponse:
        prompt = f"Analyze this {request.language} code for issues and quality:\n{request.code}"
        
        response = self.client.chat.completions.create(
            model=self.config.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config.MAX_TOKENS,
            temperature=self.config.TEMPERATURE
        )
        
        content = response.choices[0].message.content
        
        return AnalysisResponse(
            issues=[{"type": "analysis", "message": content}],
            suggestions=["Review the analysis above"],
            complexity_score=0.7
        )
