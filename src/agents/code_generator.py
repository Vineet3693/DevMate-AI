
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field
from typing import List, Optional
import os

class GeneratedCode(BaseModel):
    code: str
    explanation: str
    language: str
    functions: List[str] = []
    dependencies: List[str] = []
    test_cases: Optional[str] = None
    documentation: Optional[str] = None

class CodeGenerator:
    def __init__(self):
        self.agent = Agent(
            f"groq:{os.getenv('GROQ_MODEL', 'llama-3.1-70b-versatile')}",
            result_type=GeneratedCode,
            system_prompt=self._get_system_prompt()
        )
    
    def _get_system_prompt(self) -> str:
        return """
        You are an expert software engineer specializing in clean, efficient code generation.
        
        When generating code:
        1. Follow language-specific best practices
        2. Include proper error handling
        3. Add clear comments and documentation
        4. Use appropriate design patterns
        5. Ensure code is production-ready
        6. Include type hints where applicable
        7. Generate corresponding test cases
        
        Always explain your approach and design decisions.
        """
    
    async def generate_code(self, description: str, language: str, 
                          include_tests: bool = True) -> GeneratedCode:
        """Generate code based on natural language description"""
        prompt = f"""
        Generate {language} code for the following requirement:
        
        Description: {description}
        Language: {language}
        Include Tests: {include_tests}
        
        Provide:
        1. Clean, well-documented code
        2. Explanation of the approach
        3. List of functions created
        4. Required dependencies
        {"5. Unit tests" if include_tests else ""}
        """
        
        result = await self.agent.run(prompt)
        return result.data
