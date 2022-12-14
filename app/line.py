import requests


class LINENotifyBot:
    API_URL = "https://notify-api.line.me/api/notify"

    def __init__(self, access_token):
        self.__headers = {"Authorization": "Bearer " + access_token}

    def send(
        self,
        message,
        image=None,
        sticker_package_id=None,
        sticker_id=None,
    ):
        payload = {
            "message": message,
            "stickerPackageId": sticker_package_id,
            "stickerId": sticker_id,
        }
        files = {}
        if image != None:
            files = {"imageFile": open(image, "rb")}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
        )


# if __name__ == '__main__':
def line_bot(name1, name2, time):
    bot = LINENotifyBot(access_token="line-api-key")

    bot.send(
        message=f"{time}に{name1}さんと{name2}の論文輪講が予約されました。",
    )
