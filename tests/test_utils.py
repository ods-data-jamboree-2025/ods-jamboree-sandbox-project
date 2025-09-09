"""
Tests for the utils module.

These tests demonstrate testing utility functions and edge cases.
"""

import sys
import tempfile
from pathlib import Path

import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils.file_utils import (calculate_statistics, ensure_directory,
                              list_files_with_extension, read_json, write_json)
from utils.string_utils import (camel_to_snake, clean_text, count_words,
                                extract_emails, generate_slug, snake_to_camel,
                                truncate_text)


class TestFileUtils:
    """Tests for file utility functions."""

    def test_calculate_statistics_basic(self):
        """Test basic statistics calculation."""
        numbers = [1, 2, 3, 4, 5]
        stats = calculate_statistics(numbers)

        assert stats["mean"] == 3.0
        assert stats["median"] == 3.0
        assert stats["min"] == 1
        assert stats["max"] == 5
        assert stats["count"] == 5
        assert stats["std"] > 0

    def test_calculate_statistics_empty_list(self):
        """Test statistics with empty list raises ValueError."""
        with pytest.raises(
            ValueError, match="Cannot calculate statistics for empty list"
        ):
            calculate_statistics([])

    def test_calculate_statistics_single_value(self):
        """Test statistics with single value."""
        stats = calculate_statistics([42])
        assert stats["mean"] == 42
        assert stats["median"] == 42
        assert stats["min"] == 42
        assert stats["max"] == 42
        assert stats["std"] == 0.0
        assert stats["count"] == 1

    def test_calculate_statistics_even_count(self):
        """Test median calculation with even number of values."""
        numbers = [1, 2, 3, 4]
        stats = calculate_statistics(numbers)
        assert stats["median"] == 2.5  # (2 + 3) / 2

    def test_json_read_write(self):
        """Test JSON read and write operations."""
        test_data = {"name": "Test", "value": 42, "items": [1, 2, 3]}

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        try:
            # Write and read JSON
            write_json(test_data, temp_path)
            read_data = read_json(temp_path)

            assert read_data == test_data
        finally:
            Path(temp_path).unlink()  # Clean up

    def test_read_json_file_not_found(self):
        """Test reading non-existent JSON file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            read_json("non_existent_file.json")

    def test_ensure_directory(self):
        """Test directory creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_path = Path(temp_dir) / "new" / "nested" / "directory"

            result = ensure_directory(test_path)

            assert result.exists()
            assert result.is_dir()
            assert result == test_path

    def test_list_files_with_extension(self):
        """Test listing files with specific extension."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create test files
            (temp_path / "test1.txt").touch()
            (temp_path / "test2.txt").touch()
            (temp_path / "test.py").touch()
            (temp_path / "test.md").touch()

            txt_files = list_files_with_extension(temp_path, ".txt")
            py_files = list_files_with_extension(temp_path, "py")  # Without dot

            assert len(txt_files) == 2
            assert len(py_files) == 1
            assert all(f.suffix == ".txt" for f in txt_files)


class TestStringUtils:
    """Tests for string utility functions."""

    def test_clean_text_basic(self):
        """Test basic text cleaning."""
        text = "  Hello   World!  "
        result = clean_text(text)
        assert result == "hello world!"

    def test_clean_text_no_lowercase(self):
        """Test text cleaning without lowercasing."""
        text = "Hello WORLD"
        result = clean_text(text, lowercase=False)
        assert result == "Hello WORLD"

    def test_clean_text_remove_punctuation(self):
        """Test text cleaning with punctuation removal."""
        text = "Hello, World! How are you?"
        result = clean_text(text, remove_punctuation=True)
        assert result == "hello world how are you"

    def test_count_words(self):
        """Test word counting."""
        assert count_words("Hello world") == 2
        assert count_words("") == 0
        assert count_words("   ") == 0
        assert count_words("One") == 1
        assert count_words("  Multiple   spaces   between  ") == 3

    def test_extract_emails(self):
        """Test email extraction."""
        text = "Contact us at hello@example.com or support@test.org for help."
        emails = extract_emails(text)
        assert len(emails) == 2
        assert "hello@example.com" in emails
        assert "support@test.org" in emails

    def test_extract_emails_no_emails(self):
        """Test email extraction with no emails."""
        text = "No emails in this text."
        emails = extract_emails(text)
        assert len(emails) == 0

    def test_truncate_text(self):
        """Test text truncation."""
        text = "This is a long text that needs to be truncated"
        result = truncate_text(text, 20)
        assert len(result) <= 20
        assert result.endswith("...")
        assert result == "This is a long te..."

    def test_truncate_text_short(self):
        """Test truncation with text shorter than max length."""
        text = "Short"
        result = truncate_text(text, 20)
        assert result == "Short"

    def test_snake_to_camel(self):
        """Test snake_case to camelCase conversion."""
        assert snake_to_camel("hello_world") == "helloWorld"
        assert snake_to_camel("test_function_name") == "testFunctionName"
        assert snake_to_camel("single") == "single"

    def test_camel_to_snake(self):
        """Test camelCase to snake_case conversion."""
        assert camel_to_snake("helloWorld") == "hello_world"
        assert camel_to_snake("testFunctionName") == "test_function_name"
        assert camel_to_snake("single") == "single"
        assert camel_to_snake("HTTPResponse") == "http_response"

    def test_generate_slug(self):
        """Test URL slug generation."""
        assert generate_slug("Hello World!") == "hello-world"
        assert generate_slug("Test with Spaces & Symbols") == "test-with-spaces-symbols"
        assert generate_slug("Multiple---Hyphens") == "multiple-hyphens"

    def test_generate_slug_max_length(self):
        """Test slug generation with max length."""
        long_text = "This is a very long title that exceeds the maximum length"
        slug = generate_slug(long_text, max_length=20)
        assert len(slug) <= 20
        assert not slug.endswith("-")


# Parametrized tests for comprehensive coverage
class TestParametrizedUtils:
    """Parametrized tests for utility functions."""

    @pytest.mark.parametrize(
        "numbers,expected_mean",
        [
            ([1, 2, 3], 2.0),
            ([10, 20, 30], 20.0),
            ([1], 1.0),
            ([0, 0, 0], 0.0),
        ],
    )
    def test_statistics_mean(self, numbers, expected_mean):
        """Test mean calculation with various inputs."""
        stats = calculate_statistics(numbers)
        assert stats["mean"] == expected_mean

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("hello@example.com", 1),
            ("No emails here", 0),
            ("test@test.com and user@domain.org", 2),
            ("invalid.email", 0),
        ],
    )
    def test_email_extraction_count(self, text, expected):
        """Test email extraction count with various inputs."""
        emails = extract_emails(text)
        assert len(emails) == expected

    @pytest.mark.parametrize(
        "snake,camel",
        [
            ("hello_world", "helloWorld"),
            ("test_case", "testCase"),
            ("single", "single"),
        ],
    )
    def test_case_conversion(self, snake, camel):
        """Test bidirectional case conversion."""
        assert snake_to_camel(snake) == camel
        assert camel_to_snake(camel) == snake


if __name__ == "__main__":
    # Run tests if this file is executed directly
    pytest.main([__file__, "-v"])
