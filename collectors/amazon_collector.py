from .base_collector import BaseCollector
class AmazonCollector(BaseCollector):
    def fetch(self):
        return [{"keyword":"solar night lamp","growth_rate":60,"volume":5000}]
    def parse(self, data): return data
    def save(self, data): pass
