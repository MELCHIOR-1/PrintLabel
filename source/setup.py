# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:00:17 2016

@author: x
"""

from distutils.core import setup
import py2exe

options = {"py2exe":
    {"skip_archive":True,
    "dll_excludes":["OLEAUT32.dll","USER32.dll","SHELL32.dll","ole32.dll","ADVAPI32.dll","mfc90.dll","WS2_32.dll","WINSPOOL.DRV","GDI32.dll","VERSION.dll","KERNEL32.dll"]}}
setup(console=[{"script":"print.py", "icon_resources": [(1, "badge.ico")]}],options=options,zipfile="lib/bar.zip")