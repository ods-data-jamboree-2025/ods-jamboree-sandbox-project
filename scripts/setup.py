#!/usr/bin/env python3
"""
Setup script for the ODS Data Jamboree Sandbox Project.

This script helps set up the development environment and run common tasks.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description=""):
    """Run a shell command and print the result."""
    if description:
        print(f"🔧 {description}...")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_dependencies():
    """Install project dependencies."""
    commands = [
        ("pip install -r requirements.txt", "Installing core dependencies"),
        ("pip install -r requirements-dev.txt", "Installing development dependencies"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True


def run_tests():
    """Run the test suite."""
    return run_command("pytest -v", "Running tests")


def format_code():
    """Format code with black and isort."""
    commands = [
        ("black src/ tests/", "Formatting code with black"),
        ("isort src/ tests/", "Sorting imports with isort"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True


def lint_code():
    """Lint code with flake8."""
    return run_command("flake8 src/ tests/", "Linting code with flake8")


def check_code():
    """Check code formatting and linting."""
    commands = [
        ("black --check src/ tests/", "Checking code formatting"),
        ("isort --check-only src/ tests/", "Checking import sorting"),
        ("flake8 src/ tests/", "Linting code"),
    ]
    
    all_passed = True
    for command, description in commands:
        if not run_command(command, description):
            all_passed = False
    
    return all_passed


def run_examples():
    """Run example scripts."""
    examples = [
        "src/examples/hello_world.py",
        "src/examples/data_analysis.py",
        "src/data_processing/csv_processor.py",
    ]
    
    for example in examples:
        if Path(example).exists():
            print(f"\n{'='*50}")
            print(f"Running {example}")
            print('='*50)
            run_command(f"python {example}", f"Running {example}")
    
    return True


def main():
    """Main setup function."""
    print("🎉 ODS Data Jamboree Sandbox Project Setup")
    print("=" * 50)
    
    if len(sys.argv) < 2:
        print("Usage: python scripts/setup.py <command>")
        print("\nAvailable commands:")
        print("  install    - Install dependencies")
        print("  test       - Run tests")
        print("  format     - Format code")
        print("  lint       - Lint code")
        print("  check      - Check code quality")
        print("  examples   - Run example scripts")
        print("  all        - Run install, format, lint, and test")
        return
    
    command = sys.argv[1].lower()
    
    # Check Python version first
    if not check_python_version():
        sys.exit(1)
    
    success = True
    
    if command == "install":
        success = install_dependencies()
    elif command == "test":
        success = run_tests()
    elif command == "format":
        success = format_code()
    elif command == "lint":
        success = lint_code()
    elif command == "check":
        success = check_code()
    elif command == "examples":
        success = run_examples()
    elif command == "all":
        success = (
            install_dependencies() and
            format_code() and
            check_code() and
            run_tests()
        )
    else:
        print(f"❌ Unknown command: {command}")
        success = False
    
    if success:
        print("\n✅ Command completed successfully!")
    else:
        print("\n❌ Command failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()