import requests
from verify_code_to_string.verify_code_to_string import verify_code_to_string
def request_noproxy_noland(url,headers,data=None,methord='get'):
    if not data and methord=='get':
        response = requests.get(url=url,headers=headers)
        response.encoding='utf8'
        return response.text
    elif data and methord == 'get':
        response = requests.get(url=url,headers=headers,params=data)
        response.encoding='utf8'
        return response.text
    elif data and methord == 'post':
        response = requests.post(url=url,data=data,headers=headers)
        response.encoding='utf8'
        return response.text
    else:
        raise Exception
def request_needproxy_noland(url,headers,proxy,data=None,methord='get'):
    #获取proxy
    if not data and methord=='get':
        response = requests.get(url=url,headers=headers,proxies=proxy)
        response.encoding='utf8'
        return response.text
    elif data and methord == 'get':
        response = requests.get(url=url,headers=headers,params=data,proxies=proxy)
        response.encoding='utf8'
        return response.text
    elif data and methord == 'post':
        response = requests.post(url=url,data=data,headers=headers,proxies=proxy)
        response.encoding='utf8'
        return response.text
    else:
        raise Exception
class RequestNoproxyNeedland():
    '''url:登陆的post接口，account：登陆提交的表单包括用户名密码等'''

    def __init__(self,url,headers,account,if_need_verify=False,verify_code_url=None,account_verify_name=None):
        if not if_need_verify:
            self.opener = requests.Session()
            self.headers = headers
            self.opener.post(url,headers=headers,data=account)
        elif if_need_verify and verify_code_url and account_verify_name:
            self.opener = requests.Session()
            self.headers = headers
            #获取验证码
            s = 0
            while True:
                s+=1
                self.verify_img = self.opener.get(verify_code_url, headers=self.headers).content
                with open('code.png', 'wb') as fp:
                    fp.write(self.verify_img)
                #使用打码平台解析
                cid,code_string = verify_code_to_string('code.png')
                #把验证码放入account中
                account[account_verify_name] = code_string
                if self.opener.post(url=url,headers=headers,data=account).status_code == 200 or s > 3:
                    print('尝试第%d次打码结束'%s)
                    break
        else:
            print('参数缺失')
    def request_noproxy_needland(self,url,data=None,methord='get'):
        if not data and methord=='get':
            response = self.opener.get(url=url,headers=self.headers)
            response.encoding='utf8'
            return response.text
        elif data and methord == 'get':
            response = self.opener.get(url=url,headers=self.headers,params=data)
            response.encoding='utf8'
            return response.text
        elif data and methord == 'post':
            response = self.opener.post(url=url,data=data,headers=self.headers)
            response.encoding='utf8'
            return response.text
        else:
            raise Exception
class RequestNeedproxyNeedland():
    '''url:登陆的post接口，account：登陆提交的表单包括用户名密码等'''

    def __init__(self,url,headers,account,if_need_verify=False,verify_code_url=None,account_verify_name=None):
        if not if_need_verify:
            self.opener = requests.Session()
            self.headers = headers
            self.opener.post(url,headers=headers,data=account)
        elif if_need_verify and verify_code_url and account_verify_name:
            self.opener = requests.Session()
            self.headers = headers
            #获取验证码
            s = 0
            while True:
                s+=1
                self.verify_img = self.opener.get(verify_code_url, headers=self.headers).content
                with open('code.png', 'wb') as fp:
                    fp.write(self.verify_img)
                #使用打码平台解析
                cid,code_string = verify_code_to_string('code.png')
                #把验证码放入account中
                account[account_verify_name] = code_string
                if self.opener.post(url=url,headers=headers,data=account).status_code == 200 or s > 3:
                    print('尝试第%d次打码结束'%s)
                    break
        else:
            print('参数缺失')
    def request_needproxy_needland(self,url,proxies,data=None,methord='get'):
        if not data and methord=='get':
            response = self.opener.get(url=url,headers=self.headers,proxies=proxies)
            response.encoding='utf8'
            return response.text
        elif data and methord == 'get':
            response = self.opener.get(url=url,headers=self.headers,params=data,proxies=proxies)
            response.encoding='utf8'
            return response.text
        elif data and methord == 'post':
            response = self.opener.post(url=url,data=data,headers=self.headers,proxies=proxies)
            response.encoding='utf8'
            return response.text
        else:
            raise Exception
'''#需要登陆，不需要代理，需要验证码例子
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    account = {
        '__VIEWSTATE':'89mtomFbHAPsIbCz1XxKXl3Ilv82npcm2j9T8wA6TuXTFCHbLI/Pi+K1XN4d2c8CV0AWCoUM0ns2w3+QtF/LnlNIUdhj8hhU1rx4VvHnccg5Smt2oIPouPY/rek=',
        '__VIEWSTATEGENERATOR':'C93BE1AE',
        'from':'http://so.gushiwen.org/user/collect.aspx',
        'email':'992895433@qq.com',
        'pwd':'wbt19951208',
        'denglu':'登录',
    }
    browser = RequestNoproxyNeedland(url,headers,account,if_need_verify=True,verify_code_url='http://so.gushiwen.org/RandCode.ashx',account_verify_name='code')
    html  = browser.request_noproxy_needland('https://so.gushiwen.org/user/collect.aspx')
    print(html)
'''