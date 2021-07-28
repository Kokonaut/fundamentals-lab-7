import pyglet

from engine.tower_sprites.tower import TowerSprite
from engine.tower_sprites.lightning_tower import LightningTowerSprite
from engine.tower_sprites.rock_tower import RockTowerSprite


class ClickHandler:

    SLOT_CLICK_BOX_X = 100
    SLOT_CLICK_BOX_Y = 50

    TILE_CLICK_BOX_X = 20
    TILE_CLICK_BOX_Y = 20

    TILE_OFFSET_HEIGHT = 50
    TILE_OFFSET_WIDTH = 40

    def __init__(self, slots, towers, window, batch, group):
        self.slots = slots
        self.towers = towers
        self.window = window
        self.batch = batch
        self.focused = None
        self.group = group
        self.lightning_tile = self.build_lightning_tile()
        self.rock_tile = self.build_rock_tile()
        self.ice_tile = self.build_ice_tile()
        self.poison_tile = self.build_poison_tile()

    def build_lightning_tile(self):
        tile_1 = pyglet.resource.image('assets/tiles/lightning.png')
        tile_1.anchor_x = tile_1.width // 2
        tile_1.anchor_y = tile_1.height // 2
        lightning_tile = pyglet.sprite.Sprite(
            tile_1, x=0, y=0, batch=self.batch, group=self.group)
        lightning_tile.scale = 0.33
        lightning_tile.visible = False
        return lightning_tile

    def build_rock_tile(self):
        tile_2 = pyglet.resource.image('assets/tiles/rock.png')
        tile_2.anchor_x = tile_2.width // 2
        tile_2.anchor_y = tile_2.height // 2
        rock_tile = pyglet.sprite.Sprite(
            tile_2, x=0, y=0, batch=self.batch, group=self.group)
        rock_tile.scale = 0.33
        rock_tile.visible = False
        return rock_tile

    def build_ice_tile(self):
        tile_1 = pyglet.resource.image('assets/tiles/ice.png')
        tile_1.anchor_x = tile_1.width // 2
        tile_1.anchor_y = tile_1.height // 2
        ice_tile = pyglet.sprite.Sprite(
            tile_1, x=0, y=0, batch=self.batch, group=self.group)
        ice_tile.scale = 0.33
        ice_tile.visible = False
        return ice_tile

    def build_poison_tile(self):
        tile_1 = pyglet.resource.image('assets/tiles/poison.png')
        tile_1.anchor_x = tile_1.width // 2
        tile_1.anchor_y = tile_1.height // 2
        poison_tile = pyglet.sprite.Sprite(
            tile_1, x=0, y=0, batch=self.batch, group=self.group)
        poison_tile.scale = 0.33
        poison_tile.visible = False
        return poison_tile

    def handle_click(self, x, y):
        click_handled = False
        if not self.focused:
            for slot in self.slots:
                if self.slot_is_clicked(slot, x, y):
                    self.focused = self.slots[slot]
                    self.show_tiles(self.focused)
                    return True
        else:
            lightning_tile_xy = (self.lightning_tile.x, self.lightning_tile.y,)
            rock_tile_xy = (self.rock_tile.x, self.rock_tile.y,)
            ice_tile_xy = (self.ice_tile.x, self.ice_tile.y,)
            poison_tile_xy = (self.poison_tile.x, self.poison_tile.y,)
            if self.tile_is_clicked(lightning_tile_xy, x, y):
                self.towers[(self.focused.x, self.focused.y,)
                            ]['lightning_tower'].activate()
                click_handled = True
            elif self.tile_is_clicked(rock_tile_xy, x, y):
                self.towers[(self.focused.x, self.focused.y,)
                            ]['rock_tower'].activate()
                click_handled = True
            elif self.tile_is_clicked(ice_tile_xy, x, y):
                self.towers[(self.focused.x, self.focused.y,)
                            ]['ice_tower'].activate()
            elif self.tile_is_clicked(poison_tile_xy, x, y):
                self.towers[(self.focused.x, self.focused.y,)
                            ]['poison_tower'].activate()
            elif self.slot_is_clicked((self.focused.x, self.focused.y,), x, y):
                return True
            self.focused = None
            self.hide_tiles()
        return click_handled

    def show_tiles(self, slot):
        x = slot.x
        y = slot.y
        tile_down_x = x - self.TILE_OFFSET_WIDTH
        tile_up_y = y + self.TILE_OFFSET_HEIGHT
        tile_up_x = x + self.TILE_OFFSET_WIDTH
        tile_down_y = y - self.TILE_OFFSET_HEIGHT

        self.lightning_tile.x = tile_down_x
        self.lightning_tile.y = tile_up_y
        self.lightning_tile.visible = True

        self.rock_tile.x = tile_up_x
        self.rock_tile.y = tile_up_y
        self.rock_tile.visible = True

        self.ice_tile.x = tile_down_x
        self.ice_tile.y = tile_down_y
        self.ice_tile.visible = True

        self.poison_tile.x = tile_up_x
        self.poison_tile.y = tile_down_y
        self.poison_tile.visible = True

    def hide_tiles(self):
        self.lightning_tile.visible = False
        self.rock_tile.visible = False
        self.ice_tile.visible = False
        self.poison_tile.visible = False

    def slot_is_clicked(self, origin, x, y):
        clicked_x = (origin[0] - self.SLOT_CLICK_BOX_X < x
                     and x < origin[0] + self.SLOT_CLICK_BOX_X)
        clicked_y = (origin[1] - self.SLOT_CLICK_BOX_Y < y
                     and y < origin[1] + self.SLOT_CLICK_BOX_Y)
        return clicked_x and clicked_y

    def tile_is_clicked(self, origin, x, y):
        clicked_x = (origin[0] - self.TILE_CLICK_BOX_X < x
                     and x < origin[0] + self.TILE_CLICK_BOX_X)
        clicked_y = (origin[1] - self.TILE_CLICK_BOX_Y < y
                     and y < origin[1] + self.TILE_CLICK_BOX_Y)
        return clicked_x and clicked_y
