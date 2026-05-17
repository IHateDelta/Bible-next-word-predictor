in_file = open ("pol_ubg.txt","r", errors='ignore',encoding='utf8')
out_file = open ("bible_lines.txt","w",encoding='utf8')
while s := in_file.readline():
    t=s[s.find(":")+1:]
    #t.replace("."," ")
    while t[0].isdigit() or t[0]==" " or t[0]=="¶": t=t[1:]
    for x in [",",".",";","?",":","!","\"","\'","– ","- ","„","”","(",")"]: t=t.replace(x,"")
    t=t.lower()
    out_file.write(f"{t}")
in_file.close()
out_file.close()