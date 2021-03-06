"""
    .. autoclass:: bibliography
"""

from docutils import nodes


class bibliography(nodes.General, nodes.Element):
    """Node for representing a bibliography. Replaced by a list of
    citations by
    :class:`~sphinxcontrib.bibtex2.foot_transforms.BibliographyTransform`.
    """
    pass
