import interface
import requests
import vk_api
import os
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
                                        #longpoll.listen возвращает event тогда, 
    for event in longpoll.listen():     #когда происходит какое-то событие в вк
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ') #log в консоль
            
            if not interface.NewChat(event.peer_id): #Проверка, новая ли конфа
                write(event.peer_id, 'Я впервые в этой конфе')
                chatinfo = vk.messages.getChat(chat_id = event.peer_id - 2000000000)#Загружаем инфу из конфы
                interface.InitConfig(event.peer_id, chatinfo) #Создать новую конфу
                

if __name__ == '__main__':
    main()
