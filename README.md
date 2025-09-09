
# ODS Data Jamboree 2025 - Sandbox Project 🧪

Welcome to the ODS Data Jamboree 2025 Sandbox Project! This repository provides a safe environment for participants to experiment, test, and learn various development workflows, tools, and GitHub features.

## 🎯 Purpose

This sandbox project is designed for participants to:
- Practice Git and GitHub workflows
- Test different development tools and configurations
- Experiment with CI/CD pipelines
- Learn collaborative development practices
- Try out code formatting, linting, and testing tools
- Explore different project structures and conventions

## 🚀 Getting Started

### Prerequisites
- Git installed on your system
- Python 3.8+ (for Python examples)
- A GitHub account

### Quick Start
1. **Fork this repository** to your own GitHub account
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ods-jamboree-sandbox-project.git
   cd ods-jamboree-sandbox-project
   ```
3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

```
ods-jamboree-sandbox-project/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── requirements-dev.txt         # Development dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # Apache 2.0 License
├── src/                        # Main source code
│   ├── __init__.py
│   ├── examples/               # Example modules and scripts
│   ├── utils/                  # Utility functions
│   └── data_processing/        # Data processing examples
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_examples.py
│   └── test_utils.py
├── docs/                       # Documentation
│   ├── CONTRIBUTING.md
│   ├── TESTING_GUIDE.md
│   └── WORKFLOWS.md
├── scripts/                    # Utility scripts
│   ├── setup.py
│   └── lint.py
└── .github/                    # GitHub configurations
    └── workflows/              # CI/CD workflows
        └── python-tests.yml
```

## 🧪 What You Can Test

### 1. **Git Workflows**
- Create branches and pull requests
- Practice merge conflicts resolution
- Try different branching strategies
- Test commit message conventions

### 2. **Python Development**
- Run and modify example scripts
- Add new functions and modules
- Practice code formatting with `black` and `isort`
- Try linting with `flake8` or `pylint`

### 3. **Testing**
- Write and run tests with `pytest`
- Practice test-driven development (TDD)
- Explore different testing patterns

### 4. **CI/CD**
- Modify GitHub Actions workflows
- Test automated testing and linting
- Experiment with deployment scripts

### 5. **Documentation**
- Practice writing documentation
- Try different documentation formats
- Update README files

## 🛠️ Available Commands

After installing dependencies, you can use these commands:

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src

# Format code
black src/ tests/
isort src/ tests/

# Lint code
flake8 src/ tests/

# Run example scripts
python src/examples/hello_world.py
python src/examples/data_analysis.py
```

## 📚 Learning Resources

### Git & GitHub
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

### Python Development
- [Python Testing 101](docs/TESTING_GUIDE.md)
- [Code Style Guide](docs/CONTRIBUTING.md)

### CI/CD
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Examples](docs/WORKFLOWS.md)

## 🤝 Contributing

This is a sandbox project, so feel free to:
- Open issues for questions or suggestions
- Submit pull requests with improvements
- Add new examples or utilities
- Improve documentation

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

## ⚠️ Important Notes

- **This is a testing environment** - feel free to experiment!
- **Don't commit sensitive data** - this is a public repository
- **Be respectful** - this is a shared learning space
- **Have fun** - learning should be enjoyable!

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🆘 Need Help?

- Check the [documentation](docs/) folder
- Open an issue with your question
- Ask for help during the jamboree sessions

Happy coding! 🎉
