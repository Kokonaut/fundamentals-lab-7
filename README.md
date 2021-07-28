# Lab 7: Tower Powers

## Intro
This week we will be working with our tower objects and creating some more interesting game elements.

Your game will soon be expanded to have 4 elemental tower types, each having a different strength and weakness. Also we will be adding status effects to our monster classes.

For this lab, we will be practicing our inheritance and OOP principles. Now that we have more monster and tower types, we need a better way to organize their various traits and functions.


## Set Up
* Click the green 'Code' button on the top right of this section.
* Find 'Download ZIP' option and click it
* Unzip the file and move it over to your 'workspace' folder (or wherever you keep your files)

* Find the folder and open the entire folder in VSCode
    * You can find it in your Files and right click on it. Use the "Open with VSCode" option
    * You can also open VSCode, go to 'File' > 'Open' and then find the lab folder

* With VSCode open, go to the top of your window and find `Terminal`
* Click `Terminal`
* Click `New Terminal`


## Game Explanation
This is an expanded version of tower defense with 4 tower types. The objective is to take down the monsters before they reach the destination flag.

If a monster reaches your flag, then you will lose a life. Lose all your lives, and you lose the game.

We expect 4 magic towers:
* Lightning
    * Tower with weak damage but low cooldown. Good for taking down lots of targets.
* Rock
    * Tower with high damage but high cooldown. Higher DPS than lightning, but is slower and can not handle a lot of targets.
* Poison
    * Tower with weak damage that can set the poison status effect. Good against high HP monsters, but takes a while for full damage to take effect.
* Ice
    * Tower with low damage, medium cooldown, and can slow monsters down. Good against all monsters, but can not take monsters down by itself.

We have 4 monster types:
* Fast
    * Most common monster with high speed and low HP.
* Heavy
    * Tanky monster with high HP and low speed.
* Shield
    * Monster with average traits, but ignores first couple counts of damage
* Speed
    * Monster with high HP and very low speed. Will gain speed everytime it gets hit.

## Lab Steps
* All the code you will need to edit is in `monsters/` and `towers/` folders
* Everything inside the `engine/` folder are the inner workings of the game. Feel free to take a look, but you won't need to change anything

### Set up Base Tower
First, before we start defining our elemental towers, we must set up a base tower as a parent class. The base tower will have all the shared attributes and functions that we expect all the other towers to have. This way, we don't need to repeat our code once we implement the other towers.

* Inside `towers/` folder, create the `base_tower.py` file
* Create a class with:
```python
class BaseTower:

    def __init__(self):
        pass

```

* This is an empty class and doesn't do anything at all (yet)
* Now let's figure out what we need to define for each tower (it's attributes)
* At the simplest, what we need for each tower:
    * We need to know how much damage the tower can do
    * We need to know how far this tower can reach
    * We need to know how long the cooldown for the tower is (how fast it can attack)

* Our game engine calls each tower, expecting that it has these attributes
    * tower.attack_damage
    * tower.attack_cooldown
    * tower.attack_radius

* Let's add these attributes to our init function
```python
class BaseTower:

    def __init__(self):
        self.attack_damage = None
        self.attack_cooldown = None
        self.attack_radius = None

```
* Do these actually do something? Not really!
* We define these at the base class so we know that the child classes have to override it. If a child class doesn't override it, then we can know that the value is None (instead of doesn't exist)
    * Remember, overriding means that a child implements its own version of a the parent class's attribute/method.

* Our game engine expects at least one more thing too. The behavior when a tower attacks a monster in its range!
* The game engine will first figure out which monsters are in range of a tower, and will then call:
    * tower.run_attack(monsters_in_range)

* Because of this, we must define a method on our class called run_attack!
* However, different towers have different attacks, so we can't define this generally. What we do intead is leave it open to interpretation! 
    * At the same time, if a child class of BaseTower DOESN'T define the attack function, we must throw an error, or else the game is broken!
```python
class BaseTower:

    def __init__(self):
        self.attack_damage = None
        self.attack_cooldown = None
        self.attack_radius = None
    
    def run_attack(self, monsters):
        raise NotImplementedError

```
* `raise NotImplementedError` will raise an error and cause our python program to stop. It indicates to us that a child class of tower has inherited that method, but did not override it! 
    * Since the child class did not override it, we can't define it's attack behavior, meaning that the game would be broken without it.
    * This is an OOP design principle. We define attributes/behaviours that a child class MUST implement on its own (due to its own special behavior)

### Set up Lightning Tower
* Awesome, we got started with our parent class! Now let's get into making some child classes.

* Create a new file in `towers/` folder called `lightning_tower.py`
* Inside, lets create an empty class that INHERITS from BaseTower
```python
from towers.base_tower import BaseTower


class LightningTower(BaseTower):

    def __init__(self):
        pass

```
* Notice how we had to import our parent class into the file.
* Also notice how we use the parent class inside of the child class declaration!
    * `class LightningTower(BaseTower):`
* Remember, we need to override four things from our parent class!
    * attack_damage
    * attack_radius
    * attack_cooldown
    * run_attack(monsters_in_range)

* Inside of the init function, define these attributes
```python
        self.attack_damage = 25
        self.attack_cooldown = 3
        self.attack_radius = 300
```

* For the lightning tower, our attack behavior is pretty basic.
    * Just pick a target and apply damage to it.
* Add this method to LightningTower
```python
    def run_attack(self, monsters_in_range):
        if len(monsters_in_range) == 0:
            return None
        monster = monsters_in_range[0]
        monster.take_damage(self.attack_damage)
        return monster
```
* This is a basic implementation, only selecting the first monster in range. In the future, try seeing if you can make this a better attack function!
* That's it! We have successfully created a child class of our BaseTower, that does everything our game engine expects it to!

### On your own
Let's have you set up the rock tower on your own! The rock tower should almost be identical to the lightning tower (you can even use the same `run_attack` method as LightningTower).

* Create a new file inside of `towers/` called `rock_tower.py`
* Inside that file, create a new child class called `RockTower` that inherits from `BaseTower`
* Rock tower should have these attributes:
    * attack damage of 80
    * attack cooldown of 6
    * attack radius of 200
* Rock tower can have a similar attack function as LightningTower. Just select a monster and damage it!

### Set up Ice Tower
Now let's set up the Ice Tower that can apply slow to our monsters!

* Create a new file inside of `towers/` called `ice_tower.py`
* Create a child class of `BaseTower` called `IceTower`
    * attack damage of 10
    * attack cooldown of 4
    * attack radius of 350
* Give it a similar run_attack function as `RockTower`
* It should look like:

```python
from towers.base_tower import BaseTower


class IceTower(BaseTower):

    def __init__(self):
        self.attack_damage = 10
        self.attack_cooldown = 2
        self.attack_radius = 350

    def run_attack(self, monsters_in_range):
        if len(monsters_in_range) == 0:
            return None
        monster = monsters_in_range[0]
        monster.take_damage(self.attack_damage)
        return monster
```

Now let's define our tower's ability!

* We COULD just directly modify the target monster's speed attribute, but that's not good OOP design. Instead, let's write a method in the `BaseMonster` class to apply the slow effect.
* Open up `monsters/base_monster.py`
* Add this method to the `BaseMonster` class
```python
    def apply_slow(self, speed_modifier):
        self.speed -= speed_modifier
        if self.speed < 10:
            self.speed = 10
```

* Notice how now we have a clear indictation what this status effect does, and a well defined way for our code to modify a monster's speed.
* Also notice how we don't want a negative or 0 speed. We want the minimum slow speed to be at least 5 pixels per second. If we didn't define this here, then every tower would need to repeat this code if we wanted to modify speed!

* Since we modified the `BaseMonster` class to have this method, now ALL children of BaseMonster will inherit this method! It's much more convenient to write it once, rather than repeat it over and over again.
* Now with this method available for all monsters, let's go back to our `IceTower`
* Add this attribute to our tower's `__init__` method
```python
        self.slow_amount = 10
```
* This is so we can clearly define the amount of speed we slow a monster down with on each attack!
* Now add this line to IceTower's `run_attack` method (right before we damage our target monster)
```python
        monster.apply_slow(self.slow_amount)
```

* You should now be done with the IceTower!

### Set up the Poison Tower
Setting the poisoned status effect is a bit trickier. We don't want this effect to stack, and we want to apply it temporarily. Also, we need to apply poision damage once per second if the character is poisoned.

We need to add a good amount of attributes and behaviors to our monsters so that they can keep track of poison status/damage.

#### Set up Monster poison status
Similar to how we handled the slow effects from `IceTower`, let's now add the poison effects to our `BaseMonster` class.

* Go into `monsters/base_monster.py`
* Inside of the `__init__` method, add these attributes
```python
        self.poison_time = 0
        self.poison_delay = 1
        self.poison_damage = 0
        self.is_poisoned = False
```
* Poison time will be the remaining time that a monster is poisoned. We activate poison status by setting it to > 0. Poison status runs out when it gets updated to < 0.
* Poison delay will be the remaining time until a monster takes poison damage. We want this to apply once a second, so we set it to 1.
* Poison damage will be the amount of damage per each poison. The tower class determines this, so we set it to 0.
* `is_poisoned` is a boolean indicating whether the monster is currently poisoned.

* Now add this method to the `BaseMonster` class
```python
    def update_poison(self, delta):
        self.poison_time -= delta
        self.poison_delay -= delta
        # Check if currently poisoned
        if self.poison_time <= 0:
            self.is_poisoned = False
        else:
            self.is_poisoned = True
        if self.is_poisoned:
            # Check if a second has passed and we should apply damage
            if self.poison_delay < 0:
                self.take_damage(self.poison_damage)
                self.poison_delay = 1
```

* Next fill in the `update_status` method to call `update_poison`
```python
    def update_status(self, timedelta):
        self.update_poison(timedelta)
```

* Our game engine will call `update_status` everytime we need to update a monster. The game attempts to do this as fast as possible (similar to how frames per second work). However the timing isn't perfect, so it'll pass in a `timedelta` argument.
    * `timedelta` is the duration between one point of time and another. In this case its the amount of seconds between the last time `update` was called and the current time.
* We use `timedelta` to decrement our variables, indicating the remaining poison time left, and the remaining time until next poison damage is applied.
* Once our variables go below 0, we apply necessary actions, such as setting poison status to false, or applying poison damage and resetting the timer back to 1.

* Next, let's have a public method for our monster class to expose the poison setting feature. Add this method:
```python
    def apply_poisoned(self, time, damage):
        self.poison_time = time
        self.poison_damage = damage
```
* This method allows our towers to set the poisoned status on monsters. We set the amount of time the monster is poisoned and the amount of damage it takes at each second.

Overall, your BaseMonster class should look like:
```python
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

        self.poison_time = 0
        self.poison_delay = 1
        self.poison_damage = 0
        self.is_poisoned = False

        # Filled in by children
        self.assets = None
        self.hp = None
        self.speed = None

    def update_status(self, delta):
        self.update_poison(delta)

    def update_poison(self, delta):
        self.poison_time -= delta
        self.poison_delay -= delta
        # Check if currently poisoned
        if self.poison_time <= 0:
            self.is_poisoned = False
        else:
            self.is_poisoned = True
        if self.is_poisoned:
            # Check if a second has passed and we should apply damage
            if self.poison_delay < 0:
                self.take_damage(self.poison_damage)
                self.poison_delay = 1

    def apply_slow(self, speed_modifier):
        self.speed -= speed_modifier
        if self.speed < 5:
            self.speed = 5

    def apply_poisoned(self, time, damage):
        self.poison_time = time
        self.poison_damage = damage

    def take_damage(self, damage):
        raise NotImplementedError

```

#### Set up Poison Tower
Now let's set up our actual poison tower.

* Inside `towers/` create a new file called `poison_tower.py`
* Create a class called `PoisonTower` that inherits from `BaseTower`
* Inside the `__init__` function, give these attributes
```python
        self.attack_damage = 10
        self.attack_cooldown = 3
        self.attack_radius = 250

        self.poison_duration = 5
        self.damage_from_poison = 5
```
* Create the `run_attack` method, and make sure to include this line:
```python
        monster.apply_poisoned(self.poison_duration, self.damage_from_poison)
```

### Run the game
Once you have all the towers defined, you can now run the game! Make sure all your files are saved and then use the command `python run.py`.

You should get a decent challenge of monsters and have a choice 4 towers to create into each tower slot.

### On your own
Our `run_attack` functions have been pretty basic so far, just pick the first monster and attack it. Using the strength of each tower, you should be able to define the function so that it can optimize its damage.

On your own, modify each tower's `run_attack` function to optimize the total effect it can have on the game.

Some suggestions:
* `PoisonTower` doesn't stack poison damage, but it's poison effect lasts a while. You can maximize damage output by having it attack unique targets each time. Try using a variable to change which monster in the list of `monsters_in_range` you target, every time the `run_attack` function gets called.
* `IceTower` can continuously slow enemies. It would best be used on tanky monsters with high HP, in order to let higher DPS towers take advantage. Change `run_attack` to have it target the highest HP monster in range (that also has a speed greater than 10).
* `LightningTower` has low damage, but attacks often. Have it target the low HP monsters so it can quickly pick off monsters and thin the herd.
* `RockTower` has high damage, but attacks less often. Have it target the higher HP monsters so it can maximize its DPS. If it one-shots a low HP monster, then that extra damage is wasted!

Also, if you feel that the monster challenge isn't great enough, feel free to add more monsters inside of `run.py` !

Good luck and have fun!
