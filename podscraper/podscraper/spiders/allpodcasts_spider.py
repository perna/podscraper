import scrapy
from podscraper.items import PodscraperItem

class AllPodcastsSipder(scrapy.Spider):
    name = "allpodcasts"
    allowed_domains = ["allpodcasts.com"]
    start_urls = [
        "http://www.allpodcasts.com/Tools/OPMLViewer.aspx?url=http://www.digitalpodcast.com/opml/digitalpodcast.opml",
    ]

    def parse(self, response):
        for item in response.css("#ctl00_body_Outlines > .opmlOutline > ul li"):
            for sel in item.css("ul li"):
                podcast = PodscraperItem()
                podcast["name"] = sel.css("a::text")[0].extract().strip()
                podcast["feed"] = sel.css("a").xpath('@href')[0].extract()

                yield podcast
