"""
Tests for the examples module.

These tests demonstrate how to write unit tests for the sandbox project.
Participants can use these as examples and add their own tests.
"""

import sys
from pathlib import Path

import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from examples.data_analysis import analyze_data, generate_sample_data
from examples.hello_world import get_current_time, greet


class TestHelloWorld:
    """Tests for the hello_world module."""

    def test_greet_default(self):
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

    def test_get_current_time_format(self):
        """Test that current time is returned in expected format."""
        result = get_current_time()
        assert isinstance(result, str)
        assert len(result) == 19  # "YYYY-MM-DD HH:MM:SS" format
        assert result[4] == "-"
        assert result[7] == "-"
        assert result[10] == " "
        assert result[13] == ":"
        assert result[16] == ":"


class TestDataAnalysis:
    """Tests for the data_analysis module."""

    def test_generate_sample_data_default(self):
        """Test sample data generation with default parameters."""
        df = generate_sample_data()
        assert len(df) == 100
        assert list(df.columns) == ["x", "y", "category", "value"]

    def test_generate_sample_data_custom_size(self):
        """Test sample data generation with custom size."""
        df = generate_sample_data(50)
        assert len(df) == 50
        assert list(df.columns) == ["x", "y", "category", "value"]

    def test_generate_sample_data_categories(self):
        """Test that generated data contains expected categories."""
        df = generate_sample_data(100)
        unique_categories = set(df["category"].unique())
        expected_categories = {"A", "B", "C"}
        assert unique_categories == expected_categories

    def test_analyze_data_structure(self):
        """Test that analysis returns expected structure."""
        df = generate_sample_data(50)
        analysis = analyze_data(df)

        assert "shape" in analysis
        assert "summary_stats" in analysis
        assert "correlation" in analysis
        assert "category_counts" in analysis

        assert analysis["shape"] == (50, 4)
        assert len(analysis["category_counts"]) == 3  # A, B, C

    def test_analyze_data_correlation_matrix(self):
        """Test that correlation matrix has correct dimensions."""
        df = generate_sample_data(100)
        analysis = analyze_data(df)

        corr_matrix = analysis["correlation"]
        # Should have correlation for numeric columns: x, y, value
        assert corr_matrix.shape == (3, 3)

        # Diagonal should be 1.0 (perfect self-correlation)
        assert all(corr_matrix.iloc[i, i] == 1.0 for i in range(3))


# Example of a parametrized test
class TestParametrizedExamples:
    """Examples of parametrized tests."""

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Alice", "Hello, Alice!"),
            ("Bob", "Hello, Bob!"),
            ("", "Hello, !"),
            ("123", "Hello, 123!"),
        ],
    )
    def test_greet_parametrized(self, name, expected):
        """Test greet function with multiple inputs."""
        assert greet(name) == expected

    @pytest.mark.parametrize("n_samples", [10, 50, 100, 200])
    def test_sample_data_sizes(self, n_samples):
        """Test sample data generation with different sizes."""
        df = generate_sample_data(n_samples)
        assert len(df) == n_samples
        assert len(df.columns) == 4


# Example of testing for exceptions
class TestExceptionHandling:
    """Examples of testing exception handling."""

    def test_generate_sample_data_zero_samples(self):
        """Test that zero samples raises appropriate behavior."""
        # This should work but return empty DataFrame
        df = generate_sample_data(0)
        assert len(df) == 0

    def test_generate_sample_data_negative_samples(self):
        """Test that negative samples handles appropriately."""
        # This depends on implementation - might raise ValueError
        # For now, we'll test that it doesn't crash
        try:
            df = generate_sample_data(-1)
            # If it doesn't raise an exception, check it's empty or has expected behavior
            assert len(df) >= 0
        except ValueError:
            # This is also acceptable behavior
            pass


# Fixture example
@pytest.fixture
def sample_dataframe():
    """Fixture providing a sample DataFrame for testing."""
    return generate_sample_data(20)


class TestWithFixtures:
    """Examples of using fixtures in tests."""

    def test_using_fixture(self, sample_dataframe):
        """Test using the sample DataFrame fixture."""
        assert len(sample_dataframe) == 20
        assert "x" in sample_dataframe.columns

    def test_fixture_analysis(self, sample_dataframe):
        """Test analysis with fixture data."""
        analysis = analyze_data(sample_dataframe)
        assert analysis["shape"] == (20, 4)


if __name__ == "__main__":
    # Run tests if this file is executed directly
    pytest.main([__file__, "-v"])
