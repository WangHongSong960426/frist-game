import os 
import random

def start():
    st = input('請輸入 !play! 開始遊戲: ')
    if st == '!play!':
        print('開始遊戲...')
    else:
        print('只能輸入 !play!')


def read_file(filename):
    lines = []
    with open(filename, 'r', encoding= 'utf-8') as f:
        for line in f:
            lines.append(line.strip().split(','))
    return lines


def frist():
    lines = []
    coin = 0
    level = 0
    health = 100
    hunger = 0
    name = input('你要幫這個遊戲的主角取甚麼名子? ')
    print('這個遊戲的玩法是: 有一些代碼可以使這個遊戲發生改變，像是 金幣 級數 生命 飢餓度 會改變')
    print('代碼有: 吃飯 吃飯有分大 中或小 吃飯能讓健康值上升 金幣和飢餓度下降')
    print('狩獵 狩獵有分高階 中階與低階 會依照該等級能讓金幣上升 級數上升 生命下降 和飢餓度下降或者上升')
    print('打架 打架也有分高階 中階與低階 會依照該等級能讓級數上升 生命下降 和飢餓度上升')
    print('探索 探索有分地區 像是 沙漠 森林...等等 會依照該地區能讓金幣 飢餓度 上升 和生命下降 ')
    print('離開 存檔離開')
    while True:
        c = input('請輸入代碼: ')
        if c == '吃飯':
            s = input('請輸入 大 中 小: ')
            if s == '大':
                coin -= 100
                hunger -= 80
                if health > 100:
                    health = 100  
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '中':
                coin -= 50
                hunger -= 35
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '小':
                coin -= 20
                hunger -= 10
                if health > 100:
                    hunger = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            else:
                print('只能輸入 大 中 小')
        if c == '狩獵':
            s = input('請輸入 高階 中階 低階: ')
            if s == '高階':
                coin += 90    
                hunger -= 20
                e = random.randint (70,95)
                health -= e
                l = random.randint (3,6)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '中階':
                coin += 40
                hunger -= 10
                e = random.randint (35,50)
                health -= e
                l = random.randint (1,4)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '低階':
                coin += 20
                hunger += 10
                e = random.randint (20,50)
                health -= e
                l = random.randint (0,2)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            else:
                print('只能輸入 高階 中階 低階')
        if c == '打架':
            s = input('請輸入 高階 中階 低階: ')
            if s == '高階':
                coin += 90
                hunger -= 20
                e = random.randint (70,95)
                health -= e
                l = random.randint (3,6)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '中階':
                coin += 40
                hunger -= 10
                e = random.randint (35,50)
                health -= e
                l = random.randint (1,4)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '低階':
                coin += 20
                hunger -= 10
                e = random.randint (20,50)
                health -= e
                l = random.randint (0,2)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            else:
                print('只能輸入 高階 中階 低階')
        if c == '探索':
            print('現在探索地區有: 高原 森林 草叢 冰山 都市 山地 峽谷 沙漠')
            s = input('你要探索哪裡? ')
            if s == '高原':
                coin += 20
                hunger -= 10
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '都市':
                coin += 30
                hunger -= 10
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '森林':
                coin += 25
                hunger -= 20
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '草叢':
                coin += 15
                hunger -= 15
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '冰山':
                coin += 20
                hunger -= 15
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '山地':
                coin += 20
                hunger -= 20
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '峽谷':
                coin += 25
                hunger -= 15
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '沙漠':
                coin +=10
                hunger -= 5
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
        if c == '離開':
            coin = str(coin)
            level = str(level)
            health = str(health)
            hunger = str(hunger)
            sf = [name, coin, level, health, hunger]
            return sf
            break
        else:
            print('只能輸入吃飯 狩獵 打架 探索 離開')


def second(lines):
    name = lines[-5]
    coin = lines[-4]
    coin = int(name)
    level = lines[-3]
    level = int(level)
    health = lines[-2]
    health = int(health)
    hunger = lines[-1]
    hunger = int(hunger)
    print('這個遊戲的玩法是: 有一些代碼可以使這個遊戲發生改變，像是 金幣 級數 生命 飢餓度 會改變')
    print('代碼有: 吃飯 吃飯有分大 中或小 吃飯能讓健康值上升 金幣和飢餓度下降')
    print('狩獵 狩獵有分高階 中階與低階 會依照該等級能讓金幣上升 級數上升 生命下降 和飢餓度下降或者上升')
    print('打架 打架也有分高階 中階與低階 會依照該等級能讓級數上升 生命下降 和飢餓度上升')
    print('探索 探索有分地區 像是 沙漠 森林...等等 會依照該地區能讓金幣 飢餓度 上升 和生命下降 ')
    print('離開 存檔離開')
    while True:
        c = input('請輸入代碼:　')
        if c == '吃飯':
            s = input('請輸入 大 中 小: ')
            if s == '大':
                coin -= 100
                hunger -= 80
                if health > 100:
                    health = 100  
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '中':
                coin -= 50
                hunger -= 35
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '小':
                coin -= 20
                hunger -= 10
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            else:
                print('只能輸入 大 中 小')
        if c == '狩獵':
            s = input('請輸入 高階 中階 低階: ')
            if s == '高階':
                coin += 90    
                hunger -= 20
                e = random.randint (70,95)
                helth -= e
                l = random.randint (3,6)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '中階':
                coin += 40
                hunger -= 10
                e = random.randint (35,50)
                health -= e
                l = random.randint (1,4)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            elif s == '低階':
                coin += 20
                hunger += 10
                e = random.randint (20,50)
                health -= e
                l = random.randint (0,2)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            else:
                print('只能輸入 高階 中階 低階')
        if c == '打架':
            s = input('請輸入 高階 中階 低階: ')
            if s == '高階':
                coin += 90
                hunger -= 20
                e = random.randint (70,95)
                helth -= e
                l = random.randint (3,6)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '中階':
                coin += 40
                hunger -= 10
                e = random.randint (35,50)
                health -= e
                l = random.randint (1,4)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '低階':
                coin += 20
                hunger -= 10
                e = random.randint (20,50)
                health -= e
                l = random.randint (0,2)
                level += l
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            else:
                print('只能輸入 高階 中階 低階')
        if c == '探索':
            print('現在探索地區有: 高原 森林 草叢 冰山 都市 山地 峽谷 沙漠')
            s = input('你要探索哪裡? ')
            if s == '高原':
                coin += 20
                hunger -= 10
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '都市':
                coin += 30
                hunger -= 10
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '森林':
                coin += 25
                hunger -= 20
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '草叢':
                coin += 15
                hunger -= 15
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '冰山':
                coin += 20
                hunger -= 15
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '山地':
                coin += 20
                hunger -= 20
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '峽谷':
                coin += 25
                hunger -= 15
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
            if s == '沙漠':
                coin +=10
                hunger -= 5
                if health > 100:
                    health = 100 
                print(name, '現在 金幣=', coin, '級數=', level, '生命=' , health, '飢餓度=', hunger)
        if c == '離開':
            coin = str(coin)
            level = str(level)
            health = str(health)
            hunger = str(hunger)
            sf = [name, coin, level, health, hunger]
            return sf
            break
        else:
            print('只能輸入吃飯 狩獵 打架 探索 離開')


def save(sf):
    with open('game.txt', 'w') as f:
            f.write[sf]


def main():
    lines = []
    sf = []
    start()
    filename = 'game.txt'
    if os.path.isfile(filename):
        print('找到了檔案')
        lines = read_file(filename)
        second(lines)
        save(sf)
    else:
        print('找不到檔案')
        frist()
        save(sf)


main()