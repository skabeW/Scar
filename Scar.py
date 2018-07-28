import requests
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
        vk_session.auth(token_only=True) #Получение токена
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session) # ЛонгПолл для сообщений
    
    #Авторизация завершена
    
    def write(id, s): #Отправляет пользователю с таким id сообщение s
        vk.messages.send(
            peer_id = id,
            message = s
        )
        
    write(TEST_CONFA, '2day')    
                                        #longpoll.listen возвращает event тогда, 
    for event in longpoll.listen():     #когда происходит какое-то событие в вк
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
            write(TEST_CONFA, 'Миша ' + event.text + '? а с ебалом че?')
            vk.messages.send(
                    peer_id = TEST_CONFA,
                    message = 'Да я твой рот ебал',
                    forward_messages = event.message_id
                    )
            print('\n'.join(str(value) for value in event))


if __name__ == '__main__':
    main()
