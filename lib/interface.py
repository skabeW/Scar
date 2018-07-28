# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:31:10 2018

@author: SkabeW
"""
import os
import datetime

def NewChat(peer_id) : #Проверяет, новая ли эта конфа или нет
    file_path = os.getcwd() + '/peer/' + str(peer_id) + '/'
    directory = os.path.dirname(file_path)
    return os.path.exists(directory)

def InitConfig(peer_id, chatinfo) : #Создает все необходимые папки и файлы для первичной конфигурации
    file_path = os.getcwd() + '/peer/' + str(peer_id) + '/'
    directory = os.path.dirname(file_path)
    os.mkdir(directory)
    
    f = open(file_path + 'config.txt', 'w')
    for i in chatinfo :
        f.write(i + '\n')
        f.write('\t' + str(chatinfo[i]) + '\n')
        f.write('\n')
    f.close()
    
    date = datetime.date.today()
    
    f = open(file_path + 'members.txt', 'w')
    for i in chatinfo['users'] :
        f.write(str(i) + '\t0\t0\t' + str(int(date.day)-1) + '\n')
    f.close()
    
def karmaUp(From_id, to_id):
    