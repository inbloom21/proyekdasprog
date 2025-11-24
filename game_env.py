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
        "Goblin" : [15, 2, 0],
        "Orc" : [20, 2, -1],
        "Troll" : [30, 6, -1],
        "Bandit" : [20, 4, 0]
    },
    'Forest' : {
        'Owlbear': [35, 6, -1],
        'Werewolf': [25, 4, 1],
        'Goblin Hexer': [18, 4, 1],
        'Ogre': [40, 8, -2],
        'Grick': [40, 6, 0],
    },
    'Desert' : {
        'Mummy': [18, 4, -2],
        'Giant Scorpion': [35, 6, 0],
        'Leucrotta': [40, 6, 1],
        'Meazel': [35, 4, 2],
        'Giant Spider': [30, 6, 1],
    },
    'Tundra' : {
        'Saber Toothed Tiger': [25, 6, 2],
        'Yeti': [40, 8, -1],
        'Winter Wolf': [18, 4, 1],
        'Polar Bear': [28, 6, 0],
        'Manticore': [40, 8, 1],
    },
    'Hills' : {
        'Basilisk': [35, 8, 0],
        'Griffon': [45, 6, 2],
        'Neogi': [40, 6, 0],
        'Harpy': [25, 4, 1],
        'Giant Vulture': [35, 4, 1],
    },
    'Swamp' : {
        'Ghoul': [15, 2, 0],
        'Giant Crocodile': [30, 6, -1],
        'Giant Snakes': [35, 4, 1],
        'Flail Snail': [40, 8, -2],
        'Wight': [20, 4, 0]
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