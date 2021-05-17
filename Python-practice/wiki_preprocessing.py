import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Data_pre-processing").content
soup = BeautifulSoup(response, 'html.parser', from_encoding = 'utf-8')
article = soup.find("div", id = 'mw-content-text').get_text()

punc = '''!()-[]{};:'"-=\,–<>./?@#$%^&*_~'''
for ele in article:
    if ele in punc:
        article = article.replace(ele, "")
#print(article)

article = article.lower()

article_list = article.split()

word_list = []
for word in article_list:
    if word not in word_list: 
        if word.find('http') != 0:
            word_list.append(word)

print(word_list)

with open('./sample_res/wikiwords.txt','w+') as writeArticle:
    for word in word_list:
        writeArticle.write(word)
        writeArticle.write("\n")

writeArticle.close()
