import re

stopwords = []

for line in open('yoMamaSpider/stopwords.txt'):
    stopwords.append(line.strip('\n'))


def striptags(tag):
    tag = re.sub(r'(?i)([^\w]|^\s+|[0-9])', '\n', str(tag))
    remainder = []
    words = tag.split('\n')
    for word in words:
        if word != '':
            if word.lower() not in stopwords:
                remainder.append(word)
    return ','.join(remainder)
