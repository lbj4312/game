import sys
with open(sys.argv[1],'rb') as f:
    nr=f.read()
    nr=nr.decode("utf-8").replace("\r\n","\r").encode("utf-8")
with open(sys.argv[1],'wb') as f:
    f.write(nr)