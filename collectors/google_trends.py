from .base_collector import BaseCollector
class GoogleTrendsCollector(BaseCollector):
    def fetch(self):
        return [{"keyword":"solar night light","growth_rate":85,"volume":12000}]
    def parse(self, data): return data
    def save(self, data): pass
