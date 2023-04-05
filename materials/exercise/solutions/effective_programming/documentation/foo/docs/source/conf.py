# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'foo'
copyright = '2023, Matthias'
author = 'Matthias'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# Extension necessary 

# Allow sphinx to read the foo package files
import os 
import sys 
sys.path.insert(0, os.path.abspath('..')) 

#Define a few extensions we want to use 
extensions = [
    'sphinx.ext.autodoc', # User the functionality to automatically create documentation from code
    'sphinx.ext.napoleon' # Allow us to use google docstring - depends on what you want to use / used in the code 
    ]