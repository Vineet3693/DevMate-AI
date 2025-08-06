# DevMate-AI


📁 GITHUB REPOSITORY STRUCTURE
📦 devmate-ai/
├── 📋 README.md
├── 📋 requirements.txt
├── 📋 .env.example
├── 📋 .gitignore
├── 📋 Dockerfile
├── 📋 docker-compose.yml
├── 📋 pyproject.toml
│
├── 📂 src/
│   ├── 📂 agents/
│   │   ├── __init__.py
│   │   ├── code_analyzer.py
│   │   ├── code_generator.py
│   │   ├── documentation_agent.py
│   │   ├── debug_assistant.py
│   │   └── refactoring_agent.py
│   │
│   ├── 📂 models/
│   │   ├── __init__.py
│   │   ├── code_models.py
│   │   ├── analysis_models.py
│   │   └── response_models.py
│   │
│   ├── 📂 utils/
│   │   ├── __init__.py
│   │   ├── code_parser.py
│   │   ├── language_detector.py
│   │   └── file_processor.py
│   │
│   └── 📂 config/
│       ├── __init__.py
│       └── settings.py
│
├── 📂 streamlit_app/
│   ├── 📋 main.py
│   ├── 📂 pages/
│   │   ├── 1_🔍_Code_Analysis.py
│   │   ├── 2_🛠️_Code_Generator.py
│   │   ├── 3_📝_Documentation.py
│   │   ├── 4_🐛_Debug_Assistant.py
│   │   └── 5_📊_Quality_Metrics.py
│   │
│   ├── 📂 components/
│   │   ├── __init__.py
│   │   ├── sidebar.py
│   │   ├── code_editor.py
│   │   └── results_display.py
│   │
│   └── 📂 static/
│       ├── 📂 css/
│       ├── 📂 images/
│       └── 📂 js/
│
├── 📂 tests/
│   ├── test_agents.py
│   ├── test_models.py
│   └── test_utils.py
│
├── 📂 docs/
│   ├── installation.md
│   ├── api_reference.md
│   └── examples.md
│
├── 📂 examples/
│   ├── sample_code/
│   └── demo_notebooks/
│
└── 📂 .github/
    └── 📂 workflows/
        ├── ci.yml
        ├── deploy.yml
        └── tests.yml
