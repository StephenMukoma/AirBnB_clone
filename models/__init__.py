#!/usr/bin/python3
"""Reloads JSON storage file"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
__all__ = ["base_model", "user", "state", "city", "amenity", "place", "review"]
