buah = ["Jeruk", "Naga", "Pepaya", "Mangga"]
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
    #Enemy : HP, damage_dice, speed_modifier
    "Goblin" : [30, 2, 0],
    "Orc" : [50, 2, -1],
    "Troll" : [80, 8, -1],
    "Bandit" : [40, 4, 0]
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