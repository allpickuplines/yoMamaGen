import re

stopwords = []

for line in open('yoMamaSpider/stopwords.txt'):
    stopwords.append(line.strip('\n'))


def stripcats(cat):
    cat = re.sub(r'(?i)([^\w]|^\s+|[0-9])', '\n', str(cat))
    remainder = []
    words = cat.split('\n')
    for word in words:
        if word != '':
            if word.lower() not in stopwords:
                remainder.append(word)
    return ','.join(remainder)

def stripjokes(joke):
	return str(re.sub(' +', ' ', joke.replace('\"', "'")).replace('\r\n', '').strip())
