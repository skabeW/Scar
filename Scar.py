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

    # Авторизация группы (для групп рекомендуется использовать VkBotLongPoll):
    # при передаче token вызывать vk_session.auth не нужно
    
    #vk_session = vk_api.VkApi(token='d74b56a9d74b56a9d74b56a915d72e322ddd74bd74b56a98c10673b82fd8829405ee408')

    vk = vk_session.get_api()

    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)
    
    def write(id, s):
        vk.messages.send(
            peer_id = id,
            message = s
        )
    write(TEST_CONFA, 'suka')



if __name__ == '__main__':
    main()
