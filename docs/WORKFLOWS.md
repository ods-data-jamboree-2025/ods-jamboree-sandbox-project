# Workflow Examples for ODS Data Jamboree Sandbox

This document provides examples of common development workflows that participants can practice in this sandbox environment.

## 🔄 Git Workflows

### Basic Git Workflow
```bash
# 1. Make changes to files
vim src/examples/new_example.py

# 2. Check status
git status

# 3. Add changes
git add src/examples/new_example.py

# 4. Commit changes
git commit -m "Add new example script"

# 5. Push to your fork
git push origin feature-branch
```

### Feature Branch Workflow
```bash
# 1. Create and checkout a new branch
git checkout -b feature/new-data-processor

# 2. Make your changes
# ... edit files ...

# 3. Add and commit
git add .
git commit -m "Add new data processor with CSV support"

# 4. Push branch
git push origin feature/new-data-processor

# 5. Create pull request on GitHub
```

### Collaborative Workflow
```bash
# 1. Keep your fork updated
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main

# 2. Create feature branch from updated main
git checkout -b feature/my-improvement

# 3. Work and commit
# ... make changes ...
git add .
git commit -m "Improve error handling in utility functions"

# 4. Rebase if needed
git rebase main

# 5. Push and create PR
git push origin feature/my-improvement
```

## 🧪 Testing Workflows

### Test-Driven Development (TDD)
```bash
# 1. Write a failing test first
echo "def test_new_function():
    assert new_function('test') == 'expected'" >> tests/test_new.py

# 2. Run tests (should fail)
pytest tests/test_new.py -v

# 3. Write minimal code to make test pass
echo "def new_function(input_str):
    return 'expected'" >> src/utils/new_module.py

# 4. Run tests (should pass)
pytest tests/test_new.py -v

# 5. Refactor and improve
# ... improve implementation ...

# 6. Run tests again
pytest tests/test_new.py -v
```

### Continuous Testing
```bash
# Run tests automatically on file changes
# Install pytest-watch: pip install pytest-watch
ptw src/ tests/

# Or use entr (if available)
find src/ tests/ -name "*.py" | entr pytest
```

## 📊 Data Science Workflow

### Exploratory Data Analysis
```python
# 1. Load and explore data
from src.data_processing.csv_processor import CSVProcessor

processor = CSVProcessor()
data = processor.create_sample_data(100)
print(data.info())

# 2. Basic analysis
stats = processor.get_summary_statistics()
print(stats)

# 3. Group analysis
by_category = processor.group_analysis('department', 'salary', 'mean')
print(by_category)

# 4. Filter and analyze subsets
filtered = processor.filter_data({'age': (25, 45)})
print(f"Filtered dataset size: {len(filtered)}")
```

### Data Pipeline Workflow
```bash
# 1. Create sample data
python -c "
from src.data_processing.csv_processor import CSVProcessor
p = CSVProcessor()
data = p.create_sample_data(200)
p.save_data('data/raw_data.csv', data)
"

# 2. Process data
python -c "
from src.data_processing.csv_processor import CSVProcessor
p = CSVProcessor('data/raw_data.csv')
cleaned = p.clean_data()
p.save_data('data/cleaned_data.csv', cleaned)
"

# 3. Generate analysis
python src/examples/data_analysis.py
```

## 🎨 Code Quality Workflow

### Pre-commit Workflow
```bash
# 1. Format code
black src/ tests/

# 2. Sort imports
isort src/ tests/

# 3. Lint code
flake8 src/ tests/

# 4. Run tests
pytest

# 5. If all pass, commit
git add .
git commit -m "Add feature with proper formatting and tests"
```

### Code Review Workflow
```bash
# 1. Check what changed
git diff main

# 2. Run quality checks
python scripts/setup.py check

# 3. Create detailed commit
git add .
git commit -m "feat: add email extraction utility

- Add extract_emails function to string_utils
- Include comprehensive tests
- Update documentation with examples
- Follows RFC 5322 email format"

# 4. Push for review
git push origin feature/email-extraction
```

## 🔄 CI/CD Workflow

### Local CI Simulation
```bash
# Simulate what CI will do
# 1. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 2. Run linting
flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source
flake8 src/ tests/ --exit-zero --max-complexity=10 --max-line-length=88

# 3. Check formatting
black --check src/ tests/
isort --check-only src/ tests/

# 4. Run tests with coverage
pytest --cov=src --cov-report=term-missing

# 5. Run examples
python src/examples/hello_world.py
python src/examples/data_analysis.py
```

### GitHub Actions Workflow
The project includes a GitHub Actions workflow that:
1. Tests on multiple Python versions (3.8, 3.9, 3.10, 3.11)
2. Runs linting and formatting checks
3. Executes the test suite with coverage
4. Runs example scripts to ensure they work

## 🐛 Debugging Workflow

### Test Debugging
```bash
# 1. Run specific failing test
pytest tests/test_utils.py::TestStringUtils::test_extract_emails -v

# 2. Add debug output
pytest tests/test_utils.py::TestStringUtils::test_extract_emails -v -s

# 3. Drop into debugger on failure
pytest tests/test_utils.py::TestStringUtils::test_extract_emails --pdb

# 4. Show local variables on failure
pytest tests/test_utils.py::TestStringUtils::test_extract_emails -l
```

### Code Debugging
```python
# Use print debugging
def extract_emails(text):
    print(f"Debug: input text = {repr(text)}")  # Temporary debug
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    result = re.findall(email_pattern, text)
    print(f"Debug: found emails = {result}")  # Temporary debug
    return result
```

## 📈 Performance Workflow

### Profiling Code
```python
# Using timeit for simple timing
import timeit

# Time a function
time_taken = timeit.timeit(
    lambda: extract_emails("test@example.com and user@test.org"), 
    number=1000
)
print(f"Time per call: {time_taken/1000:.6f} seconds")
```

### Memory Profiling
```python
# Check memory usage
import sys

def check_memory_usage(data):
    return sys.getsizeof(data)

# Example
large_list = list(range(10000))
print(f"Memory usage: {check_memory_usage(large_list)} bytes")
```

## 🎓 Learning Workflows

### Code Reading Workflow
1. **Start with tests** - Understand expected behavior
2. **Read documentation** - Check docstrings and README
3. **Trace execution** - Follow code path with debugger
4. **Modify and experiment** - Make small changes to understand

### Skill Building Workflow
1. **Pick a small feature** to implement
2. **Write tests first** (TDD approach)
3. **Implement incrementally** 
4. **Refactor and improve**
5. **Document your work**
6. **Share and get feedback**

## 🤝 Collaboration Workflow

### Code Review Process
1. **Self-review first** - Check your own changes
2. **Write clear PR description** - Explain what and why
3. **Respond to feedback** - Address reviewer comments
4. **Update and improve** - Make requested changes
5. **Learn from reviews** - Apply lessons to future code

### Pair Programming
```bash
# Using git for pair programming
# Driver commits with co-author
git commit -m "Add validation logic

Co-authored-by: Partner Name <partner@example.com>"
```

## 🎯 Project-Specific Workflows

### Adding a New Example
1. Create script in `src/examples/`
2. Add comprehensive docstring
3. Include if `__name__ == "__main__":` block
4. Write tests in `tests/test_examples.py`
5. Update README if needed
6. Test with `python src/examples/your_script.py`

### Adding a New Utility
1. Add function to appropriate module in `src/utils/`
2. Include type hints and docstring
3. Write comprehensive tests
4. Add to `__init__.py` if needed
5. Document usage examples

### Improving Documentation
1. Check existing docs for accuracy
2. Add missing examples
3. Update for new features
4. Test all code examples
5. Check for typos and clarity

Remember: This is a **sandbox environment** - feel free to experiment, make mistakes, and learn! 🚀