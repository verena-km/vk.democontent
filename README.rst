.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.



==============
vk.democontent
==============

Simple Addon for adding sample content to Plone site for testing purposes.

Features
--------
Adds a view to your Plone site for generating sample content in the current folder:

The following content types can be generated:

- Folder
- Document
- News Item
- Link
- File (pdf, docx, xlsx)
- Image

This Addon uses ``lorem``, ``reportlab``, ``python-docx`` and ``XlsWriter`` and the
generman wordlist ``wortliste.txt`` from https://codeberg.org/davidak/wortliste/src/branch/master/wortliste.txt


Usage
--------

If you have admin permission you will find an object action `Beispielinhalte hinzufügen` in every folderish object.
Select the number of elements to add for each content type. For folders you can define the maximal depth for the nested
folders.

The content will be randomly in the new subfolders

Translations
------------
TODO


Installation
------------

Install vk.democontent by adding it to your buildout::

    [buildout]

    ...

    eggs =
        vk.democontent


and then running ``bin/buildout``


Authors
-------

Provided by awesome people ;)


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/verena-km/vk.democontent/issues
- Source Code: https://github.com/verena-km/vk.democontent

Support
-------

If you are having issues, please let us know.

License
-------

The project is licensed under the GPLv2.
