class NeedData(Exception):
    def __str__(self):
        print('post方式时data不能为空')