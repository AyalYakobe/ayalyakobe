from comcrawl import IndexClient

array_papers = ["https://www.nytimes.com/*", "https://www.wsj.com/*", "https://www.washingtonpost.com/*",
                "https://www.jpost.com/*", "https://www.haaretz.co.il/*", "https://www.chicagotribune.com/*",
                "https://www.latimes.com/*", "https://www.economist.com/*", "https://www.bbc.com/*",
                "https://www.npr.org/*", "https://www.usatoday.com/*", "https://www.theguardian.com/*",
                "https://www.miamiherald.com/*", "https://www.pewresearch.org/*", "https://www.brookings.edu",
                "https://www.rand.org/*", "https://www.cato.org/*", "https://www.propublica.org/*",
                "https://www.epi.org/*", "https://www.cepr.net/*", "https://www.cbpp.org/*",
                "https://www.hoover.org/*","https://european-union.europa.eu/*", "https://news.yahoo.com/*",
                "https://www.cnn.com/*", "https://www.foxnews.com/*", "https://www.nbcnews.com/*"]

client = IndexClient(["2020-05", "2020-10", "2020-16", "2020-24",
                      "2020-29", "2020-34", "2020-40", "2020-45",
                      "2020-50"])
c = 0


def print_url(site, cli):
    cli.search(site, threads=10)

    cli.results = [res for res in cli.results if res['status'] == '200' and '2020' in res['urlkey']]
    for element in cli.results:
        if ('covid' in element.get('url') or 'coronavirus' in element.get('url')) and 'economy' in element.get('url'):
            global c
            c += 1
            print(str(c) + " " + element.get('url'))


for paper in array_papers:
    print_url(paper, client)
