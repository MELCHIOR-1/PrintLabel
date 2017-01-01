# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import win32com.client
import os
label_file = os.path.abspath('labels.docx')
source_file = os.path.abspath('names.xlsx')
w = win32com.client.gencache.EnsureDispatch('Word.Application')
#w = win32com.client.Dispatch('Word.Application')
w.Visible = 1
w.DisplayAlerts = 0
#w.WindowState = 1
oldprint = w.ActivePrinter
doc = w.Documents.Open(label_file)
mm = doc.MailMerge
mm.OpenDataSource(source_file)
mm.Destination = 1
mm.Execute()

w.Documents.Close(0)
w.ActivePrinter = oldprint
w.Quit()