import requests
import xmltodict

class QuarksCrawler():

    def __init__(self, urllist):
        self.urllist = urllist

    def get_astros(self, urls):
        """
        Returns list of python dicts that are of structure
        {
            'title': '',
            'url': '',
        }
        and the ones that are not present in `existing_urls`
        """
        urls = set(urls)

        content = []

        for crawl_url in self.urllist:
            page = requests.get(crawl_url)
            doc = xmltodict.parse(page.text)

            for page in doc['urlset']['url']:
                url = page['loc']
                title = url.split('/')[-2]

                if url not in urls:
                    print url, title
                    content.append({
                        'url': url,
                        'title': title
                    })
                    urls.add(url)

        return content
