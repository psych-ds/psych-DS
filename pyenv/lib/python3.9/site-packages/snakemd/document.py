"""
The document module houses the Document class, a tool for
generating markdown documents.
"""
from __future__ import annotations

import logging
import os
import pathlib
import random
from typing import Iterable

from .elements import (
    Block,
    Code,
    Element,
    Heading,
    HorizontalRule,
    Inline,
    MDList,
    Paragraph,
    Quote,
    Raw,
    Table,
)
from .templates import TableOfContents, Template

logger = logging.getLogger(__name__)


class Document:
    """
    A document represents a markdown file. Documents store
    a collection of elements which are appended with new lines
    between to generate the markdown document. Document methods
    are intended to provided convenience when generating a
    markdown file. However, the functionality is not exhaustive.
    To get the full range of markdown functionality, you can
    take advantage of the :func:`add_block` function to provide
    custom markdown blocks.

    .. testsetup:: document

        import snakemd

    .. testcleanup:: document

        import os
        os.remove("README.md")

    :param list[Element] elements:
        an optional list of elements that make up a markdown document

        .. versionadded:: 2.2
            Included to make __repr__ more useful
    """

    def __init__(self, elements: list[Element] = None) -> None:
        self._elements: list[Element] = elements or []
        logger.info("Created new document: %r", self)

    def __str__(self) -> str:
        """
        Renders the markdown document from a list of elements.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_heading("First")
            Heading(text=[...], level=1)
            >>> print(doc)
            # First

        :return:
            the document as a markdown string
        """
        # load templates
        for block in self._elements:
            if isinstance(block, Template):
                block.load(self._elements)
        # render all
        document = "\n\n".join(str(block) for block in self._elements)
        logger.info("Rendered document: %r", document)
        return document

    def __repr__(self) -> str:
        """
        Renders self as an unambiguous string for development.
        In this case, it displays in the style of a dataclass,
        where instance variables are listed with their
        values.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> repr(doc)
            'Document(elements=[])'

        :return:
            the MDList object as a development string
        """
        return f"Document(elements={self._elements!r})"

    def get_elements(self) -> list[Element]:
        """
        A getter method which allows the user to retrieve
        the underlying document structure of elements
        as a list. The return value is directly aliased
        to the underlying representation, so any changes
        to this object will change the document.

        The primary use of this method is to share an
        alias to the underlying document structure to
        other useful components like TableOfContents
        without creating circular references.

        .. versionadded:: 2.2
            Included as a part of the TableOfContents rework

        :return:
            the list of block comprising this document
        """
        return self._elements

    def add_block(self, block: Block) -> Block:
        """
        A generic function for appending blocks to the document.
        Use this function when you want a little more control over
        what the output looks like.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_block(snakemd.Heading("Python is Cool!", 2))
            Heading(text=[Inline(text='Python is Cool!',...)], level=2)
            >>> print(doc)
            ## Python is Cool!

        :param Block block:
            a markdown block (e.g., Table, Heading, etc.)
        :return:
            the :class:`Block` added to this Document
        """
        self._elements.append(block)
        logger.info("Added custom block to document: %r", block)
        return block

    def add_raw(self, text: str) -> Raw:
        """
        A convenience method which adds text as-is to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_raw("X: 5\\nY: 4\\nZ: 3")
            Raw(text='X: 5\\nY: 4\\nZ: 3')
            >>> print(doc)
            X: 5
            Y: 4
            Z: 3

        :param str text:
            some text
        :return:
            the :class:`Raw` block added to this Document
        """
        raw = Raw(text)
        self._elements.append(raw)
        logger.info("Added raw block to document: %r", text)
        return raw

    def add_heading(self, text: str, level: int = 1) -> Heading:
        """
        A convenience method which adds a heading to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_heading("Welcome to SnakeMD!")
            Heading(text=[Inline(text='Welcome to SnakeMD!',...)], level=1)
            >>> print(doc)
            # Welcome to SnakeMD!

        :param str text:
            the text for the heading
        :param int level:
            the level of the heading from 1 to 6
        :return:
            the :class:`Heading` added to this Document
        """
        heading = Heading(Inline(text), level)
        self._elements.append(heading)
        logger.info("Added heading to document: %r", heading)
        return heading

    def add_paragraph(self, text: str) -> Paragraph:
        """
        A convenience method which adds a paragraph of text to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_paragraph("Mitochondria is the powerhouse of the cell.")
            Paragraph(content=[...])
            >>> print(doc)
            Mitochondria is the powerhouse of the cell.

        :param str text:
            any arbitrary text
        :return:
            the :class:`Paragraph` added to this Document
        """
        paragraph = Paragraph([Inline(text)])
        self._elements.append(paragraph)
        logger.info("Added paragraph to document: %r", paragraph)
        return paragraph

    def add_ordered_list(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds an ordered list to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_ordered_list(["Goku", "Piccolo", "Vegeta"])
            MDList(items=[...], ordered=True, checked=None)
            >>> print(doc)
            1. Goku
            2. Piccolo
            3. Vegeta

        :param Iterable[str] items:
            a "list" of strings
        :return:
            the :class:`MDList` added to this Document
        """
        md_list = MDList(items, ordered=True)
        self._elements.append(md_list)
        logger.info("Added ordered list to document: %r", md_list)
        return md_list

    def add_unordered_list(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds an unordered list to the document.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_unordered_list(["Deku", "Bakugo", "Kirishima"])
            MDList(items=[...], ordered=False, checked=None)
            >>> print(doc)
            - Deku
            - Bakugo
            - Kirishima

        :param Iterable[str] items:
            a "list" of strings
        :return:
            the :class:`MDList` added to this Document
        """
        md_list = MDList(items)
        self._elements.append(md_list)
        logger.info("Added unordered list to document: %r", md_list)
        return md_list

    def add_checklist(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds a checklist to the document.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_checklist(["Okabe", "Mayuri", "Kurisu"])
            MDList(items=[...], ordered=False, checked=False)
            >>> print(doc)
            - [ ] Okabe
            - [ ] Mayuri
            - [ ] Kurisu

        :param Iterable[str] items:
            a "list" of strings
        :return:
            the :class:`MDList` added to this Document
        """
        md_checklist = MDList(items, checked=False)
        self._elements.append(md_checklist)
        logger.info("Added checklist to document: %r", md_checklist)
        return md_checklist

    def add_table(
        self,
        header: Iterable[str],
        data: Iterable[Iterable[str]],
        align: Iterable[Table.Align] = None,
        indent: int = 0,
    ) -> Table:
        """
        A convenience method which adds a table to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> header = ["Place", "Name"]
            >>> rows = [["1st", "Robert"], ["2nd", "Rae"]]
            >>> align = [snakemd.Table.Align.CENTER, snakemd.Table.Align.RIGHT]
            >>> doc.add_table(header, rows, align=align)
            Table(header=[...], body=[...], align=[...], indent=0)
            >>> print(doc) # doctest: +NORMALIZE_WHITESPACE
            | Place | Name   |
            | :---: | -----: |
            | 1st   | Robert |
            | 2nd   | Rae    |

        :param Iterable[str] header:
            a "list" of strings
        :param Iterable[Iterable[str]] data:
            a "list" of "lists" of strings
        :param Iterable[Table.Align] align:
            a "list" of column alignment values;
            defaults to None
        :param int indent:
            indent size for the whole table
        :return:
            the :class:`Table` added to this Document
        """
        header = [Paragraph([text]) for text in header]
        data = [[Paragraph([item]) for item in row] for row in data]
        table = Table(header, data, align, indent)
        self._elements.append(table)
        logger.info("Added table to document: %r", table)
        return table

    def add_code(self, code: str, lang: str = "generic") -> Code:
        """
        A convenience method which adds a code block to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_code("x = 5")
            Code(code='x = 5', lang='generic')
            >>> print(doc)
            ```generic
            x = 5
            ```

        :param str code:
            a preformatted code string
        :param str lang:
            the language for syntax highlighting
        :return:
            the :class:`Code` block added to this Document
        """
        code_block = Code(code, lang=lang)
        self._elements.append(code_block)
        logger.info("Added code block to document: %r", code_block)
        return code_block

    def add_quote(self, text: str) -> Quote:
        """
        A convenience method which adds a blockquote to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_quote("Welcome to the Internet!")
            Quote(content=[Raw(text='Welcome to the Internet!')])
            >>> print(doc)
            > Welcome to the Internet!

        :param str text:
            the text to be quoted
        :return:
            the :class:`Quote` added to this Document
        """
        quote = Quote(text)
        self._elements.append(quote)
        logger.info("Added quote to document: %r", quote)
        return quote

    def add_horizontal_rule(self) -> HorizontalRule:
        """
        A convenience method which adds a horizontal rule to the document:

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_horizontal_rule()
            HorizontalRule()
            >>> print(doc)
            ***

        :return:
            the :class:`HorizontalRule` added to this Document
        """
        horizontal_rule = HorizontalRule()
        self._elements.append(horizontal_rule)
        logger.info("Added horizontal rule to document: %r", horizontal_rule)
        return horizontal_rule

    def add_table_of_contents(self, levels: range = range(2, 3)) -> TableOfContents:
        """
        A convenience method which creates a table of contents. This function
        can be called where you want to add a table of contents to your
        document. The table itself is lazy loaded, so it always captures
        all of the heading blocks regardless of where the table of contents
        is added to the document.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_table_of_contents()
            TableOfContents(levels=range(2, 3))
            >>> doc.add_heading("First Item", 2)
            Heading(text=[Inline(text='First Item',...)], level=2)
            >>> doc.add_heading("Second Item", 2)
            Heading(text=[Inline(text='Second Item',...)], level=2)
            >>> print(doc)
            1. [First Item](#first-item)
            2. [Second Item](#second-item)
            <BLANKLINE>
            ## First Item
            <BLANKLINE>
            ## Second Item

        :param range levels:
            a range of heading levels to be included in the table of contents
        :return:
            the :class:`TableOfContents` added to this Document
        """
        toc = TableOfContents(levels=levels)
        self._elements.append(toc)
        logger.info("Added table of contents to document: %r", toc)
        return toc

    def scramble(self) -> None:
        """
        A silly method which mixes all of the blocks in this document in
        a random order.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_horizontal_rule()
            HorizontalRule()
            >>> doc.scramble()
            >>> print(doc)
            ***
        """
        random.shuffle(self._elements)
        logger.info("Scrambled document")

    def dump(
        self,
        name: str,
        directory: str | os.PathLike = "",
        ext: str = "md",
        encoding: str = "utf-8",
    ) -> None:
        """
        Outputs the markdown document to a file. This method assumes the output
        directory is the current working directory. Any alternative directory provided
        will be made if it does not already exist. This method also assumes a file
        extension of md and a file encoding of utf-8, all of which are configurable
        through the method parameters.

        .. doctest:: document

            >>> doc = snakemd.new_doc()
            >>> doc.add_horizontal_rule()
            HorizontalRule()
            >>> doc.dump("README")

        :param str name:
            the name of the markdown file to output without the file extension
        :param str | os.PathLike directory:
            the output directory for the markdown file; defaults to ""

            .. versionchanged:: 2.2
                Renamed from dir to directory to avoid built-in clashes

        :param str ext:
            the output file extension; defaults to "md"
        :param str encoding:
            the encoding to use; defaults to utf-8
        """
        pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
        with open(
            os.path.join(directory, f"{name}.{ext}"), "w+", encoding=encoding
        ) as output_file:
            output_file.write(str(self))
        logger.info("Dumped document to %s with filename %s.%s", directory, name, ext)
