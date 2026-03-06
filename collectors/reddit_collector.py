from .base_collector import BaseCollector
class RedditCollector(BaseCollector):
    def fetch(self):
        return [{"keyword":"solar night lamp","growth_rate":70,"volume":5000}]
    def parse(self, data): return data
    def save(self, data): pass
