# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{00020905-0000-0000-C000-000000000046}'
# On Fri Dec 23 09:10:59 2016
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

class DocumentEvents2:
	CLSID = CLSID_Sink = IID('{00020A02-0000-0000-C000-000000000046}')
	coclass_clsid = IID('{00020906-0000-0000-C000-000000000046}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		       13 : "OnContentControlBeforeDelete",
		       14 : "OnContentControlOnExit",
		       17 : "OnContentControlBeforeContentUpdate",
		        7 : "OnSync",
		       18 : "OnBuildingBlockInsert",
		        9 : "OnXMLBeforeDelete",
		       12 : "OnContentControlAfterAdd",
		       15 : "OnContentControlOnEnter",
		       16 : "OnContentControlBeforeStoreUpdate",
		        6 : "OnClose",
		        4 : "OnNew",
		        5 : "OnOpen",
		        8 : "OnXMLAfterInsert",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnContentControlBeforeDelete(self, OldContentControl=defaultNamedNotOptArg, InUndoRedo=defaultNamedNotOptArg):
#	def OnContentControlOnExit(self, ContentControl=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnContentControlBeforeContentUpdate(self, ContentControl=defaultNamedNotOptArg, Content=defaultNamedNotOptArg):
#	def OnSync(self, SyncEventType=defaultNamedNotOptArg):
#	def OnBuildingBlockInsert(self, Range=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, Category=defaultNamedNotOptArg, BlockType=defaultNamedNotOptArg
#			, Template=defaultNamedNotOptArg):
#	def OnXMLBeforeDelete(self, DeletedRange=defaultNamedNotOptArg, OldXMLNode=defaultNamedNotOptArg, InUndoRedo=defaultNamedNotOptArg):
#	def OnContentControlAfterAdd(self, NewContentControl=defaultNamedNotOptArg, InUndoRedo=defaultNamedNotOptArg):
#	def OnContentControlOnEnter(self, ContentControl=defaultNamedNotOptArg):
#	def OnContentControlBeforeStoreUpdate(self, ContentControl=defaultNamedNotOptArg, Content=defaultNamedNotOptArg):
#	def OnClose(self):
#	def OnNew(self):
#	def OnOpen(self):
#	def OnXMLAfterInsert(self, NewXMLNode=defaultNamedNotOptArg, InUndoRedo=defaultNamedNotOptArg):


win32com.client.CLSIDToClass.RegisterCLSID( "{00020A02-0000-0000-C000-000000000046}", DocumentEvents2 )
