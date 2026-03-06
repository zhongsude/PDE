from .base_collector import BaseCollector
class ProductHuntCollector(BaseCollector):
    def fetch(self):
        return [{"keyword":"solar night lamp","growth_rate":50,"volume":3000}]
    def parse(self, data): return data
    def save(self, data): pass
