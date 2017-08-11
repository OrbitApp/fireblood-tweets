# Send to single device.

from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAEejQtwY:APA91bEN9fmcaBFI3pJRSFfyCN6aDKcMXzgg7wPGiVDcVfs2CPsRWtuNpu4QYZmBUUiMRIYT9V821zcxdJ7y_DcsC5EWDU0w5xs4u8qBP5AQBIbAtIHbIWx6GUJLSSVRn1xd0STW2G2j")



# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "dTiF1KGahSo:APA91bHcP0affwYlLqBp_yemQ2Rg057aqTXKzurIX_1SZ9tcclRLc90r7fvCS0q_Evj69YGVwsQ6cv-a8v75q4dY8cvUwjOWEF8TGcoLu7Pp3NS8x5HUZmzpghkIVhJCeTKti1CGpnGQ"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)



print result





