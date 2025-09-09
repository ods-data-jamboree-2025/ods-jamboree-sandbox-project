#!/usr/bin/env python3
"""
Hello World Example

A simple example script to demonstrate basic Python functionality.
This script can be used to test:
- Basic Python execution
- Import statements
- Function definitions
- Command-line arguments
"""

import sys
from datetime import datetime


def greet(name: str = "World") -> str:
    """
    Generate a greeting message.

    Args:
        name: The name to greet (default: "World")

    Returns:
        A greeting message string
    """
    return f"Hello, {name}!"


def get_current_time() -> str:
    """
    Get the current date and time as a formatted string.

    Returns:
        Current timestamp as a string
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    """Main function to demonstrate the script functionality."""
    print("🎉 Welcome to the ODS Data Jamboree 2025 Sandbox!")
    print("=" * 50)

    # Check for command-line arguments
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    else:
        name = "Participant"

    # Generate and display greeting
    greeting = greet(name)
    current_time = get_current_time()

    print(f"{greeting}")
    print(f"Current time: {current_time}")
    print("\nThis is a sandbox environment - feel free to modify this script!")
    print("Try running with your name: python hello_world.py Your Name")


if __name__ == "__main__":
    main()
