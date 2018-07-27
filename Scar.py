import vkauth
import vk_api

vkz = vkauth.VKAuth(['messages', 'users'], '6644868',  '5.80')
vkz.auth()

access_token = vkz.get_token()
user_id = vkz.get_user_id()
vkz._close()

vk = vk_api.VkApi(token = access_token)

def write(s):
    vk.method('messages.send', {'peer_id': 200000001, 'message':s})#200000001
    
write('Рот ебал');