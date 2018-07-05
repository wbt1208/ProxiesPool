from request_methord.request_methord import request_noproxy_noland
from parse_methord import parse_methord
class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if "crawl" in k :
                attrs['__CrawlFunc__'].append(k)
                count+=1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases,attrs)
class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            if proxy :
                # print("成功取到代理",proxy)
                proxies.append(proxy)
        return proxies
    # def crawl_66ip(self,page_count=100):
    #     url_orginal = "http://www.66ip.cn/{}.html"
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    #     }
    #     urls = [url_orginal.format(page) for page in range(2,page_count)]
    #     for url in urls:
    #         contant = request_noproxy_noland(url=url,headers=headers)
    #         base_xapth = "//table[@width='100%']/tr"
    #         ip_xpath = "./td[1]/text()"
    #         port_xpath = "./td[2]/text()"
    #         if contant:
    #             for td_infor in parse_methord.find_right_infor_usexpath(contant,base_xapth)[1:] :
    #                 ip = td_infor.xpath(ip_xpath)[0]
    #                 port = td_infor.xpath(port_xpath)[0]
    #                 ip_port = ":".join([ip, port])
    #                 if ip_port:
    #                     yield ip_port
    def crawl_kuaidaili(self,page_count=100):
        url_orginal = "https://www.kuaidaili.com/free/inha/{}/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        url_lists = [url_orginal.format(page) for page in range(1,page_count)]
        for url in url_lists:
            contant = request_noproxy_noland(url=url, headers=headers)
            base_xapth = "//tbody/tr"
            ip_xpath = "./td[1]/text()"
            port_xpath = "./td[2]/text()"
            http_xpath = "./td[4]/text()"
            if contant:
                for td_infor in parse_methord.find_right_infor_usexpath(contant,base_xapth) :
                    ip = td_infor.xpath(ip_xpath)[0]
                    port = td_infor.xpath(port_xpath)[0]
                    http = td_infor.xpath(http_xpath)[0].lower()
                    ip_port = ":".join([ip, port])
                    if ip_port:
                        http_ip_port =http+":"+"//" +ip_port
                        yield http_ip_port
    def crawl_xici(self,page_count = 1000):
        url_orginal = "http://www.xicidaili.com/nn/{}"
        url_list = [url_orginal.format(page) for page in range(1,page_count)]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        for url in url_list:
            contant = request_noproxy_noland(url=url, headers=headers)
            base_xapth = "//table//tr"
            ip_xpath = "./td[2]/text()"
            port_xpath = "./td[3]/text()"
            http_xpath = "./td[6]/text()"
            if contant:
                for td_infor in parse_methord.find_right_infor_usexpath(contant, base_xapth)[2:]:
                    ip = td_infor.xpath(ip_xpath)[0]
                    port = td_infor.xpath(port_xpath)[0]
                    http = td_infor.xpath(http_xpath)[0].lower()
                    ip_port = ":".join([ip, port])
                    if ip_port:
                        http_ip_port = http + ":" + "//" + ip_port
                        yield http_ip_port
# c = Crawler()
# for i in c.crawl_xici():
#     print(i)


