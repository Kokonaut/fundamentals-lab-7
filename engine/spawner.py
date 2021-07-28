from engine.monster import MonsterSprite


FAST_SPEED = 90
FAST_HEALTH = 35

HEAVY_SPEED = 35
HEAVY_HEALTH = 140


class Spawner:

    def __init__(self, monsters, batch, group=None):
        self.monsters = monsters
        self.monster_queue = list()
        self.spawned = list()
        self.interval = None
        self.intervals = list()
        self.batch = batch
        self.group = group

        self.monster_index = 0

        self.load_in_monsters()

    def load_in_monsters(self):
        for i in range(len(self.monsters)):
            spawn = self.monsters[i]
            self.monster_queue.append(self.load_monster(spawn))
            self.intervals.append(spawn.spawn_delay)
        self.interval = self.get_interval_to_next_spawn()

    def update(self, dt):
        self.run_spawn(dt)
        for sprite in self.spawned:
            sprite.update(dt)

    def run_spawn(self, dt):
        if len(self.monster_queue) == 0:
            return
        if self.interval <= 0:
            sprite = self.monster_queue.pop(0)
            self.spawned.append(sprite)
            print("Spawning monster: {id}".format(id=sprite.id))
            sprite.show()
            self.monster_index += 1
            self.interval = self.get_interval_to_next_spawn()
        else:
            self.interval -= dt

    def get_interval_to_next_spawn(self):
        if len(self.monster_queue) == 0:
            return 999
        next_spawn = self.intervals.pop(0)
        return next_spawn

    def load_monster(self, monster):
        sprite = MonsterSprite(
            monster.id,
            monster.assets,
            monster.x,
            monster.y,
            monster.path,
            monster,
            batch=self.batch,
            group=self.group
        )
        sprite.hide()
        return sprite
