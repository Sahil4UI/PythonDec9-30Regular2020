Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> dt=datetime.now()
>>> dt.strftime("%d/%m/%y")
'12/01/21'
>>> dt.strftime("%d/%m/%y,%a")
'12/01/21,Tue'
>>> dt.strftime("%H:%M:%Y,%p")
'09:55:2021,AM'
>>> #%H-24hours clock format
>>> dt.strftime("%I:%M:%Y,%p")
'09:55:2021,AM'
>>> #%I-12hours clock format
>>> 
