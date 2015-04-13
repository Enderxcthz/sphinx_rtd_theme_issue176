sphinx_rtd_theme_issue176
=========================

Document Template Testing
=========================
This documents the troubleshooting procedures followed to determine the cause of the 'Table of Contents' not displaying in the 'rtd_theme'. It's issue number 176_ of snide/sphinx_rtd_theme. 

.. _176: https://github.com/snide/sphinx_rtd_theme/issues/176

1. Developed rainbowsUnicorns.py in C:\sphinxTests.
2. Used DOS Command Prompt to run Sphinx-quickstart in the directory.
3. Edited the index.rst and made the following changes:
    -Added::
        .. automodule:: rainbowsUnicorns
            :members:

4. Edited conf.py and uncommented:
    sys.path.insert(0, os.path.abspath('.'))

Alabaster HTML Theme
====================
5. Ran 'make html' using default 'Alabaster' theme.
    .. NOTE:: This theme has a table of contents on the left side, as it should.
6. Renamed .\\_build\\html\\index.html to 'index_alabaster.html'. 

Read the Docs HTML Theme
========================
7. Edited conf.py and added::
    # Import the _Read the Docs Theme: http://docs.readthedocs.org/en/latest/theme.html
    import sphinx_rtd_theme

    # Read the Docs Theme
    html_theme = ('sphinx_rtd_theme')

    # Get the path to the Read the Docs Theme
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
8. Commented out "html_theme = 'alabaster'"
9. Ran 'make html' using 'phinx_rtd_theme' theme.
    .. NOTE:: This theme does NOT have a table of contents on the left side, as it should.
10. Renamed .\_build\html\index.html to 'index_readTheDocs.html'

Classic Theme
=============
11. Edited conf.py and added::
    html_theme = 'classic'
12. Commented out html_theme = ('sphinx_rtd_theme') and it's components.
13. Ran 'make html' using 'classic' theme.
    .. NOTE:: This theme has a table of contents on the left side, as it should.
14. Renamed .\_build\html\index.html to 'index_classic.html'