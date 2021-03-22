from zmanim.zmanim_calendar import ZmanimCalendar
from slack import WebClient

client = WebClient('xoxb-1587525278033-1575125138755-bcAvj7balyzss74JO1bRsKTj')

calendar = ZmanimCalendar()


class SunsetNotification:
    def __init__(self):
        return

    def sunset_time(self):
        sunset = calendar.sunset()

        sunset = str(sunset).split(' ')[1]
        sunset = sunset.split('.')[0]

        sunset_hour = str(sunset).split(':')[0]
        sunset_minute = str(sunset).split(':')[1]
        sunset_second = str(sunset).split(':')[2]

        if int(sunset_hour) >= 13:
            sunset_hour = int(sunset_hour) - 12
            text = (str(sunset_hour) + ':' + sunset_minute + ':' + sunset_second + ' pm')
            slack_message = self.post_message(text)
            print('Sent message to Slack')

    # client.chat_postMessage(channel='#notifications', text=sunset)

    def post_message(self, text):
        client.chat_postMessage(
            channel='#notifications',
            text=text
        )


# notification = SunsetNotification()
# notification.sunset_time()