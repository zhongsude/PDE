from .base_collector import BaseCollector
class TikTokCollector(BaseCollector):
    def fetch(self):
        return [{"keyword":"solar night lamp","growth_rate":75,"volume":10000}]
    def parse(self, data): return data
    def save(self, data): pass
