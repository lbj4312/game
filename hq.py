import requests
ip=requests.get("http://6.ipw.cn/").text
with open("i.html",'w') as f:
    f.write("<a href='http://["+ip+"]:8000/' target=_blank><button>狗屁不通文章生成器</button></a>\n<a href='http://["+ip+"]:8500/' target=_blank><button>打篮球游戏</button></a>")
