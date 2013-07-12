import re

stopwords = []

for line in open('stopwords.txt'):
    stopwords.append(line.strip('\n'))
print 'stopwords = ' + str(stopwords)


def strip_stopwords(title):
    title = re.sub(r'(?i)([^\w]|^\s+)', '\n', str(title))
    remainder = []
    words = title.split('\n')
    for word in words:
        if word != '':
            if word.lower() not in stopwords:
                remainder.append(word)
    return ','.join(remainder)
