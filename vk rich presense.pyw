import vk_api
import pypresence
import time
import random

app_id = 
#код приложения с discord developer
#app id from discord developer page

vk_token = ""
#Токен вашей страницы вк, получать здесь https://vkhost.github.io/
#your vk profile token, get it here https://vkhost.github.io/

user_id =
#Цифры айди вашего профиля вк
#Numbers of your vk profile id

tip = ""

def run():
    try:
        presence = pypresence.Presence(app_id)
        presence.connect()
        vk_session = vk_api.VkApi(token=vk_token)
        vk = vk_session.get_api()

        while True:
            large_image = "vk"
            activity = {
                "large_image": large_image
            }
            res = vk.users.get(user_ids=user_id, fields="status")[0]

            if "status_audio" not in res:
                state = tip
                if "details" in activity:
                    activity.pop("details")

                large_image = "https://i.pinimg.com/originals/96/d2/29/96d229d8c1be97c0d8c297b16a65ae0d.gif"
                activity.update({'state': state, 'large_image': large_image})
            else:
                curr_music = res['status_audio']

                state = f"{curr_music['title']}"
                details = f"{curr_music['artist']}"
                large_image = "https://i.pinimg.com/originals/96/d2/29/96d229d8c1be97c0d8c297b16a65ae0d.gif"
                large_text = tip
                if 'album' in curr_music and 'thumb' in curr_music['album']:
                    large_image = curr_music["album"]["thumb"]["photo_300"]
                    large_text = curr_music["album"]["title"]

                activity.update(
                    {'state': "by "+details, 'details': f"{state}",
                     'large_image': large_image, 'large_text': large_text})

            presence.update(**activity)
            time.sleep(3)
    except OSError:
        print("Restarting.")
        run()


if __name__ == "__main__":
    run()
