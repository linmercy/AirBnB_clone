#!/usr/bin/python3
"""Review Module"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)

