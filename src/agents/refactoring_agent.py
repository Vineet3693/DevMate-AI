
from ..models.code_models import CodeRequest, CodeResponse
from ..config.settings import load_config
from groq import Groq

class RefactoringAgent:
    def __init__(self):
        self.config = load_config()
        self.client = Groq(api_key=self.config.GROQ_API_KEY)
    
    def refactor_code(self, request: CodeRequest) -> CodeResponse:
        prompt = f"Refactor this {request.language} code for better quality:\n{request.code}"
        
        response = self.client.chat.completions.create(
            model=self.config.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config.MAX_TOKENS,
            temperature=self.config.TEMPERATURE
        )
        
        return CodeResponse(
            generated_code=response.choices[0].message.content,
            language=request.language
        )
