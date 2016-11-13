from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://opendata.camden.gov.uk/api/views/5rhh-fxna/rows.xml?accessType=DOWNLOAD"
districts_url = "https://opendata.camden.gov.uk/api/views/ta65-2szc/rows.json?accessType=DOWNLOAD"
council_id = 'E09000007'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts')
districts_scraper.scrape()
