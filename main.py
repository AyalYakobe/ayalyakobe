from comcrawl import IndexClient

array_papers = ["https://www.nytimes.com/*", "https://www.wsj.com/*", "https://www.washingtonpost.com/*",
                "https://www.jpost.com/*", "https://www.haaretz.co.il/*", "https://www.chicagotribune.com/*",
                "https://www.latimes.com/*", "https://www.economist.com/*", "https://www.bbc.com/*"]

client = IndexClient(["2020-05", "2020-10", "2020-16", "2020-24",
                      "2020-29", "2020-34", "2020-40", "2020-45", "2020-50"])


def print_url(site, cli):
    cli.search(site, threads=10)

    cli.results = [res for res in cli.results if res['status'] == '200' and '2020' in res['urlkey']][:1000000000]
    for element in cli.results:
        if 'covid' in element.get('url'):
            if 'economy' in element.get('url'):
                print(element.get('url'))


for paper in array_papers:
    print_url(paper, client)
