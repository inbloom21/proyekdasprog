buah = ["Jeruk", "Naga", "Pepaya", "Mangga"]
biome = ['Grassland', 'Forest', 'Desert', 'Tundra', 'Hills', 'Swamp']

armor = {
    # Armor : AC_modifier
    "Cloth" : 1,
    "Studded Leather" : 3,
    "Leather" : 2,
    "Plate" : 4,
    "Cloak" : 1
}
weapon = {
    # Weapon : damage
    "Shortsword" : 6,
    "Rapier" : 8,
    "Longsword" : 10,
    "Scimitar" : 6,
    "Mace" : 6,
    "Dagger" : 4,
    "Staff" : 4
}
spell = {
    # Spell : mana cost, damage_dice, effect
    "Fireball" : (5, 12, "Fire"),
    "Firebolt" : (3, 8, "Fire"),
    "Bullet" : (2, 6, "None"),
    "Cannon" : (7, 20, "None"),
    "Armor" : (4, 2, "None"),
    "Fog" : (2, 0, "Fog"),
    "Blind" : (5, 0, "Blind")
}
enemy = {
    'Grassland' : {
    #Enemy : HP, damage_dice, speed_modifier
        "Goblin" : [30, 2, 0],
        "Orc" : [50, 2, -1],
        "Troll" : [80, 8, -1],
        "Bandit" : [40, 4, 0]
    },
    'Forest' : {
        'Owlbear': [90, 10, -1],
        'Werewolf': [70, 6, 1],
        'Goblin Hexer': [40, 4, 1],
        'Ogre': [120, 12, -2],
        'Grick': [60, 6, 0],
    },
    'Desert' : {
        'Mummy': [55, 6, -2],
        'Giant Scorpion': [75, 8, 0],
        'Leucrotta': [85, 8, 1],
        'Meazel': [45, 4, 2],
        'Giant Spider': [65, 6, 1],
    },
    'Tundra' : {
        'Saber Toothed Tiger': [70, 8, 2],
        'Yeti': [90, 10, -1],
        'Winter Wolf': [80, 8, 1],
        'Polar Bear': [85, 8, 0],
        'Manticore': [95, 10, 1],
    },
    'Hills' : {
        'Basilisk': [75, 8, 0],
        'Griffon': [85, 8, 2],
        'Neogi': [55, 6, 0],
        'Harpy': [50, 4, 1],
        'Giant Vulture': [60, 6, 1],
    },
    'Swamp' : {
        'Ghoul': [45, 4, 0],
        'Giant Crocodile': [110, 12, -1],
        'Giant Snakes': [70, 6, 1],
        'Flail Snail': [85, 10, -2],
        'Wight': [65, 6, 0]
    }
}

status_base = {
    'Health' : 30,
    'AC' : 10,
    'Position' : 0,
    'Mana' : 6
}

armor_all = list(armor.keys())
weapon_all = list(weapon.keys())
spell_all = list(spell.keys())
enemy_all = list(enemy.keys())