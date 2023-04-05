from setuptools import setup, find_packages

setup(
    name="my-package",
    version="0.1.0",
    author="Your Name",
    description="A short description of your package",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.16.0",
        "pandas>=0.24.0",
        "matplotlib>=3.0.0"
    ]
)
