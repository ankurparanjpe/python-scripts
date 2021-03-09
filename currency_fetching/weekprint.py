import pendulum
from datetime import datetime, timezone


dt_2020 = datetime(2020, 11, 27, tzinfo=timezone.utc)
print(int(dt_2020.timestamp()))

start = pendulum.yesterday('Europe/Berlin')
start = start.start_of('week')
start = start.strftime("%d")
print(start)

end = pendulum.yesterday('Europe/Berlin')
end = end.end_of('week')
print(end)
