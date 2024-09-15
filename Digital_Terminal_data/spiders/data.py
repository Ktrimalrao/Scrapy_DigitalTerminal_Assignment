import scrapy
import json

class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["https://digitalterminal.in/trending"]
    
    # Adding all URLs to scrape
    start_urls = [
        "https://digitalterminal.in/channel/redington-to-sell-latest-iphone-16-series-in-india",
        "https://digitalterminal.in/startup/aws-selects-seven-indian-startups-for-global-generative-ai-accelerator-program",
        "https://digitalterminal.in/trending/ai-and-automation-drive-50-faster-software-development-outsystems-and-kpmg-survey-reveals",
        "https://digitalterminal.in/tech-companies/commvault-report-reveals-increased-investment-in-cyber-resilience-by-breached-organizations",
        "https://digitalterminal.in/trending/dt-channel-survey-2024-navigating-opportunities-and-challenges-in-indias-it-channel",
        "https://digitalterminal.in/tech-companies/lt-semiconductor-and-ibm-to-collaborate-on-advanced-processor-innovations",
        "https://digitalterminal.in/device/canon-introduces-selphy-qx20-portable-photo-printer",
        "https://digitalterminal.in/trending/indian-businesses-face-growing-data-breach-threats-due-to-ai-sophistication-cloudflare-report",
        "https://digitalterminal.in/government/indian-government-rolls-out-enhanced-cybersecurity-measure-to-address-cyber-threats",
        "https://digitalterminal.in/channel/infopercept-appoints-ivalue-as-its-distributor-for-india-southeast-asia-and-saarc",
        "https://digitalterminal.in/solutions/tally-solutions-unveils-tallyprime-50-pioneers-api-based-gst-filing-for-msmes",
        "https://digitalterminal.in/tech-companies/optoma-india-reaches-milestone-with-official-registration",
        "https://digitalterminal.in/tech-companies/viewsonic-achieves-historic-epeat-gold-certification-for-sustainable-signage-displays",
        "https://digitalterminal.in/trending/kaspersky-to-host-first-asia-pacific-industrial-cybersecurity-conference-in-bangkok-this-october",
        "https://digitalterminal.in/device/acer-introduces-aspire-7-gaming-laptop-with-13th-gen-intel-and-nvidia-graphics",
        "https://digitalterminal.in/association-news/semi-and-iesa-forge-strategic-alliance-to-boost-indias-semiconductor-industry-at-semicon-india-2024",
        "https://digitalterminal.in/tech-companies/mediatek-hosts-catch-up-with-tech-meet-showcasing-advanced-smart-devices-with-motorola-and-flipkart",
        "https://digitalterminal.in/government/pm-modi-inaugurates-semicon-india-2024-conference-in-greater-noida",
        "https://digitalterminal.in/trending/apple-ships-made-in-india-iphone-16-to-global-markets-for-sale",
        "https://digitalterminal.in/trending/oracle-introduces-oci-zero-trust-packet-routing-to-prevent-data-breaches-from-network-misconfigurations"
    ]
    
    # List to store all articles data
    articles_data = []

    def parse(self, response):
        # Extract data using appropriate CSS selectors
        base_url = 'https://digitalterminal.in'
        article_url = response.url
        title = response.css("h1[data-testid='story-headline'] bdi::text").get()
        author_name = response.css('div[data-test-id="author-name"] a::text').get()
        relative_author_url = response.css('div[data-test-id="author-name"] a::attr(href)').get()
        # Construct the full author URL
        author_url = base_url + relative_author_url
        article_content = response.css("div[data-test-id='text'] p::text").getall()
        published_date = response.css("div[data-test-id='publishDetails'] time::text").get()

        # Structure the data in a dictionary for each article
        article_data = {
            "Article URL": article_url,
            "Title": title,
            "Author Name": author_name,
            "Author URL": author_url,
            "Article Content": " ".join(article_content),
            "Published Date": published_date
        }

        # Append each article data to the articles_data list
        self.articles_data.append(article_data)
        
        # When all articles are scraped, save them into a single JSON file
        if len(self.articles_data) == len(self.start_urls):
            filename = 'all_articles.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.articles_data, f, ensure_ascii=False, indent=4)

            self.log(f"Saved all articles to {filename}")
