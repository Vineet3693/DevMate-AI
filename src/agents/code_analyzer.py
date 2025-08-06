
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from ..models.analysis_models import CodeSmell, SecurityVulnerability, PerformanceInsight

class CodeAnalysisResult(BaseModel):
    code_smells: List[CodeSmell] = []
    security_issues: List[SecurityVulnerability] = []
    performance_insights: List[PerformanceInsight] = []
    overall_score: int = Field(ge=0, le=100)
    summary: str
    recommendations: List[str] = []

class CodeAnalyzer:
    def __init__(self):
        self.agent = Agent(
            f"groq:{os.getenv('GROQ_MODEL', 'llama-3.1-70b-versatile')}",
            result_type=CodeAnalysisResult,
            system_prompt=self._get_system_prompt()
        )
    
    def _get_system_prompt(self) -> str:
        return """
        You are an expert code reviewer and software architect with 15+ years of experience.
        
        Analyze the provided code for:
        1. Code smells and anti-patterns
        2. Security vulnerabilities
        3. Performance bottlenecks
        4. Best practice violations
        5. Maintainability issues
        
        Provide specific, actionable feedback with:
        - Clear explanations
        - Line-specific issues
        - Concrete improvement suggestions
        - Severity ratings
        - Example fixes where appropriate
        
        Rate the overall code quality from 0-100.
        """
    
    @agent.tool
    async def detect_language(self, ctx: RunContext, code: str) -> str:
        """Detect the programming language of the code"""
        # Simple language detection logic
        if 'def ' in code and 'import ' in code:
            return 'python'
        elif 'function ' in code or 'const ' in code:
            return 'javascript'
        elif 'public class' in code:
            return 'java'
        return 'unknown'
    
    @agent.tool
    async def count_lines(self, ctx: RunContext, code: str) -> int:
        """Count non-empty lines of code"""
        return len([line for line in code.split('\n') if line.strip()])
    
    async def analyze_code(self, code: str, language: str = None) -> CodeAnalysisResult:
        """Analyze code and return structured results"""
        prompt = f"""
        Analyze this {language or 'code'} for quality, security, and performance:
        
        ```{language or ''}
        {code}

        ```
        
        Provide a comprehensive analysis with specific line numbers where issues occur.
        """
        
        result = await self.agent.run(prompt)
        return result.data
