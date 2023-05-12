:orphan:

##############
RST Cheatsheet
##############

Restructured text
#################

RST stands for "Restructured text" and is a simple markup language. It is more
powerful than Markdown while being a lot easier for humans to read and understand
than for example TeX or HTML.

Here is a quick overview of the most important features that you'll have
to learn.

https://github.com/ralsina/rst-cheatsheet

https://sphinx-tutorial.readthedocs.io/cheatsheet/

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html

Document structure
===================
You can create headlines by under/overlining your heading with special characters.
Different types of characters result in different headline levels.

There is no special rule about which character to use, but you should keep
consistency within your documentation.

.. code-block:: rst

    #################################
    RRA Documentation Sphinx Template
    #################################
    ...

    Restructured text
    #################
    RST stands for "Restructured text"...

    Document structure
    ===================
    You can create headlines by under/overlining your heading...

    Headline Level 4
    *****************
    Cupcake ipsum dolor sit amet gummies danish...

    Headline Level 5
    -----------------
    Gummies jelly chocolate bar candy. Danish...

Inline formatting
==================
If you have already used Markdown, you will be familiar with using single ``*text*`` for
*italic* text and double ``**text**`` for **bold** text.

But there are some more interesting options or roles, as they are called.
You can apply a role to your text by putting it in quotes and writing the role before it.

.. code-block:: rst

    Press :kbd:`Ctrl+C` to copy.

**:kbd:**
    Mark a key or key combination. Press :kbd:`Ctrl+C` to copy.
**:guilabel:**
    Describe a button or input field in your software's UI. Press :guilabel:`OK` to continue.

All roles are documented here: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html

Lists
======
Bullet point lists are easy. Just use either ``-`` or ``*`` as a bullet point
and indent sub-lists using tabs. Note that sub-lists must be separated from the main list
by blank lines.

.. code-block:: rst

    - Operating systems

        - Windows
        - Linux
        - MacOS

    - Programming languages

        - C++
        - Java
        - Python
        - Brainf*ck

- Operating systems

    - Windows
    - Linux
    - MacOS

- Programming languages

    - C++
    - Java
    - Python
    - Brainf*ck

Numbered lists are just as simple. Use ``#.``, the numbering is handled by Sphinx.

.. code-block:: rst

    #. Get up
    #. Put on your clothes

        #. Shirt
        #. Pants
        #. Socks

    #. Have breakfast
    #. Start coding


#. Get up
#. Put on your clothes

    #. Shirt
    #. Pants
    #. Socks

#. Have breakfast
#. Start coding


Tables
=================
There are multiple ways to create tables using sphinx.

Simple table
*************
Simple tables use spaces as horizontal and "equals" charcters as vertical delimiters.

.. code-block:: rst

    ============  ============
    Header 1      Header 2
    ============  ============
    body row 1    column 2
    body row 2    column 2
    ============  ============

============  ============
Header 1      Header 2
============  ============
body row 1    column 2
body row 2    column 2
============  ============

Complex table
**************
Complex tables use various special characters as delimiters in order to create
a beautiful spreadsheet look using ASCII only.
I would not recommend using them since they are a mess to create and edit

.. code-block:: rst

    +------------+------------+-----------+
    | Header 1   | Header 2   | Header 3  |
    +============+============+===========+
    | body row 1 | column 2   | column 3  |
    +------------+------------+-----------+
    | body row 2 | Cells may span columns.|
    +------------+------------+-----------+
    | body row 3 | Cells may  | - Cells   |
    +------------+ span rows. | - contain |
    | body row 4 |            | - blocks. |
    +------------+------------+-----------+

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

List table
*************
List tables are basically lists of lists, which form table rows and columns.
The principle is similar to HTML tables. They dont look like a table in the source file,
but they are way nicer to work with. That's why they are my favourite option.

.. code-block:: rst

    .. list-table::
        :widths: 15 10 30
        :header-rows: 1

        * - Treat
          - Price
          - Description
        * - Albatross
          - 2.99
          - On a stick!
        * - Crunchy Frog
          - 1.49
          - If we took the bones out, it wouldn't be crunchy, now would it?
        * - Gannet Ripple
          - 1.99
          - On a stick!

.. list-table::
    :widths: 15 10 30
    :header-rows: 1

    * - Treat
      - Price
      - Description
    * - Albatross
      - 2.99
      - On a stick!
    * - Crunchy Frog
      - 1.49
      - If we took the bones out, it wouldn't be crunchy, now would it?
    * - Gannet Ripple
      - 1.99
      - On a stick!


CSV table
**********
You'll find out quickly that plain text editors are not the perfect tool for working with
tables. That's why there is another option: CSV.

Here is a small CSV table that I created using Excel.
You can import it using the ``csv-table`` directive.

.. code-block:: rst

    .. csv-table::
        :header-rows: 1
        :delim: ;

        Amount;Product;Art.Nr.;Price
        1;Intel Core i7;26487;349 €
        2;24 inch monitor;14238;240 €
        6;micro USB cable;94125;9€

Instead of copying the raw CSV into your document, you can put the CSV file into your
documentation folder and have Sphinx import it, too.

.. code-block:: rst

    .. csv-table::
        :file: csv/table.csv
        :header-rows: 1
        :delim: ;

.. csv-table::
    :header-rows: 1
    :delim: ;

    Amount;Product;Art.Nr.;Price
    1;Intel Core i7;26487;349 €
    2;24 inch monitor;14238;240 €
    6;micro USB cable;94125;9€

Images
=======
To include images in your documentation, put the files in the img folder (or anywhere else
within the docs directory) and reference them from an image directive.

.. code-block:: rst

    .. image:: img/demo.jpg
        :height: 300px

If you need to include an image from a web site, you can reference them via the URL directly.

.. code-block:: rst

    .. image:: https://images.unsplash.com/photo-1502877338535-766e1452684a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&h=300&q=80

.. image:: https://images.unsplash.com/photo-1502877338535-766e1452684a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&h=300&q=80
    :height: 300px

You can add options to the image directive for further customization.

**:alt:** Alternative text shown if the image can't be displayed (or spoken to visually impaired users)

**:width: / :height:** Image size

**:scale:** Uniform image scaling in percent

**:align:** Image alignment (top, middle, bottom, left, center, right)

**:target:** Link target (URL or reference name, see :ref:`0_demo:Hyperlinks` )

Hyperlinks
===========

URLs starting with ``http://`` or ``https://`` like
for example https://google.com are turned into links automatically.

You can create links with alternative text like `GitHub <https://github.com>`_ by putting the URL
in angle brackets:

.. code-block:: rst

     `GitHub <https://github.com>`_

Links to a section within your documentation are created using ``:ref:`file:Title```,
for example :ref:`0_demo:Hyperlinks`.

.. code-block:: rst

    :ref:`0_demo:Hyperlinks`

To use alternative text for an internal link, put the section title in angled brackets
with the alternative text before it:

.. code-block:: rst

    :ref:`index page<index:{{ cookiecutter.project_name }}>`

Code
=====
Code can be included inline and in blocks. Code blocks also come with
syntax highlighting.

.. code-block:: rst

    .. code-block:: python

        def hello_world():
            print('Hello World')

    Call ``hello_world()`` and look at the console output!

results in this:

.. code-block:: python

        def hello_world():
            print('Hello World')

Call ``hello_world()`` and look at the console output!

Admonitions
============
Admonitions can be used to prominently mention important details
of your documentation. Sphinx comes with lots of different types!

.. code-block:: rst

    .. danger::
        Mad scientists at work!

.. danger::
    Mad scientists at work!

.. error::
    Does not compute

.. attention::
    Directives at large.

.. caution::
    Don't take wooden nickels.

.. warning::
    Strong prose may provoke extreme mental exertion. Reader discretion is strongly advised.

.. important::
    Call your mother

.. hint::
    It’s bigger than a bread box.

.. note::
    Buy one liter of milk. And if they have eggs, get 6.

.. tip::
    15% if the service is good

.. seealso::
    Look over there
