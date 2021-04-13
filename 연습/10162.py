#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T=int(input("시간 입력:"))
a=0
b=0
c=0

if (T%10)!=0:
    print(-1)
else:
    a=T/300
    T=T%300
    b=T/60
    T=T%60
    c=T/10
    print("%d %d %d" %(a,b,c))

