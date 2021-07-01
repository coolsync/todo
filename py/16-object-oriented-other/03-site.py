class Site(object):
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name: %s' % self.name)
        print('url: %s' % self.__url)

    def __fn(self):
        print('this is private method')

    def fn(self):
        print('this is pub method')
        self.__fn()

site = Site('example', 'www.example.com')

# print(site.name)
# print(site.__url)

site.who()
site.fn()