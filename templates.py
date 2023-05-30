"""
PSILOSX TEMPLATES
"""
from functools import cached_property
from photoshop.api._artlayer import ArtLayer

# Standard Library Imports
from functools import cached_property

# Proxyshop Imports
import src.text_layers as text_classes
from src import templates as temp
from src.constants import con
from src.settings import cfg
import src.helpers as psd


class BorderlessMinimalistTemplate (temp.BorderlessTemplate):
    """
     * Borderless Minimalist Template
     * Created by PsilosX
    """
    template_suffix = "Borderless Minimalist"

    @cached_property
    def twins_layer(self) -> ArtLayer:
       return psd.getLayer("Twins")


class BorderlessMinimalistShortTemplate (temp.BorderlessTemplate):
    """
     * Borderless Minimalist Short Template
     * Created by PsilosX
    """
    template_suffix = "Borderless Minimalist Short"

    @cached_property
    def twins_layer(self) -> ArtLayer:
       return psd.getLayer("Twins")

    def __init__(self, layout):
        cfg.remove_flavor = True
        super().__init__(layout)