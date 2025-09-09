"""
String utility functions for the sandbox project.

This module provides common string manipulation and text processing utilities.
"""

import re
import string
from typing import List, Optional


def clean_text(
    text: str, remove_punctuation: bool = False, lowercase: bool = True
) -> str:
    """
    Clean and normalize text.

    Args:
        text: Input text to clean
        remove_punctuation: Whether to remove punctuation
        lowercase: Whether to convert to lowercase

    Returns:
        Cleaned text
    """
    if not isinstance(text, str):
        text = str(text)

    # Remove extra whitespace
    cleaned = re.sub(r"\s+", " ", text.strip())

    if lowercase:
        cleaned = cleaned.lower()

    if remove_punctuation:
        # Remove punctuation but keep spaces
        cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))
        # Clean up extra spaces again
        cleaned = re.sub(r"\s+", " ", cleaned.strip())

    return cleaned


def count_words(text: str) -> int:
    """
    Count the number of words in a text.

    Args:
        text: Input text

    Returns:
        Number of words
    """
    if not text or not text.strip():
        return 0

    # Split by whitespace and count non-empty elements
    words = text.strip().split()
    return len(words)


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text.

    Args:
        text: Input text to search

    Returns:
        List of email addresses found
    """
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.findall(email_pattern, text)


def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text.

    Args:
        text: Input text to search

    Returns:
        List of URLs found
    """
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    return re.findall(url_pattern, text)


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: Input text to truncate
        max_length: Maximum length of the result
        suffix: Suffix to add when truncating

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text

    if max_length <= len(suffix):
        return suffix[:max_length]

    return text[: max_length - len(suffix)] + suffix


def capitalize_words(text: str, exceptions: Optional[List[str]] = None) -> str:
    """
    Capitalize the first letter of each word, with exceptions.

    Args:
        text: Input text
        exceptions: List of words that should not be capitalized

    Returns:
        Text with capitalized words
    """
    if exceptions is None:
        exceptions = [
            "a",
            "an",
            "and",
            "as",
            "at",
            "but",
            "by",
            "for",
            "if",
            "in",
            "nor",
            "of",
            "on",
            "or",
            "so",
            "the",
            "to",
            "up",
            "yet",
        ]

    words = text.split()
    result = []

    for i, word in enumerate(words):
        # Always capitalize the first word
        if i == 0 or word.lower() not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return " ".join(result)


def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text.

    Args:
        text: Input text with HTML tags

    Returns:
        Text with HTML tags removed
    """
    html_pattern = re.compile("<.*?>")
    return html_pattern.sub("", text)


def snake_to_camel(snake_str: str) -> str:
    """
    Convert snake_case to camelCase.

    Args:
        snake_str: String in snake_case

    Returns:
        String in camelCase
    """
    components = snake_str.split("_")
    return components[0] + "".join(word.capitalize() for word in components[1:])


def camel_to_snake(camel_str: str) -> str:
    """
    Convert camelCase to snake_case.

    Args:
        camel_str: String in camelCase

    Returns:
        String in snake_case
    """
    # Insert an underscore before any uppercase letter that follows a lowercase letter
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_str)
    # Insert an underscore before any uppercase letter that follows a lowercase letter or number
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def generate_slug(text: str, max_length: int = 50) -> str:
    """
    Generate a URL-friendly slug from text.

    Args:
        text: Input text
        max_length: Maximum length of the slug

    Returns:
        URL-friendly slug
    """
    # Convert to lowercase and remove special characters
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    # Replace spaces and multiple hyphens with single hyphens
    slug = re.sub(r"[-\s]+", "-", slug)
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    # Truncate if necessary
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip("-")

    return slug
