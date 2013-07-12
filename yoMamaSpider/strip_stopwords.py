import re

stopwords = []

for line in open('yoMamaSpider/stopwords.txt'):
    stopwords.append(line.strip('\n'))


def strip_title(title):
    title = re.sub(r'(?i)([^\w]|^\s+|[0-9])', '\n', str(title))
    remainder = []
    words = title.split('\n')
    for word in words:
        if word != '':
            if word.lower() not in stopwords:
                remainder.append(word)
    return ','.join(remainder)
