import os
import importlib

def load_plugins():
    plugins = []
    for file in os.listdir("plugins"):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = importlib.import_module(f"plugins.{module_name}")
            plugins.append(module)
    return plugins
