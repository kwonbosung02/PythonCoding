
from bs4 import BeautifulSoup 
from urllib.request import urlopen

url="http://movie.naver.com/movie/sdb/rank/rmovie.nhn"

soup = BeautifulSoup(urlopen(url).read())

pkg_list=soup.findAll("div", "tit3")  

count = 1           

for i in pkg_list: 
	title = i.findAll('a')    
	print( count, "위: ", str(title)[str(title).find('title="')+7:str(title).find('">')])


	count=count+1  