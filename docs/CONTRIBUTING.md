# Contributing to ODS Data Jamboree Sandbox Project

Thank you for your interest in contributing to the ODS Data Jamboree Sandbox Project! This document provides guidelines for contributing to this learning environment.

## 🎯 Purpose of Contributions

This is a **sandbox environment** designed for learning and experimentation. Contributions should focus on:

- Educational value
- Clear, well-documented examples
- Beginner-friendly content
- Diverse use cases and scenarios
- Bug fixes and improvements

## 🚀 Getting Started

### 1. Fork and Clone
```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/ods-jamboree-sandbox-project.git
cd ods-jamboree-sandbox-project
```

### 2. Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
```

## 📝 Code Style Guidelines

### Python Code Style
- Follow [PEP 8](https://pep8.org/) guidelines
- Use [Black](https://github.com/psf/black) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Use type hints where appropriate

### Formatting Commands
```bash
# Format code
black src/ tests/
isort src/ tests/

# Check formatting
black --check src/ tests/
isort --check-only src/ tests/

# Lint code
flake8 src/ tests/
```

### Documentation Style
- Use clear, concise language
- Include code examples
- Add docstrings to all functions and classes
- Use Markdown for documentation files

## 🧪 Testing Guidelines

### Writing Tests
- Write tests for all new functionality
- Use `pytest` for testing
- Follow the existing test structure
- Include both positive and negative test cases
- Test edge cases and error conditions

### Test Structure
```python
def test_function_name():
    """Test description of what the function should do."""
    # Arrange
    input_data = "test input"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_output
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_examples.py

# Run with verbose output
pytest -v
```

## 📁 Project Structure

When adding new code, follow this structure:

```
src/
├── examples/          # Example scripts and demonstrations
├── utils/            # Utility functions and helpers
├── data_processing/  # Data processing examples
└── [new_category]/   # New categories as needed

tests/
├── test_examples.py  # Tests for examples
├── test_utils.py     # Tests for utilities
└── test_[new].py     # Tests for new modules

docs/
├── CONTRIBUTING.md   # This file
├── TESTING_GUIDE.md  # Testing guidelines
└── [new_docs].md     # Additional documentation
```

## 🎨 Types of Contributions

### 1. New Examples
- Create educational examples in `src/examples/`
- Include clear documentation and comments
- Add corresponding tests
- Update README.md if needed

### 2. Utility Functions
- Add reusable utilities in `src/utils/`
- Write comprehensive tests
- Include proper error handling
- Add type hints and docstrings

### 3. Documentation
- Improve existing documentation
- Add new guides or tutorials
- Fix typos and unclear explanations
- Add code examples

### 4. Bug Fixes
- Fix issues in existing code
- Add tests to prevent regression
- Update documentation if needed

### 5. Testing Improvements
- Add more test cases
- Improve test coverage
- Add integration tests
- Improve test documentation

## 🔍 Code Review Process

### Before Submitting
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New code has tests
- [ ] Documentation is updated
- [ ] Commit messages are clear

### Pull Request Guidelines
1. **Clear Title**: Use descriptive PR titles
2. **Description**: Explain what and why
3. **Testing**: Describe how you tested
4. **Documentation**: Note any doc updates
5. **Breaking Changes**: Highlight if applicable

### Example PR Description
```markdown
## Summary
Brief description of changes

## Changes Made
- Added new utility function for data validation
- Updated examples to use the new function
- Added comprehensive tests

## Testing
- All existing tests pass
- Added 5 new test cases
- Tested on Python 3.8, 3.9, 3.10

## Documentation
- Updated README.md
- Added docstrings to all new functions
```

## 🚫 What NOT to Contribute

- **Production Code**: This is a sandbox, not a production system
- **Sensitive Data**: Never commit API keys, passwords, or personal data
- **Large Dependencies**: Avoid adding heavy dependencies without discussion
- **Breaking Changes**: Don't break existing functionality without good reason
- **Copyrighted Content**: Only contribute original or properly licensed content

## 🆘 Getting Help

### Questions?
- Open an issue with the `question` label
- Ask during jamboree sessions
- Check existing documentation first

### Found a Bug?
1. Check if it's already reported
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details

### Feature Requests?
1. Open an issue with the `enhancement` label
2. Describe the educational value
3. Provide examples of how it would be used

## 🎉 Recognition

Contributors will be:
- Listed in the project contributors
- Acknowledged in release notes
- Celebrated during jamboree sessions

## 📄 License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

## 🙏 Thank You!

Your contributions help create a better learning environment for all participants. Every contribution, no matter how small, is valuable and appreciated!

Happy coding! 🚀