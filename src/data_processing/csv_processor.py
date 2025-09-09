"""
CSV Data Processor

A simple example of processing CSV data with pandas.
This module demonstrates common data processing tasks.
"""

from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd


class CSVProcessor:
    """A class for processing CSV data files."""

    def __init__(self, file_path: Optional[str] = None):
        """
        Initialize the CSV processor.

        Args:
            file_path: Optional path to a CSV file to load
        """
        self.data = None
        self.file_path = file_path

        if file_path:
            self.load_data(file_path)

    def load_data(self, file_path: str) -> None:
        """
        Load data from a CSV file.

        Args:
            file_path: Path to the CSV file

        Raises:
            FileNotFoundError: If the file doesn't exist
            pd.errors.EmptyDataError: If the file is empty
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        self.data = pd.read_csv(file_path)
        self.file_path = file_path
        print(f"✅ Loaded data from {file_path}")
        print(f"   Shape: {self.data.shape}")

    def create_sample_data(self, n_rows: int = 100) -> pd.DataFrame:
        """
        Create sample data for testing.

        Args:
            n_rows: Number of rows to generate

        Returns:
            DataFrame with sample data
        """
        np.random.seed(42)

        data = {
            "id": range(1, n_rows + 1),
            "name": [f"Person_{i}" for i in range(1, n_rows + 1)],
            "age": np.random.randint(18, 80, n_rows),
            "salary": np.random.normal(50000, 15000, n_rows).round(2),
            "department": np.random.choice(
                ["Engineering", "Sales", "Marketing", "HR"], n_rows
            ),
            "experience_years": np.random.randint(0, 20, n_rows),
            "performance_score": np.random.uniform(1, 5, n_rows).round(2),
        }

        self.data = pd.DataFrame(data)
        print(f"✅ Created sample data with {n_rows} rows")
        return self.data

    def get_basic_info(self) -> Dict[str, Any]:
        """
        Get basic information about the dataset.

        Returns:
            Dictionary with basic dataset information
        """
        if self.data is None:
            raise ValueError(
                "No data loaded. Use load_data() or create_sample_data() first."
            )

        info = {
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.to_dict(),
            "missing_values": self.data.isnull().sum().to_dict(),
            "memory_usage": f"{self.data.memory_usage(deep=True).sum() / 1024:.2f} KB",
        }

        return info

    def clean_data(self) -> pd.DataFrame:
        """
        Perform basic data cleaning operations.

        Returns:
            Cleaned DataFrame
        """
        if self.data is None:
            raise ValueError(
                "No data loaded. Use load_data() or create_sample_data() first."
            )

        cleaned_data = self.data.copy()

        # Remove duplicates
        initial_rows = len(cleaned_data)
        cleaned_data = cleaned_data.drop_duplicates()
        removed_duplicates = initial_rows - len(cleaned_data)

        # Handle missing values (example: fill with median for numeric columns)
        numeric_columns = cleaned_data.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            if cleaned_data[col].isnull().any():
                median_value = cleaned_data[col].median()
                cleaned_data[col].fillna(median_value, inplace=True)

        # Fill missing values in string columns with 'Unknown'
        string_columns = cleaned_data.select_dtypes(include=["object"]).columns
        for col in string_columns:
            cleaned_data[col].fillna("Unknown", inplace=True)

        print("🧹 Data cleaning completed:")
        print(f"   Removed {removed_duplicates} duplicate rows")
        print(f"   Filled missing values in {len(numeric_columns)} numeric columns")
        print(f"   Filled missing values in {len(string_columns)} string columns")

        self.data = cleaned_data
        return cleaned_data

    def get_summary_statistics(self) -> pd.DataFrame:
        """
        Get summary statistics for numeric columns.

        Returns:
            DataFrame with summary statistics
        """
        if self.data is None:
            raise ValueError(
                "No data loaded. Use load_data() or create_sample_data() first."
            )

        return self.data.describe()

    def group_analysis(
        self, group_by_column: str, agg_column: str, agg_function: str = "mean"
    ) -> pd.DataFrame:
        """
        Perform group-by analysis.

        Args:
            group_by_column: Column to group by
            agg_column: Column to aggregate
            agg_function: Aggregation function ('mean', 'sum', 'count', etc.)

        Returns:
            DataFrame with grouped results
        """
        if self.data is None:
            raise ValueError(
                "No data loaded. Use load_data() or create_sample_data() first."
            )

        if group_by_column not in self.data.columns:
            raise ValueError(f"Column '{group_by_column}' not found in data")

        if agg_column not in self.data.columns:
            raise ValueError(f"Column '{agg_column}' not found in data")

        result = self.data.groupby(group_by_column)[agg_column].agg(agg_function)
        return result.reset_index()

    def filter_data(self, conditions: Dict[str, Any]) -> pd.DataFrame:
        """
        Filter data based on conditions.

        Args:
            conditions: Dictionary of column names and filter values
                       e.g., {'age': (25, 65), 'department': 'Engineering'}

        Returns:
            Filtered DataFrame
        """
        if self.data is None:
            raise ValueError(
                "No data loaded. Use load_data() or create_sample_data() first."
            )

        filtered_data = self.data.copy()

        for column, condition in conditions.items():
            if column not in filtered_data.columns:
                print(f"⚠️  Warning: Column '{column}' not found, skipping filter")
                continue

            if isinstance(condition, tuple) and len(condition) == 2:
                # Range filter
                min_val, max_val = condition
                filtered_data = filtered_data[
                    (filtered_data[column] >= min_val)
                    & (filtered_data[column] <= max_val)
                ]
            elif isinstance(condition, list):
                # Multiple values filter
                filtered_data = filtered_data[filtered_data[column].isin(condition)]
            else:
                # Single value filter
                filtered_data = filtered_data[filtered_data[column] == condition]

        print(
            f"🔍 Filtered data: {len(filtered_data)} rows remaining (from {len(self.data)})"
        )
        return filtered_data

    def save_data(self, output_path: str, data: Optional[pd.DataFrame] = None) -> None:
        """
        Save data to a CSV file.

        Args:
            output_path: Path to save the CSV file
            data: Optional DataFrame to save (uses self.data if not provided)
        """
        if data is None:
            data = self.data

        if data is None:
            raise ValueError("No data to save")

        # Ensure output directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        data.to_csv(output_path, index=False)
        print(f"💾 Data saved to {output_path}")


def demonstrate_csv_processing():
    """Demonstrate the CSV processing functionality."""
    print("🔧 CSV Data Processing Demo")
    print("=" * 40)

    # Create a processor instance
    processor = CSVProcessor()

    # Create sample data
    print("\n1. Creating sample data...")
    data = processor.create_sample_data(50)
    print(data.head())

    # Get basic info
    print("\n2. Basic dataset information...")
    info = processor.get_basic_info()
    print(f"Shape: {info['shape']}")
    print(f"Columns: {info['columns']}")
    print(f"Memory usage: {info['memory_usage']}")

    # Summary statistics
    print("\n3. Summary statistics...")
    stats = processor.get_summary_statistics()
    print(stats)

    # Group analysis
    print("\n4. Group analysis (average salary by department)...")
    group_result = processor.group_analysis("department", "salary", "mean")
    print(group_result)

    # Filter data
    print("\n5. Filtering data (age 25-45, Engineering/Sales departments)...")
    filtered = processor.filter_data(
        {"age": (25, 45), "department": ["Engineering", "Sales"]}
    )
    print("Filtered data preview:")
    print(filtered[["name", "age", "department", "salary"]].head())

    print("\n✅ Demo completed!")


if __name__ == "__main__":
    demonstrate_csv_processing()
