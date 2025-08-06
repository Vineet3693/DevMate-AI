
from ..models.analysis_models import AnalysisRequest, AnalysisResponse
from ..config.settings import load_config
from groq import Groq

class DebugAssistant:
    def __init__(self):
        self.config = load_config()
        self.client = Groq(api_key=self.config.GROQ_API_KEY)
    
    def debug_code(self, request: AnalysisRequest) -> AnalysisResponse:
        prompt = f"Debug this {request.language} code and find issues:\n{request.code}"
        
        response = self.client.chat.completions.create(
            model=self.config.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config.MAX_TOKENS,
            temperature=self.config.TEMPERATURE
        )
        
        return AnalysisResponse(
            issues=[{"type": "debug", "message": response.choices[0].message.content}],
            suggestions=[],
            complexity_score=0.5
        )
