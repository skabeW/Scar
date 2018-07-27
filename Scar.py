import requests

import scar_methods
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType

TEST_CONFA = '2000000002'
STAVOCHKI = '2000000001'

def main():
    session = requests.Session()

    # Авторизация пользователя:
    login, password = 'scaronefromskabeone@gmail.com', 'MishaLox'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)
    
    def write(id, s):
        vk.messages.send(
            peer_id = id,
            message = s
        )
        
    write(TEST_CONFA, 'suka')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
            write(TEST_CONFA, 'Миша ' + event.text + '? а с ебалом че?')


if __name__ == '__main__':
    main()
