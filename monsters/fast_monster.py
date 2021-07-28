from monsters.base_monster import BaseMonster


class FastMonster(BaseMonster):

    # Offset needed to accurately flip sprite
    ANCHOR_OFFSET = 0.2

    def __init__(self, path, spawn_delay):
        super(FastMonster, self).__init__(path, spawn_delay)
        self.assets = 'assets/enemy_2/'
        self.hp = 70
        self.speed = 90

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.defeated = True
