# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{00020905-0000-0000-C000-000000000046}'
# On Fri Dec 23 09:10:51 2016
'Microsoft Word 15.0 Object Library'
makepy_version = '0.5.01'
python_version = 0x2070af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{00020905-0000-0000-C000-000000000046}')
MajorVersion = 8
MinorVersion = 6
LibraryFlags = 8
LCID = 0x0

from win32com.client import CoClassBaseClass
import sys
__import__('win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents3')
ApplicationEvents3 = sys.modules['win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents3'].ApplicationEvents3
__import__('win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents4')
ApplicationEvents4 = sys.modules['win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents4'].ApplicationEvents4
__import__('win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents2')
ApplicationEvents2 = sys.modules['win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents2'].ApplicationEvents2
__import__('win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents')
ApplicationEvents = sys.modules['win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6.ApplicationEvents'].ApplicationEvents
__import__('win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6._Application')
_Application = sys.modules['win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x6._Application']._Application
# This CoClass is known by the name 'Word.Application.15'
class Application(CoClassBaseClass): # A CoClass
	CLSID = IID('{000209FF-0000-0000-C000-000000000046}')
	coclass_sources = [
		ApplicationEvents3,
		ApplicationEvents4,
		ApplicationEvents2,
		ApplicationEvents,
	]
	default_source = ApplicationEvents4
	coclass_interfaces = [
		_Application,
	]
	default_interface = _Application

win32com.client.CLSIDToClass.RegisterCLSID( "{000209FF-0000-0000-C000-000000000046}", Application )
