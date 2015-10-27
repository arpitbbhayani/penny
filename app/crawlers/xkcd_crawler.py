import urlparse
import requests

from lxml import html

class XkcdComic():

    def __init__(self, url):
        self.url = url

    def get_comics(self, urls):
        """
        Returns list of python dicts that are of structure
        {
            'title': '',
            'url': '',
        }
        and the ones that are not present in `existing_urls`
        """
        urls = set(urls)

        # Parse
        base_url = urlparse.urljoin(self.url, '/')

        page = requests.get(self.url)
        tree = html.fromstring(page.text)

        anchors = tree.xpath('//div[@id="middleContainer"]/a')

        content = []

        for anchor in anchors:
            url = urlparse.urljoin(base_url, anchor.get('href'))
            title = anchor.text

            page = requests.get(url)
            tree = html.fromstring(page.text)

            content_url = tree.xpath('//*[@id="comic"]//img/@src')[0]
            content_type = 'image'

            if url not in urls:
                print url, title, content_url, content_type
                content.append({
                    'url': url,
                    'title': title,
                    'content_url': content_url,
                    'content_type': content_type
                })
                urls.add(url)
                break

        return content
