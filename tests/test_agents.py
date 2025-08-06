
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from agents.code_analyzer import CodeAnalyzer
from agents.code_generator import CodeGenerator
from models.analysis_models import AnalysisRequest
from models.code_models import CodeRequest

class TestAgents:
    def test_code_analyzer_init(self):
        analyzer = CodeAnalyzer()
        assert analyzer is not None
    
    def test_code_generator_init(self):
        generator = CodeGenerator()
        assert generator is not None
    
    def test_analysis_request_creation(self):
        request = AnalysisRequest(code="print('hello')", language="python")
        assert request.code == "print('hello')"
        assert request.language == "python"
    
    def test_code_request_creation(self):
        request = CodeRequest(code="create a function", language="python")
        assert request.code == "create a function"
        assert request.language == "python"
