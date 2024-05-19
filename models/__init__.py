#!/usr/bin/python3
""" Initial point """


from models.engine.file_storage import FileStorage


# Load existing data from JSON file
storage = FileStorage()
storage.reload()
