__author__ = 'Bogdan'
#encoding=utf-8

import urllib2
import re, codecs

main_url = u'https://slovari.yandex.ru/'

def get_urls():
    arr = []
    letters_parse = u'<div class="b-book-info__index">' \
            u'<a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%90/">А</a>' \
            u'<a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%91/">Б</a>' \
            u'<a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%92/">В</a>' \
            u'<a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%93/">Г</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%94/">Д</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%95/">Е</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%96/">Ж</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%97/">З</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%98/">И</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%99/">Й</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%9A/">К</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%9B/">Л</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%9C/">М</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%9D/">Н</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%9E/">О</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%9F/">П</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A0/">Р</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A1/">С</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A2/">Т</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A3/">У</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A4/">Ф</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A5/">Х</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A6/">Ц</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A7/">Ч</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A8/">Ш</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%A9/">Щ</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%AD/">Э</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%AE/">Ю</a><a class="ajax" href="/~%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8/%D0%9C%D0%BE%D1%80%D1%84%D0%B5%D0%BC%D0%BD%D0%BE-%D0%BE%D1%80%D1%84%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C/~%D0%AF/">Я</a></div>'
    m = re.findall('href="/(.*?)">.</a>', letters_parse)
    for i in m:
        for x in xrange(1,201):
            arr.append(i + str(x))
    return arr

def get_page():
    pages = set()
    for k in get_urls():
        url = main_url+k
        req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"})
        page = urllib2.urlopen(req).read()
        page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')
        pages.add(page)
    return pages

def get_words():
    f = codecs.open('out.txt', 'ab', 'utf-8')
    for page in get_page():
        words = re.findall('">(\w+\s?.)</a></h3><div class="b-serp-item__text">(.*?)</div>', page, flags=re.U)
        if words:
            for a,b in (sorted((words), key=lambda x: x[0])):
                f.write(a + ';' + b)
                f.write('\r\n')
        else:
            continue
    f.close()

def sort_list():
    fout = codecs.open('out2.txt', 'w', 'utf8')
    f = codecs.open('out.txt', 'r', 'utf8')
    f1 = re.sub('[\., ](.*)\.?', ';' + '\\1', f.read())
    f2 = re.sub('[;\.](\r\n)', '\\1', f1, flags=re.U)
    f3 = re.sub('(\w+);([0-9]);(.*)\s\((.*)\)', '\\1' + ';' + '\\3' + ';' + '\\4' + ';' + '\\2', f2, flags=re.U)
    #print f3
    fout.write(f3)


sort_list()