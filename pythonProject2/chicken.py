import csv

class DataProcessing():

    def __init__(self,path):
        self.file_path=path
        with open(path,'r',encoding='utf-8') as file:
            reader=csv.reader(file)
            content=list()
            for line in reader:
                content.append(line)
        self.content=content

    def get_path(self):
        return self.file_path
    def get_content(self):
        return self.content

data=DataProcessing('random_numbers.csv')

print()


class Spider():
    def __init__(self,url,header=None):
        self.url=url
        self header=header
        self.content=requests.get(url)

    def get_soup(self):
        return BeautifulSoup(self.content.text,features:'html.parser')


my_spider=Spider('https://www.chinanews.com')
soup=my_spider.get_soup()
