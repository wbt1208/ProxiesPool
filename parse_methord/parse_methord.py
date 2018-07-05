from lxml import etree
def find_right_infor_usexpath(html,xpath):
    tree = etree.HTML(html)
    return tree.xpath(xpath)
#构造这个方法，是希望可以在这个函数中编辑xpath，而不是想上面那个函数传递xpath，
# 上面解析不能实现对html多次解析得到信息情形
def find_need_infor_usexpath(html):
    items = []
    xpath_dl = "//div[@class='album_detail_wrap']/dl"
    xpath_name = './dd/p/text()'
    htmltree = etree.HTML(html)
    for dl in htmltree.xpath(xpath_dl):
        name = dl.xpath(xpath_name)[0]
        items.append(name)
    return items