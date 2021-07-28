from monsters.base_monster import BaseMonster


class ShieldMonster(BaseMonster):

    # Offset needed to accurately flip sprite
    ANCHOR_OFFSET = 0.35

    def __init__(self, path, spawn_delay):
        super(ShieldMonster, self).__init__(path, spawn_delay)
        self.assets = 'assets/enemy_3/'
        self.hp = 120
        self.speed = 40
        self.shield = 2

    def take_damage(self, damage):
        if self.shield > 0:
            self.hp -= damage
        else:
            self.shield -= 1
            return
        if self.hp <= 0:
            self.hp = 0
            self.defeated = True
