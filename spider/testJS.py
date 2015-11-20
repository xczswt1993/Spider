#!/usr/bin/env python
import js2py

js = """
function  add(){
var seal=8443+2417;
var goat=5689+2834^seal;
var cock=3994+391^goat;
var worm=905+5302^cock;
var calf=8071+6115^worm;
document.write((247^worm)+362);
}
add()
""".replace("document.write","return")
result = js2py.eval_js(js)
print result
