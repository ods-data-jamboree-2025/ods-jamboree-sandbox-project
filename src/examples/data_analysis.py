#!/usr/bin/env python3
"""
Data Analysis Example

A sample data analysis script demonstrating common data science workflows.
This script can be used to test:
- Data manipulation with pandas
- Basic visualizations with matplotlib
- Statistical operations with numpy
- File I/O operations
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_sample_data(n_samples: int = 100) -> pd.DataFrame:
    """
    Generate sample data for analysis.

    Args:
        n_samples: Number of data points to generate

    Returns:
        DataFrame with sample data
    """
    np.random.seed(42)  # For reproducible results

    data = {
        "x": np.random.randn(n_samples),
        "y": np.random.randn(n_samples) * 2 + 1,
        "category": np.random.choice(["A", "B", "C"], n_samples),
        "value": np.random.uniform(10, 100, n_samples),
    }

    return pd.DataFrame(data)


def analyze_data(df: pd.DataFrame) -> dict:
    """
    Perform basic data analysis.

    Args:
        df: Input DataFrame

    Returns:
        Dictionary with analysis results
    """
    analysis = {
        "shape": df.shape,
        "summary_stats": df.describe(),
        "correlation": df.corr(numeric_only=True),
        "category_counts": df["category"].value_counts(),
    }

    return analysis


def create_visualization(df: pd.DataFrame, output_dir: str = "plots") -> None:
    """
    Create and save visualizations of the data.

    Args:
        df: Input DataFrame
        output_dir: Directory to save plots
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)

    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Sample Data Analysis", fontsize=16)

    # Scatter plot
    axes[0, 0].scatter(df["x"], df["y"], alpha=0.6)
    axes[0, 0].set_title("X vs Y Scatter Plot")
    axes[0, 0].set_xlabel("X")
    axes[0, 0].set_ylabel("Y")

    # Histogram
    axes[0, 1].hist(df["value"], bins=20, alpha=0.7, edgecolor="black")
    axes[0, 1].set_title("Value Distribution")
    axes[0, 1].set_xlabel("Value")
    axes[0, 1].set_ylabel("Frequency")

    # Box plot by category
    categories = df["category"].unique()
    category_data = [df[df["category"] == cat]["value"] for cat in categories]
    axes[1, 0].boxplot(category_data, labels=categories)
    axes[1, 0].set_title("Value by Category")
    axes[1, 0].set_xlabel("Category")
    axes[1, 0].set_ylabel("Value")

    # Correlation heatmap
    corr_matrix = df.corr(numeric_only=True)
    im = axes[1, 1].imshow(corr_matrix, cmap="coolwarm", aspect="auto")
    axes[1, 1].set_title("Correlation Matrix")
    axes[1, 1].set_xticks(range(len(corr_matrix.columns)))
    axes[1, 1].set_yticks(range(len(corr_matrix.columns)))
    axes[1, 1].set_xticklabels(corr_matrix.columns)
    axes[1, 1].set_yticklabels(corr_matrix.columns)

    # Add colorbar
    plt.colorbar(im, ax=axes[1, 1])

    plt.tight_layout()
    plt.savefig(f"{output_dir}/data_analysis.png", dpi=300, bbox_inches="tight")
    print(f"📊 Visualization saved to {output_dir}/data_analysis.png")


def main():
    """Main function to run the data analysis example."""
    print("🔬 Running Data Analysis Example")
    print("=" * 40)

    # Generate sample data
    print("📊 Generating sample data...")
    df = generate_sample_data(200)
    print(f"Generated dataset with shape: {df.shape}")

    # Analyze data
    print("\n🔍 Analyzing data...")
    analysis = analyze_data(df)

    print(f"Dataset shape: {analysis['shape']}")
    print("\nSummary statistics:")
    print(analysis["summary_stats"])

    print("\nCategory distribution:")
    print(analysis["category_counts"])

    # Create visualizations
    print("\n📈 Creating visualizations...")
    try:
        create_visualization(df)
    except Exception as e:
        print(f"Note: Could not save plot - {e}")
        print("(This is normal if matplotlib backend doesn't support file saving)")

    print("\n✅ Analysis complete!")
    print("💡 Try modifying this script to:")
    print("   - Change the sample data generation")
    print("   - Add new analysis functions")
    print("   - Create different types of plots")


if __name__ == "__main__":
    main()
