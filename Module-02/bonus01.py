from datetime import datetime
import pytz

local_timezone = pytz.timezone("Asia/Kuala_Lumpur")
localtime = datetime.now(pytz.utc).astimezone(local_timezone)

print(localtime.time())
