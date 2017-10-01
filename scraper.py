from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://opendata.camden.gov.uk/api/views/5rhh-fxna/rows.xml?accessType=DOWNLOAD"
districts_url = "https://opendata.camden.gov.uk/api/geospatial/p2bh-u5fm?method=export&format=KML"
council_id = 'E09000007'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations', 'xml')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts', 'kml')
districts_scraper.scrape()
