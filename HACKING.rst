===================
Hacking Style Guide
===================

The Zen of Python
-----------------

PEP 20::

        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
            -- https://www.python.org/dev/peps/pep-0020/ 
                                                             
easter egg::

        #!/usr/bin/env python
        import this
 
General Governance
------------------

Imports
~~~~~~~

* Do not import objects, only modules (*)
* Do not import more than one module per line (*)
* Do not use wildcard * import (*)
* Do not make relative imports
(*) exceptions are:
* function imports from i18n module

Dictionaries/Lists
~~~~~~~~~~~~~~~~~~

* If a dictionary (dict) or list object is longer than 80 characters, its items should be split with newlines. Embedded iterables should have their items indented. Additionally, the last item in the dictionary should have a trailing comma. This increases readability and simplifies future diffs.

Calling Methods
~~~~~~~~~~~~~~~

* Calls to methods 80 characters or longer should format each argument with newlines. This is not a requirement, but a guideline.

Other
~~~~~

* Use only UNIX style newlines (\n), not Windows style (\r\n)
* It is preferred to wrap long lines in parentheses and not a backslash for line continuation.
* Do not write except:, use except Exception: at the very least. When catching an exception you should be as specific so you don’t mistakenly catch unexpected exceptions.
* Don’t put vim configuration in source files (off by default).
* Do not shadow a built-in or reserved word. Shadowing built -in or reserved words makes the code harder to understand.

PEP 8
~~~~~

*  Step 1: Read pep8
*  Step 2: Read pep8 again
*  Step 3: Read on

All python code should first and foremost follow PEP8 guidelines.

*  https://www.python.org/dev/peps/pep-0008/ ( read more here )
*  https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code ( read more here as well )
*  http://docs.python-guide.org/en/latest/writing/style/ ( also worth reading )

File Headers
~~~~~~~~~~~~

Every class class should have a header comment section, describing the purpose of the class and the key apis.  adding an (initial) author is optional but good practice.

Docstrings
~~~~~~~~~~
*  Docstrings should not start with a space.
*  Multi line docstrings should end on a new line.
*  Multi line docstrings should start without a leading new line.
*  Multi line docstrings should start with a one line summary followed by an empty line.

Sample
~~~~~~
ref ( http://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files ):
Example File Header::
        #!/usr/bin/env python
        
        '''
        Execution:
             sample.py --<long flag> -<short flag> <some arguments>
        Purpose:
             process does something
        '''
        
        __author__ = 'Matt Joyce'
        __email__ = 'matt@joyce.nyc'
        __copyright__   = "Copyright 2016, Example Co."
        
        import os
        import sys
        
        from symphony import Config
        
        
        if __name__ == "__main__":
                sym = Config(config)
 
Comments
~~~~~~~~
*  Each public api should have clear comments on how it should be used and when.
*  Each private api should have comments that describe implementation.

 
Commit Messages
~~~~~~~~~~~~~~~
*  Using a common format for commit messages will help keep our git history readable.
*  Tag all commits with a corresponding JIRA ticket, where applicable, followed by a SHORT description of the commit. 

Unit Testing
~~~~~~~~~~~~
*  unittest2 is the python2.7 defacto standard for unittesting modules.
*  we use tox to kick off tests, and mock for mocking up rest api method calls
*  For every new feature, unit tests should be created that both test and (implicitly) document the usage of said feature. If submitting a patch for a bug that had no unit test, a new passing unit test should be added. If a submitted bug fix does have a unit test, be sure to add a new one that fails without the patch and passes with the patch.

Unit Tests and assertRaises
~~~~~~~~~~~~~~~~~~~~~~~~~~~
*  A properly written test asserts that particular behavior occurs. This can be a success condition or a failure condition, including an exception. When asserting that a particular exception is raised, the most specific exception possible should be used.
*  Testing for Exception being raised is almost always a mistake since it will match (almost) every exception, even those unrelated to the exception intended to be tested.
*  This applies to catching exceptions manually with a try/except block, or usingassertRaises().
  - https://pypi.python.org/pypi/unittest2 ( Read More )
  - http://www.drdobbs.com/testing/unit-testing-with-python/240165163 ( Read even more )
*  please unittest, EVERYTHING.  If you see something not unit tested in a pull request, ask for unit tests before merging it.  integrate the unittest creation process into your prototyping of methods and functions, for the best experience in development.
 
Input Validation
~~~~~~~~~~~~~~~~
*  See PEP 8.
*  See Unit Testing.
*  assert what's absolutely essential.
*  All input should be validated, and tested in unit tests, and functional tests BEFORE code is merged.

Error Handling
~~~~~~~~~~~~~~
- https://docs.python.org/2.7/tutorial/errors.html ( Read More )

Logging
~~~~~~~
- http://docs.python-guide.org/en/latest/writing/logging/ ( Read More )
