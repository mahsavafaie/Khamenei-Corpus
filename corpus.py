
import lxml.html, urllib.request
links = []
for year in range(1997,2020):
	for page in range(1,3):
		connection = urllib.request.urlopen('http://english.khamenei.ir/archive?pi={}&tp=2&ms=0&yr={}'.format(str(page),str(year)))
		dom =  lxml.html.fromstring(connection.read())
		for link in dom.xpath('//li[@class="clearfix"]//@href'):
			links.append(link)

print('\n'.join(links), len(links))
