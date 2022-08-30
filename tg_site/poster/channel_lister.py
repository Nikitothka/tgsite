from bs4 import BeautifulSoup
import requests
from django.conf import settings

def channel_lister():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    url = 'https://tgstat.ru/ratings/posts/entertainment/pt?sort=views'
    post = []
    try:
        r = requests.get(url, headers=headers)
        assert r.status_code == 200, r.status_code
        soup = BeautifulSoup(r.text, 'lxml')
        all_el = soup.find_all("a", class_="popup_ajax text-dark")
        for i in all_el:
            el = (str(i['href'])).split('@')
            if '/channel/' in el:
                post.append(el[1])
        return post
    except Exception as e:
        settings.python_logger.exception(msg=str(e))
        return None
