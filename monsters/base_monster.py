import uuid


class BaseMonster:

    # Offset needed to accurately flip sprite
    ANCHOR_OFFSET = 0

    def __init__(self, path, spawn_delay):
        if not path:
            raise ValueError("Need path for monster")
        initial_step = path[0]
        self.x = initial_step[0]
        self.y = initial_step[1]
        self.spawn_delay = spawn_delay
        self.path = path
        self.defeated = False
        self.id = uuid.uuid4()

        # Filled in by children
        self.assets = None
        self.hp = None
        self.speed = None

    def update_status(self, delta):
        pass

    def take_damage(self, damage):
        raise NotImplementedError
