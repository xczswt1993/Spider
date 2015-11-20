#!/usr/bin/env python
#-*-coding:utf-8 -*-
import js2py
all="""
    var seal=8443+2417;
    var goat=5689+2834^seal;
    var cock=3994+391^goat;
    var worm=905+5302^cock;
    var calf=8071+6115^worm;
    """
sig ="document.write((247^worm)+362);"
html = all+sig
print html
js ="""function add(){
    %s
} 
add()""" % html.replace("document.write","return")
#result = js.replace("document.write","return")
result = js2py.eval_js(js)
print result
