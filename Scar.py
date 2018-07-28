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
                write(event.peer_id, 'Шо ебанный рот погнали нахуй')
                chatinfo = vk.messages.getChat(chat_id = event.peer_id - 2000000000)#Загружаем инфу из конфы
                interface.InitConfig(event.peer_id, chatinfo) #Создать новую конфу
            
            
            if event.text[0:3] == '[id' : #Проверка на карму
                c = event.text[len(event.text)-1]
                vk.messages.send(
                    peer_id = event.peer_id,
                    message = interface.karma(str(event.user_id), event.text[3:event.text.find('|')], event.peer_id, c),
                    forward_messages = event.message_id
                )
            
            
            
            if event.text[0:5] == 'Карма' :
                msg = interface.showcarma(event.peer_id)
                print(msg)
                
                for i in range(len(msg)) :
                    res = vk.users.get(user_ids = msg[i][:9], name_case = 'gen')
                    msg[i] = 'У ' + res[0]['first_name'] + ' ' + res[0]['last_name'] + ' карма = ' + msg[i][msg[i].find('\t', 11): msg[i].rfind('\t')] + '\n'
                
                msg2 = ''
                for i in range(len(msg)) :
                    msg2 += msg[i]
                vk.messages.send(
                    peer_id = event.peer_id,
                    message = msg2,
                    forward_messages = event.message_id
                )

if __name__ == '__main__':
    main()
