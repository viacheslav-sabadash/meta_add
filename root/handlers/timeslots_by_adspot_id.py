from datetime import datetime, date
from typing import Optional

from root.handlers import BaseHandler


class TimeslotsByAdspotId(BaseHandler):
    async def get(self, id_: str, date_: Optional[str] = None):
        if date_ is not None:
            await self.send_json(
                self.ms.get_timeslots_by_adspot_id(int(id_), date.fromisoformat(date_))
            )
        else:
            await self.send_json(
                self.ms.get_timeslots_by_adspot_id(int(id_))
            )
