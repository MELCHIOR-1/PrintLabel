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

class ApplicationEvents3:
	CLSID = CLSID_Sink = IID('{00020A00-0000-0000-C000-000000000046}')
	coclass_clsid = IID('{000209FF-0000-0000-C000-000000000046}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        2 : "OnQuit",
		       19 : "OnMailMergeBeforeMerge",
		       20 : "OnMailMergeBeforeRecordMerge",
		        6 : "OnDocumentBeforeClose",
		       22 : "OnMailMergeDataSourceValidate",
		       25 : "OnWindowSize",
		1610678273 : "OnGetTypeInfo",
		        4 : "OnDocumentOpen",
		       18 : "OnMailMergeAfterRecordMerge",
		       14 : "OnWindowBeforeDoubleClick",
		1610678275 : "OnInvoke",
		1610612737 : "OnAddRef",
		1610612736 : "OnQueryInterface",
		        8 : "OnDocumentBeforeSave",
		1610678272 : "OnGetTypeInfoCount",
		       13 : "OnWindowBeforeRightClick",
		       16 : "OnEPostageInsert",
		       11 : "OnWindowDeactivate",
		1610612738 : "OnRelease",
		       15 : "OnEPostagePropertyDialog",
		       17 : "OnMailMergeAfterMerge",
		        7 : "OnDocumentBeforePrint",
		        9 : "OnNewDocument",
		        1 : "OnStartup",
		        3 : "OnDocumentChange",
		       23 : "OnMailMergeWizardSendToCustom",
		       10 : "OnWindowActivate",
		       21 : "OnMailMergeDataSourceLoad",
		       12 : "OnWindowSelectionChange",
		1610678274 : "OnGetIDsOfNames",
		       24 : "OnMailMergeWizardStateChange",
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
#	def OnQuit(self):
#	def OnMailMergeBeforeMerge(self, Doc=defaultNamedNotOptArg, StartRecord=defaultNamedNotOptArg, EndRecord=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnMailMergeBeforeRecordMerge(self, Doc=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnDocumentBeforeClose(self, Doc=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnMailMergeDataSourceValidate(self, Doc=defaultNamedNotOptArg, Handled=defaultNamedNotOptArg):
#	def OnWindowSize(self, Doc=defaultNamedNotOptArg, Wn=defaultNamedNotOptArg):
#	def OnGetTypeInfo(self, itinfo=defaultNamedNotOptArg, lcid=defaultNamedNotOptArg, pptinfo=pythoncom.Missing):
#	def OnDocumentOpen(self, Doc=defaultNamedNotOptArg):
#	def OnMailMergeAfterRecordMerge(self, Doc=defaultNamedNotOptArg):
#	def OnWindowBeforeDoubleClick(self, Sel=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnInvoke(self, dispidMember=defaultNamedNotOptArg, riid=defaultNamedNotOptArg, lcid=defaultNamedNotOptArg, wFlags=defaultNamedNotOptArg
#			, pdispparams=defaultNamedNotOptArg, pvarResult=pythoncom.Missing, pexcepinfo=pythoncom.Missing, puArgErr=pythoncom.Missing):
#	def OnAddRef(self):
#	def OnQueryInterface(self, riid=defaultNamedNotOptArg, ppvObj=pythoncom.Missing):
#	def OnDocumentBeforeSave(self, Doc=defaultNamedNotOptArg, SaveAsUI=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnGetTypeInfoCount(self, pctinfo=pythoncom.Missing):
#	def OnWindowBeforeRightClick(self, Sel=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnEPostageInsert(self, Doc=defaultNamedNotOptArg):
#	def OnWindowDeactivate(self, Doc=defaultNamedNotOptArg, Wn=defaultNamedNotOptArg):
#	def OnRelease(self):
#	def OnEPostagePropertyDialog(self, Doc=defaultNamedNotOptArg):
#	def OnMailMergeAfterMerge(self, Doc=defaultNamedNotOptArg, DocResult=defaultNamedNotOptArg):
#	def OnDocumentBeforePrint(self, Doc=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnNewDocument(self, Doc=defaultNamedNotOptArg):
#	def OnStartup(self):
#	def OnDocumentChange(self):
#	def OnMailMergeWizardSendToCustom(self, Doc=defaultNamedNotOptArg):
#	def OnWindowActivate(self, Doc=defaultNamedNotOptArg, Wn=defaultNamedNotOptArg):
#	def OnMailMergeDataSourceLoad(self, Doc=defaultNamedNotOptArg):
#	def OnWindowSelectionChange(self, Sel=defaultNamedNotOptArg):
#	def OnGetIDsOfNames(self, riid=defaultNamedNotOptArg, rgszNames=defaultNamedNotOptArg, cNames=defaultNamedNotOptArg, lcid=defaultNamedNotOptArg
#			, rgdispid=pythoncom.Missing):
#	def OnMailMergeWizardStateChange(self, Doc=defaultNamedNotOptArg, FromState=defaultNamedNotOptArg, ToState=defaultNamedNotOptArg, Handled=defaultNamedNotOptArg):


win32com.client.CLSIDToClass.RegisterCLSID( "{00020A00-0000-0000-C000-000000000046}", ApplicationEvents3 )
