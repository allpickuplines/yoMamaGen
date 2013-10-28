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
            if word.lower() not in stopwords and word not in remainder:
                remainder.append(word.capitalize())
    return ' '.join(remainder)

def stripjokes(joke):
    joke = re.sub(' +', ' ', joke.replace('\"', "'"))
    joke = joke.replace('\r\n', '')
    joke = joke.replace("(", '')
    joke = joke.replace("\n\n\n", '')
    return joke
