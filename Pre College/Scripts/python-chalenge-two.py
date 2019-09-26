string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

newstring = "100: "

url1 = "map"

newUrl1 = ""

cypher = {"a":"c", "b":"d", "c":"e", "d":"f", "e":"g", "f":"h", "g":"i", "h":"j", "i":"k", "j":"l", \
          "k":"m", "l":"n", "m":"o", "n":"p", "o":"q", "p":"r", "q":"s", "r":"t", "s":"u", "t":"v", \
          "u":"w", "v":"x", "w":"y", "x":"z", "y":"a", "z":"b", " ":" ", ".":".", "(":"(", ")":")", \
          '"':'"', "'":"'", "/":"/",":":":"}

for char in string:
    newstring += cypher[char]
    
for char in url1:
    newUrl1 += cypher[char]
    
print(newstring)
print(newUrl1)

url ="rddz://ggg.zidryxmrkvvoxqo.myw/zm/nop/wkz.rdwv"
newURL = ""

cypher = {"a":"q", "b":"r", "c":"s", "d":"t", "e":"u", "f":"v", "g":"w", "h":"x", "i":"y", "j":"z", \
          "k":"a", "l":"b", "m":"c", "n":"d", "o":"e", "p":"f", "q":"g", "r":"h", "s":"i", "t":"j", \
          "u":"k", "v":"l", "w":"m", "x":"n", "y":"o", "z":"p", " ":" ", ".":".", "(":"(", ")":")", \
          '"':'"', "'":"'", "/":"/",":":":"}

for char in url:
    newURL += cypher[char]
    
print(newURL)
