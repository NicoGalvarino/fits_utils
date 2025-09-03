from setuptools import setup, find_packages

setup(
    name="fits_utils",
    version="0.1.0",
    description="Utilities for working with FITS files and pandas DataFrames",
    author="Nicolas Guerra Varas",
    author_email="nicolas.guerravaras@eso.org",
    packages=find_packages(),
    py_modules=["fits_utils"],
    install_requires=[
        "astropy",
        "pandas",
        "numpy",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
