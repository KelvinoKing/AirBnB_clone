#!/usr/bin/python3
"""file_storage module
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
