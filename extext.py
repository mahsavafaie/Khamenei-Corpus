from urllib.request import urlopen
import lxml.html
from lxml import etree
with open ('links.txt','r') as g:
    line = g.readline()
    num=1
    while len(line)>0:
        url=urlopen('http://english.khamenei.ir/{}'.format(line)).read()
        text=lxml.html.fromstring(url.decode('UTF-8'))
        date= text.xpath('//li[@class="date"]/text()')[0]
        title= text.xpath('//div[@class="item-noimg-title"]/h2/text()|//div[@class="item-title"]/h2/text()')[0]
        speech= ("\n").join(text.xpath('//div[@class="full-text"]/p/text()'))
        #creating the NAF file
        doc = etree.Element('NAF', version='v3')
        doc.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
        page=  etree.ElementTree(doc)
        header= etree.SubElement(doc,'nafHeader')
        fileDesc= etree.SubElement(header, 'fileDesc', creationtime=date, title=title)
        body= etree.SubElement(doc, 'raw')
        body.text= etree.CDATA(speech)
        filenum=str(num)
        with open ('Corpus/{}.naf'.format(filenum),'wb') as f:
            f.write(etree.tostring(page, encoding='unicode',pretty_print=True).encode('utf-8'))
        num += 1
        line= g.readline()

