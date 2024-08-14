from datetime import datetime

from api.config import Config
from pytz import timezone


def now():
    return datetime.now(tz=timezone(Config.TIMEZONE))
