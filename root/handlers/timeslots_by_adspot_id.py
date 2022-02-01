import json
from dataclasses import asdict

from root.handlers import BaseHandler


class TimeslotsByAdspotId(BaseHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    def get(self, id_):
        result = None
        timeslots = self.ms.get_timeslots_by_adspot_id(id_)
        if timeslots:
            result = asdict(timeslots)
        self.write(
            json.dumps(result)
        )