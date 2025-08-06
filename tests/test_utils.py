
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.code_parser import CodeParser
from utils.language_detector import detect_language
from utils.file_processor import FileProcessor

class TestUtils:
    def test_detect_python_language(self):
        code = "def hello():\n    print('world')"
        result = detect_language(code)
        assert result == "python"
    
    def test_detect_javascript_language(self):
        code = "function hello() { console.log('world'); }"
        result = detect_language(code)
        assert result == "javascript"
    
    def test_detect_unknown_language(self):
        code = "hello world"
        result = detect_language(code)
        assert result == "unknown"
    
    def test_code_parser_extract_functions(self):
        code = "def func1():\n    pass\ndef func2():\n    pass"
        functions = CodeParser.extract_functions(code, "python")
        assert "func1" in functions
        assert "func2" in functions
    
    def test_file_processor_get_extension(self):
        result = FileProcessor.get_file_extension("test.py")
        assert result == ".py"
