#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time 
import datetime 


print("üç saniye içinde başlıcak")

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("go..")
time.sleep(0.5)

once = datetime.datetime.now()

metin = input("Buraya yaz!!")

sonra = datetime.datetime.now()

hız = sonra - once

seconds = round(hız.total_seconds(),2)
saniyebasikelime = round(len(text)  / seconds,1)

print("sen yazdın : {}".format(seconds))
print("saniyede harf : {}".format(saniyebasikelime))

