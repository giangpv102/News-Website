from django.shortcuts import render
import feedparser
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    rss_feed_url = 'https://vnexpress.net/rss/tin-moi-nhat.rss'
    feed = feedparser.parse(rss_feed_url)
    
    it_rss = []
    for it in feed.entries:
        title = it.get('title')
        date = it.get('published')
        link = it.get('link')
        description = it.get('summary')
        description_soup = BeautifulSoup(description,'html.parser')
        description_text = description_soup.get_text()
        # print(description_text)
        img_tag = description_soup.find('img')
        print(description_text)
        img_src = ''
        if img_tag:
            img_src = img_tag['src']
            
        item_rss = {
            'title':title,
            'pub_date':date,
            'link':link,
            'description':description_text,
            'image':img_src
        }
        it_rss.append(item_rss)
         
    print(len(it_rss))
    return render(request, 'index.html',{'it_rss':it_rss})