############################
Cookiecutter Sphinx template
############################

Setup
#####

Install the following packages via pip:

cookiecutter
  Cookiecutter is a python application that can create project directories
  from premade templates dubbed "Cookiecutters".


Generate your documentation directory
======================================
Open a command line in the folder you want your documentation directory to be.
Then create your documentation with this command (change path of template if necessary).

.. code-block:: sh

    cookiecutter gh:ihmeuw/rra-doc-template

You can also do this over ssh if you have ssh keys configured to skip the login prompt.

.. code-block:: sh

    cookiecutter git@github.com:ihmeuw/rra-doc-template.git

Cookiecutter asks you to enter all the information about your project (author,
project name, description, etc.) and then generates your documentation in the specified
folder (``docs`` by default).

Write the docs
===============
After you have set up Sphinx, you can write your documentation as a set of .rst files
that you put in the main directory.

Dont forget to insert the filenames into the table of contents located in the
``index.rst`` file. Otherwise your documentation wont show up on the final page.

You can write your documentation with any text editor you like. If you're using VSCode
there is an extension available (``lextudio.restructuredtext``) that enables syntax
highlighting and autocompletion.

Build the docs
===============
Once you have written your documentation, you have to build it. Sphinx will take your
RST files, parse them and generate production-ready output data in html and docx format.

.. todo::
    Add instructions for building the docs
