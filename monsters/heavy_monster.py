from monsters.base_monster import BaseMonster


class HeavyMonster(BaseMonster):

    # Offset needed to accurately flip sprite
    ANCHOR_OFFSET = 0.35

    def __init__(self, path, spawn_delay):
        super(HeavyMonster, self).__init__(path, spawn_delay)
        self.assets = 'assets/enemy_1/'
        self.hp = 240
        self.speed = 35

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.defeated = True
