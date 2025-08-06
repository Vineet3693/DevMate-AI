
from ..models.code_models import CodeRequest, CodeResponse
from ..config.settings import load_config
from groq import Groq

class DocumentationAgent:
    def __init__(self):
        self.config = load_config()
        self.client = Groq(api_key=self.config.GROQ_API_KEY)
    
    def generate_docs(self, request: CodeRequest) -> CodeResponse:
        prompt = f"Generate documentation for this {request.language} code:\n{request.code}"
        
        response = self.client.chat.completions.create(
            model=self.config.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config.MAX_TOKENS,
            temperature=self.config.TEMPERATURE
        )
        
        return CodeResponse(
            generated_code=response.choices[0].message.content,
            language="markdown"
        )
