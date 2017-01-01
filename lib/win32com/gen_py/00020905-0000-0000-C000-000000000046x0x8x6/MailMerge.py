# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{00020905-0000-0000-C000-000000000046}'
# On Fri Dec 23 09:11:00 2016
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

from win32com.client import DispatchBaseClass
class MailMerge(DispatchBaseClass):
	CLSID = IID('{00020920-0000-0000-C000-000000000046}')
	coclass_clsid = None

	def Check(self):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

	def CreateDataSource(self, Name=defaultNamedOptArg, PasswordDocument=defaultNamedOptArg, WritePasswordDocument=defaultNamedOptArg, HeaderRecord=defaultNamedOptArg
			, MSQuery=defaultNamedOptArg, SQLStatement=defaultNamedOptArg, SQLStatement1=defaultNamedOptArg, Connection=defaultNamedOptArg, LinkToSource=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), ((16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),Name
			, PasswordDocument, WritePasswordDocument, HeaderRecord, MSQuery, SQLStatement
			, SQLStatement1, Connection, LinkToSource)

	def CreateHeaderSource(self, Name=defaultNamedNotOptArg, PasswordDocument=defaultNamedOptArg, WritePasswordDocument=defaultNamedOptArg, HeaderRecord=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17)),Name
			, PasswordDocument, WritePasswordDocument, HeaderRecord)

	def EditDataSource(self):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), (),)

	def EditHeaderSource(self):
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), (),)

	def EditMainDocument(self):
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), (),)

	def Execute(self, Pause=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((16396, 17),),Pause
			)

	def OpenDataSource(self, Name=defaultNamedNotOptArg, Format=defaultNamedOptArg, ConfirmConversions=defaultNamedOptArg, ReadOnly=defaultNamedOptArg
			, LinkToSource=defaultNamedOptArg, AddToRecentFiles=defaultNamedOptArg, PasswordDocument=defaultNamedOptArg, PasswordTemplate=defaultNamedOptArg, Revert=defaultNamedOptArg
			, WritePasswordDocument=defaultNamedOptArg, WritePasswordTemplate=defaultNamedOptArg, Connection=defaultNamedOptArg, SQLStatement=defaultNamedOptArg, SQLStatement1=defaultNamedOptArg
			, OpenExclusive=defaultNamedOptArg, SubType=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(112, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),Name
			, Format, ConfirmConversions, ReadOnly, LinkToSource, AddToRecentFiles
			, PasswordDocument, PasswordTemplate, Revert, WritePasswordDocument, WritePasswordTemplate
			, Connection, SQLStatement, SQLStatement1, OpenExclusive, SubType
			)

	def OpenDataSource2000(self, Name=defaultNamedNotOptArg, Format=defaultNamedOptArg, ConfirmConversions=defaultNamedOptArg, ReadOnly=defaultNamedOptArg
			, LinkToSource=defaultNamedOptArg, AddToRecentFiles=defaultNamedOptArg, PasswordDocument=defaultNamedOptArg, PasswordTemplate=defaultNamedOptArg, Revert=defaultNamedOptArg
			, WritePasswordDocument=defaultNamedOptArg, WritePasswordTemplate=defaultNamedOptArg, Connection=defaultNamedOptArg, SQLStatement=defaultNamedOptArg, SQLStatement1=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),Name
			, Format, ConfirmConversions, ReadOnly, LinkToSource, AddToRecentFiles
			, PasswordDocument, PasswordTemplate, Revert, WritePasswordDocument, WritePasswordTemplate
			, Connection, SQLStatement, SQLStatement1)

	def OpenHeaderSource(self, Name=defaultNamedNotOptArg, Format=defaultNamedOptArg, ConfirmConversions=defaultNamedOptArg, ReadOnly=defaultNamedOptArg
			, AddToRecentFiles=defaultNamedOptArg, PasswordDocument=defaultNamedOptArg, PasswordTemplate=defaultNamedOptArg, Revert=defaultNamedOptArg, WritePasswordDocument=defaultNamedOptArg
			, WritePasswordTemplate=defaultNamedOptArg, OpenExclusive=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),Name
			, Format, ConfirmConversions, ReadOnly, AddToRecentFiles, PasswordDocument
			, PasswordTemplate, Revert, WritePasswordDocument, WritePasswordTemplate, OpenExclusive
			)

	def OpenHeaderSource2000(self, Name=defaultNamedNotOptArg, Format=defaultNamedOptArg, ConfirmConversions=defaultNamedOptArg, ReadOnly=defaultNamedOptArg
			, AddToRecentFiles=defaultNamedOptArg, PasswordDocument=defaultNamedOptArg, PasswordTemplate=defaultNamedOptArg, Revert=defaultNamedOptArg, WritePasswordDocument=defaultNamedOptArg
			, WritePasswordTemplate=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),Name
			, Format, ConfirmConversions, ReadOnly, AddToRecentFiles, PasswordDocument
			, PasswordTemplate, Revert, WritePasswordDocument, WritePasswordTemplate)

	def ShowWizard(self, InitialState=defaultNamedNotOptArg, ShowDocumentStep=defaultNamedOptArg, ShowTemplateStep=defaultNamedOptArg, ShowDataStep=defaultNamedOptArg
			, ShowWriteStep=defaultNamedOptArg, ShowPreviewStep=defaultNamedOptArg, ShowMergeStep=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), ((16396, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),InitialState
			, ShowDocumentStep, ShowTemplateStep, ShowDataStep, ShowWriteStep, ShowPreviewStep
			, ShowMergeStep)

	def UseAddressBook(self, Type=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((8, 1),),Type
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (1000, 2, (13, 0), (), "Application", '{000209FF-0000-0000-C000-000000000046}'),
		"Creator": (1001, 2, (3, 0), (), "Creator", None),
		# Method 'DataSource' returns object of type 'MailMergeDataSource'
		"DataSource": (4, 2, (9, 0), (), "DataSource", '{0002091D-0000-0000-C000-000000000046}'),
		"Destination": (3, 2, (3, 0), (), "Destination", None),
		# Method 'Fields' returns object of type 'MailMergeFields'
		"Fields": (5, 2, (9, 0), (), "Fields", '{0002091F-0000-0000-C000-000000000046}'),
		"HighlightMergeFields": (11, 2, (11, 0), (), "HighlightMergeFields", None),
		"MailAddressFieldName": (9, 2, (8, 0), (), "MailAddressFieldName", None),
		"MailAsAttachment": (8, 2, (11, 0), (), "MailAsAttachment", None),
		"MailFormat": (12, 2, (3, 0), (), "MailFormat", None),
		"MailSubject": (10, 2, (8, 0), (), "MailSubject", None),
		"MainDocumentType": (1, 2, (3, 0), (), "MainDocumentType", None),
		"Parent": (1002, 2, (9, 0), (), "Parent", None),
		"ShowSendToCustom": (13, 2, (8, 0), (), "ShowSendToCustom", None),
		"State": (2, 2, (3, 0), (), "State", None),
		"SuppressBlankLines": (7, 2, (11, 0), (), "SuppressBlankLines", None),
		"ViewMailMergeFieldCodes": (6, 2, (3, 0), (), "ViewMailMergeFieldCodes", None),
		"WizardState": (14, 2, (3, 0), (), "WizardState", None),
	}
	_prop_map_put_ = {
		"Destination": ((3, LCID, 4, 0),()),
		"HighlightMergeFields": ((11, LCID, 4, 0),()),
		"MailAddressFieldName": ((9, LCID, 4, 0),()),
		"MailAsAttachment": ((8, LCID, 4, 0),()),
		"MailFormat": ((12, LCID, 4, 0),()),
		"MailSubject": ((10, LCID, 4, 0),()),
		"MainDocumentType": ((1, LCID, 4, 0),()),
		"ShowSendToCustom": ((13, LCID, 4, 0),()),
		"SuppressBlankLines": ((7, LCID, 4, 0),()),
		"ViewMailMergeFieldCodes": ((6, LCID, 4, 0),()),
		"WizardState": ((14, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{00020920-0000-0000-C000-000000000046}", MailMerge )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{00020905-0000-0000-C000-000000000046}'
# On Fri Dec 23 09:11:00 2016
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

MailMerge_vtables_dispatch_ = 1
MailMerge_vtables_ = [
	(( u'Application' , u'prop' , ), 1000, (1000, (), [ (16397, 10, None, "IID('{000209FF-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Creator' , u'prop' , ), 1001, (1001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Parent' , u'prop' , ), 1002, (1002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'MainDocumentType' , u'prop' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'MainDocumentType' , u'prop' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'prop' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Destination' , u'prop' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Destination' , u'prop' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'DataSource' , u'prop' , ), 4, (4, (), [ (16393, 10, None, "IID('{0002091D-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Fields' , u'prop' , ), 5, (5, (), [ (16393, 10, None, "IID('{0002091F-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'ViewMailMergeFieldCodes' , u'prop' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'ViewMailMergeFieldCodes' , u'prop' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SuppressBlankLines' , u'prop' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SuppressBlankLines' , u'prop' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'MailAsAttachment' , u'prop' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'MailAsAttachment' , u'prop' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'MailAddressFieldName' , u'prop' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'MailAddressFieldName' , u'prop' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'MailSubject' , u'prop' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'MailSubject' , u'prop' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CreateDataSource' , u'Name' , u'PasswordDocument' , u'WritePasswordDocument' , u'HeaderRecord' , 
			u'MSQuery' , u'SQLStatement' , u'SQLStatement1' , u'Connection' , u'LinkToSource' , 
			), 101, (101, (), [ (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 9 , 108 , (3, 0, None, None) , 0 , )),
	(( u'CreateHeaderSource' , u'Name' , u'PasswordDocument' , u'WritePasswordDocument' , u'HeaderRecord' , 
			), 102, (102, (), [ (8, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 3 , 112 , (3, 0, None, None) , 0 , )),
	(( u'OpenDataSource2000' , u'Name' , u'Format' , u'ConfirmConversions' , u'ReadOnly' , 
			u'LinkToSource' , u'AddToRecentFiles' , u'PasswordDocument' , u'PasswordTemplate' , u'Revert' , 
			u'WritePasswordDocument' , u'WritePasswordTemplate' , u'Connection' , u'SQLStatement' , u'SQLStatement1' , 
			), 103, (103, (), [ (8, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 13 , 116 , (3, 0, None, None) , 64 , )),
	(( u'OpenHeaderSource2000' , u'Name' , u'Format' , u'ConfirmConversions' , u'ReadOnly' , 
			u'AddToRecentFiles' , u'PasswordDocument' , u'PasswordTemplate' , u'Revert' , u'WritePasswordDocument' , 
			u'WritePasswordTemplate' , ), 104, (104, (), [ (8, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 9 , 120 , (3, 0, None, None) , 64 , )),
	(( u'Execute' , u'Pause' , ), 105, (105, (), [ (16396, 17, None, None) , ], 1 , 1 , 4 , 1 , 124 , (3, 0, None, None) , 0 , )),
	(( u'Check' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'EditDataSource' , ), 107, (107, (), [ ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'EditHeaderSource' , ), 108, (108, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'EditMainDocument' , ), 109, (109, (), [ ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'UseAddressBook' , u'Type' , ), 111, (111, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( u'HighlightMergeFields' , u'prop' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'HighlightMergeFields' , u'prop' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'MailFormat' , u'prop' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'MailFormat' , u'prop' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'ShowSendToCustom' , u'prop' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'ShowSendToCustom' , u'prop' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'WizardState' , u'prop' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'WizardState' , u'prop' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'OpenDataSource' , u'Name' , u'Format' , u'ConfirmConversions' , u'ReadOnly' , 
			u'LinkToSource' , u'AddToRecentFiles' , u'PasswordDocument' , u'PasswordTemplate' , u'Revert' , 
			u'WritePasswordDocument' , u'WritePasswordTemplate' , u'Connection' , u'SQLStatement' , u'SQLStatement1' , 
			u'OpenExclusive' , u'SubType' , ), 112, (112, (), [ (8, 1, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 15 , 180 , (3, 0, None, None) , 0 , )),
	(( u'OpenHeaderSource' , u'Name' , u'Format' , u'ConfirmConversions' , u'ReadOnly' , 
			u'AddToRecentFiles' , u'PasswordDocument' , u'PasswordTemplate' , u'Revert' , u'WritePasswordDocument' , 
			u'WritePasswordTemplate' , u'OpenExclusive' , ), 113, (113, (), [ (8, 1, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 10 , 184 , (3, 0, None, None) , 0 , )),
	(( u'ShowWizard' , u'InitialState' , u'ShowDocumentStep' , u'ShowTemplateStep' , u'ShowDataStep' , 
			u'ShowWriteStep' , u'ShowPreviewStep' , u'ShowMergeStep' , ), 114, (114, (), [ (16396, 1, None, None) , 
			(16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			(16396, 17, None, None) , ], 1 , 1 , 4 , 6 , 188 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{00020920-0000-0000-C000-000000000046}", MailMerge )
