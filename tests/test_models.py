
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.code_models import CodeRequest, CodeResponse
from models.analysis_models import AnalysisRequest, AnalysisResponse
from models.response_models import BaseResponse

class TestModels:
    def test_code_request_validation(self):
        request = CodeRequest(code="test", language="python")
        assert request.code == "test"
        assert request.language == "python"
    
    def test_code_response_creation(self):
        response = CodeResponse(generated_code="result", language="python")
        assert response.generated_code == "result"
        assert response.language == "python"
    
    def test_analysis_response_creation(self):
        response = AnalysisResponse(
            issues=[{"type": "error", "message": "test"}],
            suggestions=["fix this"],
            complexity_score=0.5
        )
        assert len(response.issues) == 1
        assert len(response.suggestions) == 1
        assert response.complexity_score == 0.5
    
    def test_base_response_success(self):
        response = BaseResponse(success=True, data="test")
        assert response.success is True
        assert response.data == "test"
