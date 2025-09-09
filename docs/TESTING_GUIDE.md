# Testing Guide for ODS Data Jamboree Sandbox Project

This guide provides comprehensive information about testing in the sandbox project, including how to write, run, and understand tests.

## 🎯 Why Testing Matters

Testing is crucial for:
- **Confidence**: Ensuring your code works as expected
- **Documentation**: Tests serve as executable documentation
- **Refactoring**: Safe code changes with immediate feedback
- **Learning**: Understanding how code should behave
- **Collaboration**: Ensuring changes don't break existing functionality

## 🧪 Testing Framework

We use **pytest** for testing because it's:
- Easy to learn and use
- Powerful and flexible
- Great for both simple and complex testing scenarios
- Widely adopted in the Python community

## 🚀 Getting Started with Tests

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_examples.py

# Run specific test function
pytest tests/test_examples.py::TestHelloWorld::test_greet_default

# Run tests matching a pattern
pytest -k "test_greet"

# Run with coverage report
pytest --cov=src

# Run with detailed coverage report
pytest --cov=src --cov-report=html
```

### Understanding Test Output

```bash
# Successful test output
tests/test_examples.py::TestHelloWorld::test_greet_default PASSED

# Failed test output
tests/test_examples.py::TestHelloWorld::test_greet_default FAILED
```

## ✍️ Writing Tests

### Basic Test Structure

```python
def test_function_name():
    """Test description."""
    # Arrange - Set up test data
    input_value = "test"
    expected_result = "expected"
    
    # Act - Call the function being tested
    actual_result = function_to_test(input_value)
    
    # Assert - Check the result
    assert actual_result == expected_result
```

### Test Naming Conventions

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*`
- Descriptive names: `test_greet_with_custom_name`

### Example Test Cases

```python
import pytest
from src.examples.hello_world import greet

class TestGreetFunction:
    """Test cases for the greet function."""
    
    def test_greet_default_name(self):
        """Test greeting with default name."""
        result = greet()
        assert result == "Hello, World!"
    
    def test_greet_custom_name(self):
        """Test greeting with custom name."""
        result = greet("Alice")
        assert result == "Hello, Alice!"
    
    def test_greet_empty_string(self):
        """Test greeting with empty string."""
        result = greet("")
        assert result == "Hello, !"
```

## 🎯 Types of Tests

### 1. Unit Tests
Test individual functions or methods in isolation.

```python
def test_calculate_statistics():
    """Test statistics calculation for a simple list."""
    from src.utils.file_utils import calculate_statistics
    
    numbers = [1, 2, 3, 4, 5]
    stats = calculate_statistics(numbers)
    
    assert stats['mean'] == 3.0
    assert stats['median'] == 3.0
    assert stats['min'] == 1
    assert stats['max'] == 5
```

### 2. Integration Tests
Test how different parts work together.

```python
def test_data_processing_pipeline():
    """Test the complete data processing pipeline."""
    from src.data_processing.csv_processor import CSVProcessor
    
    processor = CSVProcessor()
    data = processor.create_sample_data(10)
    cleaned = processor.clean_data()
    stats = processor.get_summary_statistics()
    
    assert len(cleaned) == 10
    assert 'mean' in stats.loc['age']
```

### 3. Exception Tests
Test that functions handle errors correctly.

```python
def test_function_raises_exception():
    """Test that function raises ValueError for invalid input."""
    from src.utils.file_utils import calculate_statistics
    
    with pytest.raises(ValueError, match="Cannot calculate statistics for empty list"):
        calculate_statistics([])
```

## 🔧 Advanced Testing Techniques

### Parametrized Tests
Run the same test with different inputs.

```python
@pytest.mark.parametrize("name,expected", [
    ("Alice", "Hello, Alice!"),
    ("Bob", "Hello, Bob!"),
    ("", "Hello, !"),
])
def test_greet_parametrized(name, expected):
    """Test greet function with multiple inputs."""
    assert greet(name) == expected
```

### Fixtures
Reusable test data or setup code.

```python
@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    """Test using fixture data."""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15
```

### Temporary Files and Directories
For testing file operations.

```python
import tempfile
from pathlib import Path

def test_file_operations():
    """Test file read/write operations."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json') as f:
        test_data = {"key": "value"}
        write_json(test_data, f.name)
        result = read_json(f.name)
        assert result == test_data
```

### Mocking
Replace external dependencies for isolated testing.

```python
from unittest.mock import patch, MagicMock

@patch('requests.get')
def test_api_call(mock_get):
    """Test API call with mocked response."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "ok"}
    mock_get.return_value = mock_response
    
    result = make_api_call()
    assert result["status"] == "ok"
```

## 📊 Test Coverage

### Understanding Coverage
- **Line Coverage**: Percentage of code lines executed
- **Branch Coverage**: Percentage of code branches taken
- **Function Coverage**: Percentage of functions called

### Checking Coverage

```bash
# Generate coverage report
pytest --cov=src

# Generate HTML coverage report
pytest --cov=src --cov-report=html

# View HTML report
open htmlcov/index.html  # On macOS
# or
firefox htmlcov/index.html  # On Linux
```

### Coverage Targets
- **Good**: 80% coverage
- **Great**: 90% coverage
- **Excellent**: 95% coverage

Focus on testing critical functionality rather than achieving 100% coverage.

## 🐛 Debugging Failed Tests

### Common Test Failures

1. **AssertionError**
   ```python
   # Failed assertion
   assert actual == expected
   # Fix: Check your logic or expected values
   ```

2. **ImportError**
   ```python
   # Module not found
   from src.module import function
   # Fix: Check your Python path and module structure
   ```

3. **AttributeError**
   ```python
   # Method doesn't exist
   result.some_method()
   # Fix: Check object type and available methods
   ```

### Debugging Techniques

```python
# Add debug prints (remove before committing)
def test_debug_example():
    result = function_to_test(input_data)
    print(f"Debug: result = {result}")  # Temporary debug
    assert result == expected

# Use pytest's built-in debugging
pytest --pdb  # Drop into debugger on failure

# Show local variables on failure
pytest -l

# Show full output (don't capture stdout)
pytest -s
```

## 🎓 Testing Best Practices

### Do's ✅
- **Write descriptive test names**: `test_greet_returns_proper_format`
- **Test one thing per test**: Focus on a single behavior
- **Use arrange-act-assert pattern**: Clear test structure
- **Test edge cases**: Empty inputs, boundary values, etc.
- **Keep tests simple**: Easy to understand and maintain
- **Make tests independent**: Tests shouldn't depend on each other
- **Test error conditions**: Not just happy paths

### Don'ts ❌
- **Don't test implementation details**: Test behavior, not internal structure
- **Don't write overly complex tests**: Tests should be simpler than the code they test
- **Don't ignore test failures**: Fix or remove failing tests
- **Don't test third-party libraries**: Focus on your own code
- **Don't duplicate test logic**: Use fixtures and helpers

## 🔍 Example Test Files

Check out these example test files in the project:
- `tests/test_examples.py` - Basic unit tests
- `tests/test_utils.py` - Utility function tests

## 🆘 Troubleshooting

### Test Discovery Issues
```bash
# Make sure __init__.py files exist
touch tests/__init__.py

# Check your Python path
python -c "import sys; print(sys.path)"

# Run from project root directory
cd /path/to/project
pytest
```

### Import Issues
```python
# Add src to Python path in test files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
```

### Performance Issues
```bash
# Run tests in parallel (install pytest-xdist)
pip install pytest-xdist
pytest -n auto
```

## 🎯 Practice Exercises

1. **Write a test** for a new function you create
2. **Add parametrized tests** for different input combinations
3. **Create a fixture** for commonly used test data
4. **Test exception handling** for error conditions
5. **Achieve 90% coverage** for a module

## 📚 Further Reading

- [pytest documentation](https://docs.pytest.org/)
- [Python testing best practices](https://realpython.com/python-testing/)
- [Test-driven development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)

Remember: Testing is a skill that improves with practice. Start simple and gradually explore more advanced techniques! 🚀