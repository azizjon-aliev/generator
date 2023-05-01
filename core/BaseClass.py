import re, inflect
from datetime import datetime


class BaseClass:
    def _snake_case(self, name: str):
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    def _get_plural_name(self, name: str) -> str:
        return inflect.engine().plural(name.lower())