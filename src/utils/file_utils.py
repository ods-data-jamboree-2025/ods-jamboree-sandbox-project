"""
Common utility functions for the sandbox project.

This module provides utility functions that can be used across different
examples and experiments in the sandbox.
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Union


def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Read data from a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Dictionary containing the JSON data

    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(data: Dict[str, Any], file_path: Union[str, Path]) -> None:
    """
    Write data to a JSON file.

    Args:
        data: Dictionary to write as JSON
        file_path: Path where to save the JSON file
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def read_csv_to_dict(file_path: Union[str, Path]) -> List[Dict[str, str]]:
    """
    Read a CSV file and return as a list of dictionaries.

    Args:
        file_path: Path to the CSV file

    Returns:
        List of dictionaries, one per row

    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_dict_to_csv(data: List[Dict[str, Any]], file_path: Union[str, Path]) -> None:
    """
    Write a list of dictionaries to a CSV file.

    Args:
        data: List of dictionaries to write
        file_path: Path where to save the CSV file
    """
    if not data:
        return

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = data[0].keys()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def ensure_directory(dir_path: Union[str, Path]) -> Path:
    """
    Ensure a directory exists, creating it if necessary.

    Args:
        dir_path: Path to the directory

    Returns:
        Path object for the directory
    """
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def list_files_with_extension(
    directory: Union[str, Path], extension: str
) -> List[Path]:
    """
    List all files with a specific extension in a directory.

    Args:
        directory: Path to the directory to search
        extension: File extension to search for (e.g., '.py', '.txt')

    Returns:
        List of Path objects for matching files
    """
    path = Path(directory)
    if not path.exists():
        return []

    if not extension.startswith("."):
        extension = "." + extension

    return list(path.glob(f"*{extension}"))


def calculate_statistics(numbers: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculate basic statistics for a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Dictionary with mean, median, min, max, and std

    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics for empty list")

    sorted_numbers = sorted(numbers)
    n = len(numbers)

    # Mean
    mean = sum(numbers) / n

    # Median
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    # Min and Max
    minimum = min(numbers)
    maximum = max(numbers)

    # Standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance**0.5

    return {
        "mean": mean,
        "median": median,
        "min": minimum,
        "max": maximum,
        "std": std_dev,
        "count": n,
    }
