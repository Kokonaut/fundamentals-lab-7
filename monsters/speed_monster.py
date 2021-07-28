from monsters.base_monster import BaseMonster


class SpeedMonster(BaseMonster):

    # Offset needed to accurately flip sprite
    ANCHOR_OFFSET = 0.35

    def __init__(self, path, spawn_delay):
        super(SpeedMonster, self).__init__(path, spawn_delay)
        self.assets = 'assets/enemy_4/'
        self.hp = 200
        self.speed = 15

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.defeated = True
        self.speed += 5
