半自动爬取2.0

原理是获取全国一天内影院的上映情况
网址为 http://maoyan.com/xseats/20180207XXXXXXX（后面七位数，随机代表，我觉得是在全国范围按时间排序的）
缺点：爬取次数巨大，验证码还没设置成自动的，技术限制（本人爬虫萌新阶段）

跳出来验证图片后人眼识别输入 ENTER 就行

环境：python3.X
需要如下环境包：scrapy, 装scrapy中可能会遇到其它环境问题，没记错的话是twist的，自行百度即可
python非官方包，有的官方包不匹配,https://www.lfd.uci.edu/~gohlke/pythonlibs/

在当前文件夹，运行命令：scrapy crawl seats -o seats.csv
seats.csv 还可以是aaaa.json bbbbbb.txt等，需要输出到mysql,mongodb等，我可以帮忙设置一下。
本人菜鸟，码力还不够，多见谅

PS:保存csv文件后，需要改一下编码格式，用notepad打开，编码格式设置为UTF-8
