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
        if len(str(i)) < 9 :
            f.write(' ')
        f.write(str(i) + '\t0\t0\t' + str(int(date.day)-1) + '\n')
    f.close()
   

def karma(from_id, to_id, peer_id, c) : #Повышение Кармы 
    file_path = os.getcwd() + '/peer/' + str(peer_id) + '/'
    f = open(file_path + 'members.txt', 'r')
    
    date = datetime.date.today()
    
    i = 0
    q = -1
    for line in f:
        print(line)
        if from_id in line :
            q = i
        i += 1
    f.close()
    
    f = open(file_path + 'members.txt', 'r')
    data = f.readlines() 
    f.close()
        
    if data[q][len(data[q])-3:len(data[q])-1] == str(date.day) :
        return 'Вы использовали сегодня свое право на изменение кармы'
    else :
        f = open(file_path + 'members.txt', 'r')
        b = -1
        i = 0
        for line in f:
            if to_id in line :
                b = i
            i += 1
        f.close()
        
        if c == '+' : 
            c = 1 
        else :
            c = -1
            
        x = int(data[b][12:len(data[b])-3]) + c
        
        data[b] = to_id + '\t' + data[b][10] + '\t' + str(x) + '\t' + data[b][len(data[b])-3:]
        if len(to_id) < 9 :
            data[b] = ' ' + data[b]

        data[q] = data[q][:data[q].rfind('\t') + 1] + str(date.day) + '\n'
        
        f = open(file_path + 'members.txt', 'w')
        f.writelines(data)
        f.close()
        return 'Карма изменена'
    
def showcarma(peer_id) :
    file_path = os.getcwd() + '/peer/' + str(peer_id) + '/'
    f = open(file_path + 'members.txt', 'r')
    data = f.readlines()    
    f.close()
    
    return data
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    