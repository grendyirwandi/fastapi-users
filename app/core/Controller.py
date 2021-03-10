import sys
from app.core.ConnectionDb import ConnectionDb


class Controller:
    def model(self, model):
        mod = __import__('app.models.'+model, fromlist=[model])
        mod = getattr(mod, model)
        return mod()