#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyfcm import FCMNotification
from pprint import pprint
push_service = FCMNotification(api_key="AAAAEejQtwY:APA91bEN9fmcaBFI3pJRSFfyCN6aDKcMXzgg7wPGiVDcVfs2CPsRWtuNpu4QYZmBUUiMRIYT9V821zcxdJ7y_DcsC5EWDU0w5xs4u8qBP5AQBIbAtIHbIWx6GUJLSSVRn1xd0STW2G2j")
registration_id="dTiF1KGahSo:APA91bHcP0affwYlLqBp_yemQ2Rg057aqTXKzurIX_1SZ9tcclRLc90r7fvCS0q_Evj69YGVwsQ6cv-a8v75q4dY8cvUwjOWEF8TGcoLu7Pp3NS8x5HUZmzpghkIVhJCeTKti1CGpnGQ"
message = "Hope you're having fun this weekend, don't forget to check today's news"
result = push_service.notify_single_device(registration_id=registration_id)
pprint(result)
result = push_service.notify_multiple_devices(registration_ids=[registration_id,registration_id,registration_id])
pprint(result)
result = push_service.notify_topic_subscribers(topic_name="global", message_body=message)
