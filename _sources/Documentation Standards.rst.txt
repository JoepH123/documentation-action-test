Documentation Standards
============================

Decisions on software and formatting
--------------------------------------------------------------
As has been discussed, Sphinx is the tool that is used for the creation of the documentation of the KGA project. It uses the documentation extracted from docstrings in python files together with other hand-written documentation files to form a complete and well-structured documentation page, which can be viewed in the browser. For the composition of docstrings, we use numpydoc. This is the documentation format which is used for the development of the NumPy project. It is a easily interpretable and well organized documentation format, which can be viewed in more detail on their website (numpydoc_). For the hand-written documentation files, which are used to create more in-depth and topic specific documentation, reStructuredText (RST) is used. This is a markup language that can be used to write beautiful documentations with many customizing options. This (.rst) file type and the language allow you to add in pictures, videos, code blocks, hyperlinks etc. to the documentation. For some examples, you can visit reStructuredText_, sphinx-RST_ and sphinx-RST-syntax-guide_ or you can google more specific questions.



.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/install.html
.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html#external-hyperlink-targets
.. _sphinx-RST: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _sphinx-RST-syntax-guide: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html

Rules and Principles for Documentation in KGA
------------------------------------------------------------------
First of all, documentation consists of comments and docstrings. Both comments and docstrings have a maximum line length of
72 characters.

Commenting
~~~~~~~~~~~~~~~~
**Purposes of comments:**

- Planning and reviewing. Outlining the structure of the code and what has to be done. These comments are removed as soon as it has been completed.
- Code description. Elaboration on some of the code that is unclear.
- Algorithmic description. Roughly describing the workings of an algorithm or mentioning what algorithm was used for some task.
- Tagging. TODO, BUG, FIXME, etc..

**Rules for comments:**

- Comments close to the corresponding code.
- No redundant info. Assume basic understanding of programming principles and language syntax.
- Make the code self-explanatory. Easy-to-understand, clear principles and naming should be appropriate.

*Type hinting* can be useful to make the code itself more interpretable:

.. code-block:: python

   def hello_name(name: str) -> str:

Docstrings
~~~~~~~~~~~~~~~~
**Basics**

These are built-in strings that, when configured correctly, can help your users and yourself with your project’s documentation.

Their purpose is to provide your users with a brief overview of the object. They should be kept concise enough to be easy to maintain but still be elaborate enough for new users to understand their purpose and how to use the documented object.

Along with docstrings, Python also has the built-in function help() that prints out the objects docstring to the console:

.. code-block:: python

   say_hello.__doc__ = "A simple function that says hello... Richie style"
   help(say_hello)
   say_hello(name)
      A simple function that says hello... Richie style

So you can set a docstring using ‘function_name.__doc__ = …’. This does not work for altering the docstrings of existing objects like the string object.

You can also define a docstring by using triple quotation marks:

.. code-block:: python

   def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")

**Docstring types**

- At a bare minimum, a docstring should be a quick summary of whatever is it you’re describing and should be contained within a single line (not really used in the KGA project)

.. code-block:: python

   """This is a quick summary line used as a description of the object."""

- Multi-lined docstrings are used to further elaborate on the object beyond the summary. All multi-lined docstrings should include:
   - A one-line summary
   - A blank line proceeding the summary
   - Any further elaboration for the docstring (parameters, returns, etc. see numpydoc_ documentation)
   - Another blank line

.. code-block:: python

   """This is the summary line

    This is the further elaboration of the docstring. Within this section,
    you can elaborate further on details as appropriate for the situation.
    Notice that the summary and the elaboration is separated by a blank new
    line.
    """

    # Continuation of code

.. note::
   In the KGA project, multi-lined docstrings are the norm and single-lined docstrings should not be used.

**What should docstrings (at least) include**

*Class Docstrings: Classes and Class Methods*

Class Docstrings are created for the class itself, as well as any class methods. The docstrings are placed immediately following the class or class method indented by one level:

1. Class docstrings should contain the following information:

   - A brief summary of its purpose and behavior
   - Any public methods, along with a brief description
   - Any class properties (attributes)
   - Anything related to the interface for subclassers, if the class is intended to be subclassed

2. The class constructor parameters should be documented within the __init__ class method docstring.

3. Individual methods should be documented using their individual docstrings. Class method docstrings should contain the following:

   - A brief description of what the method is and what it’s used for
   - Any arguments (both required and optional) that are passed including keyword arguments
   - Any returns of the class method
   - Label any arguments that are considered optional or have a default value
   - Any side effects that occur when executing the method
   - Any exceptions that are raised
   - Any restrictions on when the method can be called

*Package and Module Docstrings: Package, modules, and functions*

A package is basically a python project, the different python files are the modules and in a module many functions can
be defined. A python project with different python files always has an __init__.py file.

1. Package docstrings

   - Placed at the top of the package’s __init__.py file. This docstring should list the modules and sub-packages that are exported by the package.

2. Module docstrings: Similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within. Module docstrings are placed at the top of the file even before any imports. Module docstrings should include the following:

   - A brief description of the module and its purpose
   - A list of any classes, exceptions, functions and any other objects exported by the module.

3. Function docstrings: The docstring for a module function should include the same items as a class method:

   - A brief description of what the function is and what it’s used for
   - Any arguments (both required and optional) that are passed including keyword arguments
   - Any returns of the function
   - Label any arguments that are considered optional
   - Any side effects that occur when executing the function
   - Any exceptions that are raised
   - Any restrictions on when the function can be called



