# setup.py placed at root directory
from setuptools import setup, find_packages

setup(
    name="my-package",
    version="0.1.0",
    author="Your Name",
    description="A short description of your package",
    author_email= 'matthias.baumann@ultratendency.com',
    long_description='This is a longer description for the project',
    url='https://ultratendeny.com/',
    keywords='sample, example, setuptools',
    python_requires='>=3.7, <4',
    install_requires=[
        "numpy>=1.16.0",
        "pandas>=0.24.0",
        "matplotlib>=3.0.0"
    ],
    packages=find_packages(),
    extras_require={
        'test': ['pytest', 'coverage'],
    },
    package_data={
        'sample': ['example_data.csv'],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)

