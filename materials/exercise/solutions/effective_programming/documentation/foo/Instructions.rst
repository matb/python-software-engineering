Instruction
============

type-hints, docstrings and documentation
----------------------------------------------------------------


To get started lets first have a look at the foo.Foo class and its in-place documentation. 
To create a good codebase one should always create appropriate docstrings for (at least high-level)  methods and functions.
Additionaly it is good practice to always add type-hints to let the user know what type to expect. 

Now in Foo you can see the basics of docstring and type-hints. 
The Foo class defined two methods with the same functionality:
receiving a name and greeting it.
The only difference is that one is using Google-style (napoleon) doctstrings while the other one uses reStructedText (sphinx) docstrings. 
**Please note - never do this in real code. Always use one stile in your code even better in your team, department, or even company.**
There are even more out there but this are the most common ones. Nevertheless Sphinx document generation support both as we will see later.

Task1 
~~~~~~~~~~~~~~~~~~~~~

First, there is an issue with the type-hints and this needs to be fixed. Can you spot it ? 


Task2
~~~~~~~~~~~~~~~~~~~~~
Use mypy to help you spot issues with the docstrings. 

Task3
~~~~~~~~~~~~~~~~~~~~~

create a new folder called `docs` and navigate inside. 
In the folder run `sphinx-quickstart` and fill out the questions
Have a look into the created files and folder. 
In the source folder you will find a conf.py and an index.rst. 
Lets first change our conf.py by appending the following:

.. code-block:: python
    # Allow sphinx to read the foo package files
    import os 
    import sys 
    sys.path.insert(0, os.path.abspath('..')) 

    #Define a few extensions we want to use 
    extensions = [
        'sphinx.ext.autodoc', # User the functionality to automatically create documentation from code
        'sphinx.ext.napoleon' # Allow us to use google docstring - depends on what you want to use / used in the code 
        ]
Please also delete the line 17 with ` extensions = []`

Next up is the index.rst which looks like this (ignoring the comment at the beginning of the file):

.. code-block:: rst

        Welcome to foo's documentation!
    ===============================

    .. toctree::
    :maxdepth: 2
    :caption: Contents:



    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

The `.. toctree::` is the directive for sphinx - what it should plug in. 
We are now going to append this s.t. sphinx will automatically add the documentation of our code: 

.. code-block:: reStructedText

    Welcome to Getting Started with Sphinx's documentation!
    =======================================================
    .. automodule:: foo.foo
        :members:
    .. toctree::
    :maxdepth: 2
    :caption: Contents:
    Indices and tables
    ==================
    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

Now build the documentation by going into the doc folder and build the documentation by either using  `make build` or `sphinx build source/ build/`
Now you can navigate to the build/index.html file and open it in the browser. 


Task4
~~~~~~~~~~~~~~~~~~~~

Lets add a litte more structure by creating a specific code page. 
1. Create a code.rst file in the docs/source folder. 
2. Within this file create a small Header welcoming the user to the code documentation and a few words as paragraphs
3. Cut the  `.. automodule:: foo.foo ` part (including the `:members:`) from the index.rst and move it over to your new code.rst
4. modify the index.rst by adding the a line to include our code.rst :
.. code-block:: 

    Welcome to foo's documentation!
    ===============================

    .. toctree::
    :maxdepth: 2
    :caption: Contents:

    code

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

5. rebuild the documentation as above. 