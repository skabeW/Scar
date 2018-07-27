import vkauth
import vk_api
import time

vkz = vkauth.VKAuth(['messages', 'users'], '6162462', '5.52')
vkz.auth()

access_token = vkz.get_token()
user_id = vkz.get_user_id()
vkz._close()

vk = vk_api.VkApi(token = access_token)

def write(s):
    vk.method('messages.send', {'peer_id': 200000001, 'message':s})#200000001
    
write('Рот ебал');

values = {'out':0, 'count':100, 'time_offset':5}    

while True:
    response = vk.method('messages.get', values)
    time.sleep(5)
    for item in response['items'] :
        if item['title'] != ' ... ' :
            #print("{}".format(item['title']))
            if item['chat_id'] == 74 :
                vk.method('messages.markAsRead', {'peer_id':200000001, 'message_ids' : str(item['id'])})
                
                #print('{}'.format(item))
                input = open('StatMsg.txt')
                s = input.readlines()
                input.close()
                #print('{}'.format(s))
                iq = 0
                for i in s :
                    if i.find(str(item['user_id'])) == -1:
                        iq = iq+1
                        continue
                    k = i[i.rfind(' ')+1:len(i)]
                    print('{}'.format(k))
                    c = int(k)+1
                    print('{}'.format(i))
                    #print('{}'.format(' ' + k))
                    #print('{}'.format(' '+str(c)))
                    #i.replace(" " + k, " " + str(c))
                    s[iq] = i[0:len(i)-len(k)] + str(c) + '\n'
                    print('{}'.format(s))
                    break
                output = open('StatMsg.txt', 'w')
                #output.write(s[0])
                for i in s :
                    output.write(i)
                output.close()
                
                if item['body'].find('Скар') != -1 :
                    input = open('StatMsg.txt')
                    s = input.readlines()
                    input.close()
                    string = ""
                    for i in s :
                        string = string + i[i.find(' '):len(i)]
                    write(string)
    