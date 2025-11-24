import random
import time
import game_env
import game_string
import json
import os

player1 = {
    'Ability' : {
        'Strength' : 2,
        'Dexterity' : 3,
        'Constitution' : 2,
        'Wisdom' : 3
    },
    'Status' : {
        'Health' : 0,
        'AC' : 0,
        'Position' : 0,
        'Biome' : 'Grassland',
        'Mana' : 0,
        'In Combat' : False
    },
 
    'Buah' : {
        'Total Buah' : 0
    },
    'Equipment' : {
        'Armor' : 'Cloth',
        'Weapon' : 'Shortsword',
    },
    'Spell' : dict()
}

enemy = dict()
d_weapon_damage = game_env.weapon[player1['Equipment']['Weapon']]
help_command = game_string.help_command

#------------------------Save and load functions----------------------
def save(state):#tambah savean ke current_progress.json
    with open("current_progress.json", "w") as file:
        save_state = json.dumps(state, indent=4)
        file.write(save_state)

def load():#load savean dari current_progress.json
    with open("current_progress.json") as file:
        save_state = json.load(file)
        global player1
        player1 = save_state

#------------------------Else functions----------------------

def delay(sec): #ini fungsi delay, nanti penggunaannya delay(detik)
    time.sleep(sec)
    return ''

def set_in_combat(value): #ini buat ngubah "In Combat". fungsinya nanti biar ada beberapa perintah yang ga bisa dijalanin kalo lagi battle atau kebalikannya
    player1['Status']['In Combat'] = value

def dice(x): #ini randomize dadu aja 
    return random.randint(1, x) if x > 0 else 0

def armor_modifier(): #ini modifier stats buat awal game. belom jadi
    global player1
    player1['Status']['AC'] = game_env.status_base['AC']\
        + player1['Ability']['Dexterity']\
        + game_env.armor[player1['Equipment']['Armor']]

def damage_modifier():
    global d_weapon_damage
    d_weapon_damage = game_env.weapon[player1['Equipment']['Weapon']]

#------------------------Spawn functions----------------------

def spawn_enemy(): #ini tadi buat ngasih stats ke musuh
    current_biome = player1['Status']['Biome']
    name = random.choice(list(game_env.enemy[current_biome]))
    enemy['Name'] = name
    enemy['Health'] = game_env.enemy[current_biome][name][0]
    enemy['DMG'] = game_env.enemy[current_biome][name][1]
    enemy['DEX'] = game_env.enemy[current_biome][name][2]
    enemy['Effect'] = []

def spawn_fruit(): 
    fruit = random.choice(game_env.buah)
    player1['Buah']['Total Buah'] += 1
    print(f'Kamu menemukan buah: {fruit}!')
    delay(1)
    print(f'Jumlah buah sekarang: {player1["Buah"]["Total Buah"]}')

def spawn_weapon():
    weapon = random.choice(game_env.weapon_all)
    print(f'Kamu menemukan weapon: {weapon}. Saat ini kamu memakai: {player1["Equipment"]["Weapon"]}')
    delay(1)
    ans = input('Apakah ingin mengganti senjata dengan yang ditemukan? (y/n) ').strip().lower()
    if ans and ans[0] == 'y':
        player1['Equipment']['Weapon'] = weapon
        print(f'Weapon diganti menjadi {weapon}.')
        damage_modifier()

def spawn_armor():
    armor = random.choice(game_env.armor_all)
    print(f'Kamu menemukan armor: {armor}. Saat ini kamu memakai: {player1["Equipment"]["Armor"]}')
    delay(1)
    ans = input('Apakah ingin mengganti armor dengan yang ditemukan? (y/n) ').strip().lower()
    if ans and ans[0] == 'y':
        player1['Equipment']['Armor'] = armor
        print(f'Armor diganti menjadi {armor}.')
        armor_modifier()

def spawn_scroll():
    spell = random.choice(game_env.spell_all)
    print(f'Kamu menemukan spell scroll: {spell}. Kamu bisa cast spell ini saat pertarunganmu nanti.')
    delay(1)
    player1['Spell'][spell] = game_env.spell[spell]

def spawn_potion(potion):
    match potion:
        case 'mana':
            player1['Status']['Mana'] += 4
            print('Kamu menemukan sebuah mana potion. +4 Mana.')
            delay(1)
        case 'health':
            # simple health potion
            player1['Status']['Health'] += 10
            print('Kamu menemukan sebuah health potion. +10 Health.')
            delay(1)

def spawn_loot(): #ini buat spawn loot random. palingan nanti tiap loot bakal dibikin fungsi baru lagi aja
    d_100 = random.randint(1, 100)
    # 30% fruit, 10% weapon, 10% armor, 10% spell scroll, 20% mana potion, 20% health potion
    if d_100 > 70:
        spawn_fruit()
    elif d_100 >= 60:
        spawn_weapon()
    elif d_100 >= 50:
        spawn_armor()
    elif d_100 >= 40:
        spawn_scroll()
    elif d_100 >= 20:
        spawn_potion('mana')
    else:
        spawn_potion('health')
        

#------------------------Handler functions----------------------
def death_handler(): #ini kalau player mati
    if player1['Status']['Health'] > 0:
        return 0
    else:
        print('Health kamu habis, kamu kalah dalam permainan!')
        delay(1)
        return 1

def biome_handler():
    biome = random.choice(game_env.biome)
    player1['Status']['Biome'] = biome
    print(game_string.biome['Arrived'][biome])
    delay(1)
    print(f'----------Kamu sampai di {biome}----------')
    delay(1)

def jalan_handler(): #ini kalau player input jalan. niatnya setelah beberapa ratus/ribu meter nanti ganti
    #environment yang dimana musuh sama kondisinya ada yang beda
    if player1['Status']['In Combat'] == True:
        print('Kamu tidak dapat melanjutkan perjalanan saat dalam pertarungan\
            \nSelesaikan pertarungan ini atau ketik "help combat"')
        return 0
    player1['Status']['Position'] += 75
    print('Kamu berjalan sejauh 75 meter.')
    print('Jarak dari rumahmu sekarang adalah', player1['Status']['Position'], 'meter.')
    if player1['Status']['Position'] % 150 == 0: #____________________________________MODULUSNYA NANTI GANTI PAS FINAL PRODUCT, 150 BUAT TESTING DOANG
        biome_handler()
    d_10 = dice(10)
    if d_10 < 4:
        result = combat_handler()
        if result == 1:
            return 1
    if d_10 > 4:
        spawn_loot()
        if player1['Buah']['Total Buah'] == 5:
            print('Kamu berhasil mengumpulkan 5 buah, kamu menyelesaikan permainan ini!')
            return 1


def exit_handler(): #buat keluar dari game
    print('Terimakasih telah bermain!')
    exit()
    
def cek_enemy():
    print('---Enemy---')
    for item, value in enemy.items():
        print(f'{item}: {value}')

def cek_handler(category): #mirip mirip sama help_handler
    if category == 'enemy':
        cek_enemy()
        return 0
    if category.capitalize() not in player1 :
        print('Kategori tidak ditemukan. ketik "help cek"')
        return 0
    print('---' + category.capitalize() + '---')
    for item, value in player1[category.capitalize()].items():
        print(f'{item}: {value}')
    return 0

def help_handler(category): #ini kalau player input "help"
    if category not in help_command :
        print('Kategori tidak ditemukan.')
        return 0
    for item in help_command[category]: #ngambil dari help_command sesuai kategori help nya
        print(item)

def serang_handler(): #ini kalau player nyerang
    if dice(20) > 9:
        damage = dice(d_weapon_damage) + player1['Ability']['Strength']
        enemy['Health'] -= damage
        print(f'Kamu menyerang musuh dan memberikan {damage} damage!')
        return 1
    else:
        print('Kamu gagal menyerang musuh!')
        return 1


def spell_handler(spell): #ini belom jadi. niatnya buat spell tadi.
    #jadi disini, spell bakalan ngasih efek berbeda tiap jenisnya
    spell = spell.lower()
    spell = spell.capitalize()
    if spell not in player1['Spell']:
        print('Spell tidak diketahui.')
        return 0
    if player1['Status']['Mana'] < player1['Spell'][spell][0]:
        print('Spell kekurangan mana.')
        return 0
    player1['Status']['Mana'] -= player1['Spell'][spell][0]
    print(f'Kamu menggunakan spell {spell} dan menghabiskan {player1["Spell"][spell][0]} mana.')
    d_hit = dice(20) + player1['Ability']['Wisdom']
    if d_hit > 9:
        print('Hit!')
        print(f"Musuh terkena {player1["Spell"][spell][1]} damage.")
        damage = player1['Spell'][spell][1]
        enemy['Health'] -= damage
        enemy['Effect'].append(player1['Spell'][spell][2]) #efek spell, kayaknya bakal gw ubah lagi nanti
        return 1
    else:
        print('Tidak hit!')
        return 1

def kabur_handler(): #ini buat player kabur pas combat
    d_kabur = dice(20)
    if d_kabur + player1['Ability']['Dexterity'] > 12 + enemy['DEX']:
        print('Kamu berhasil kabur dari musuh')
        set_in_combat(False)
        print('Masukan perintah cek, jalan, help, atau exit.')
        return 0
    else:
        print('Kamu gagal kabur dari musuh')
        return 1

def enemy_handler(): #ini buat ngejalanin musuh. jadi musuh nyerang sama mati ada disini. ini dipanggil pas combat
    if enemy['Effect'] == 'Fire' and player1['Status']['Biome'] != 'Tundra':
        enemy['Health'] -= 2
        print("Musuh terkena 2 damage dari efek Fire")
    if enemy['Health'] <= 0:
        print(f'Kamu mengalahkan {enemy["Name"]}!')
        delay(1)
        if dice(2) == 1:
            spawn_loot()
        set_in_combat(False)
        enemy.clear()
        print('Masukan perintah cek, jalan, help, atau exit.')
        return
    d_20 = dice(20)
    if enemy['Effect'] == 'Fog':
        print('Kabutmu mengelilingi musuh. pandangannya menjadi kabur')
        d_20 -= 2
    if enemy['Effect'] == 'Blind':
        print('Musuh tidak bisa melihat')
        d_20 -= 10
    damage = dice(enemy['DMG'])
    if d_20 >= player1['Status']['AC']:
        print(f'Kamu terkena damage {damage} serangan musuh!')
        player1['Status']['Health'] -= damage
    else:
        print(f'{enemy['Name']} mencoba menyerang kamu, tetapi tidak kena!')

def save_handler():
    if player1['Status']['In Combat'] is True:
        print('Tidak bisa save saat dalam pertarungan.')
        return
    save(player1)
    print('Progres anda telah di save')

def load_handler():
    if player1['Status']['In Combat'] is True:
        print('Tidak bisa load saat dalam pertarungan.')
        return
    load()
    print('Berhasil load progres')

#------------------------Command maps----------------------
#jadi bakal ngejalanin fungsi sesuai input pemain
command_map = { #ini command saat ngga combat
    'jalan': jalan_handler,
    'exit': exit_handler,
    'cek': lambda arg= None: cek_handler(arg) if arg else print('Kategori harus disebutkan. ketik "help cek"'),
    'help': lambda arg= None: help_handler(arg) if arg else print('Kategori harus disebutkan.'),
    'save': save_handler,
    'load': load_handler
}

combat_command = { #ini command saat combat
    'cek': lambda arg= None: cek_handler(arg) if arg else print('Kategori harus disebutkan. ketik "help cek"'),
    'exit': exit_handler,
    'help': lambda arg= None: help_handler(arg) if arg else print('Kategori harus disebutkan.'),
    'serang' : serang_handler,
    'kabur' : kabur_handler,
    'spell' : lambda arg= None: spell_handler(arg) if arg else print('Jenis spell harus disebutkan. ketik "help combat"'),
    'jalan' : jalan_handler,
    'save': save_handler,
    'load': load_handler
}

#------------------------ Main handlers----------------------

def combat_handler():
    spawn_enemy()
    print(f"{enemy['Name']} muncul dari semak-semak!\nKetik serang, spell, atau kabur.")
    set_in_combat(True)
    while player1['Status']['In Combat'] == True and player1['Status']['Health'] > 0:
        input_player = input('>>>>>').lower()
        input_player = tuple(input_player.split(' '))
        if input_handler(*input_player) == 1:
            enemy_handler() #disini dipanggilnya. jadi setelah giliran player, musuh juga jalan/aksi
        if death_handler() == 1:
            set_in_combat(False)
            return 1
    return 0

def input_handler(*args): #ini buat ngehandle input playernya
    if not args or args[0] == "": #ini pake *args biar bisa ngambil 2 kata
        #jadi player bisa masukin "cek" atau "cek status"
        print("Masukkan perintah.")
        return
    cmd = args[0]
    arg = args[1] if len(args) > 1 else None
    func = command_map.get(cmd) if not player1['Status']['In Combat'] else combat_command.get(cmd)
    #ini func buat ngambil command map yang dipake
    if func:
        if arg is not None:
            return func(arg)
        else:
            return func()
    else:
        print('Perintah tidak dikenal.')

def start(): #ini buat masukin base stats nya
    player1['Status']['Health'] = game_env.status_base['Health'] + player1['Ability']['Constitution'] * 3
    armor_modifier()

def run_game(): #Ini fungsi buat ngejalanin game nya 
    print('Objective adalah tujuan utama dalam permainan ini, yaitu mengumpulkan buah-buahan tertentu sampai 5.\
        \nKamu akan berjalan menjauh dari rumahmu, dan menghadapi berbagai musuh serta mengumpulkan buah-buahan\
        \nMasukan perintah cek, jalan, help, atau exit untuk memulai permainan.')
    while True:
        input_player = input('>>>>>').lower()
        input_player = tuple(input_player.split(' '))
        result = input_handler(*input_player)
        if result == 1:
            break

def main(): #Ini fungsi buat main game nya. jadi bisa retry dan ngeloop terus kalo pengen retry.
    while True:
        set_in_combat(False)
        start()
        run_game()
        if player1['Status']['Health'] <= 0:
            retry_answer = input('Kamu kalah! Ingin coba lagi? (y/n)').strip().lower()
        else:
            retry_answer = input('Kamu menang! Ingin coba lagi? (y/n)').strip().lower()
        if retry_answer != 'y':
            print('Terimakasih telah bermain!')
            break

main()

#TO-DO:
# Spell Action
# Win condition


