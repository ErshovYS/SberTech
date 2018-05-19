# -*- coding: utf-8 -*-
import wikipedia

class WikiFinder():
    
    def __init__(self):
        self.text = ''
        self.content = ''
        self.url = ''
        self.links = []
        
    def __wrongs__(self, liststr):
        res = 0
        for i in self.text.split():
            if i in liststr:
                res += 1
        return -res
    
    def search(self, text):
        self.text = text
        # Поиск на русском?
        if u'а'<=text[0]<=u'я' or u'А'<=text[0]<=u'Я':
            wikipedia.set_lang('ru')
        res = wikipedia.search(text, 10)
        res.sort(key=self.__wrongs__)
        notfound = True
        i = 0
        while notfound:
            try:
                item = wikipedia.page(res[i])
                self.url = item.url
                self.content = item.content[:200].strip() + '...'
                #print(u'Рекомендуемые ссылки:')
                item.links.sort(key=self.__wrongs__)
                self.links = item.links[:3]
                notfound = False
            except wikipedia.exceptions.DisambiguationError as e:
                i+=1
        return self.url + '\n' + self.content