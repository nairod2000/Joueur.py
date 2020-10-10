# Unit: A unit in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Unit(GameObject):
    """The class representing the Unit in the Coreminer game.

    A unit in the game.
    """

    def __init__(self):
        """Initializes a Unit with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bombs = 0
        self._building_materials = 0
        self._dirt = 0
        self._health = 0
        self._job = None
        self._max_cargo_capacity = 0
        self._max_health = 0
        self._max_mining_power = 0
        self._max_moves = 0
        self._mining_power = 0
        self._moves = 0
        self._ore = 0
        self._owner = None
        self._tile = None
        self._upgrade_level = 0

    @property
    def bombs(self):
        """The number of bombs being carried by this Unit. (0 to job cargo capacity - other carried materials).

        :rtype: int
        """
        return self._bombs

    @property
    def building_materials(self):
        """The number of building materials carried by this Unit. (0 to job cargo capacity - other carried materials).

        :rtype: int
        """
        return self._building_materials

    @property
    def dirt(self):
        """The amount of dirt carried by this Unit. (0 to job cargo capacity - other carried materials).

        :rtype: int
        """
        return self._dirt

    @property
    def health(self):
        """The remaining health of a Unit.

        :rtype: int
        """
        return self._health

    @property
    def job(self):
        """The Job this Unit has.

        :rtype: games.coreminer.job.Job
        """
        return self._job

    @property
    def max_cargo_capacity(self):
        """The maximum amount of cargo this Unit can carry.

        :rtype: int
        """
        return self._max_cargo_capacity

    @property
    def max_health(self):
        """The maximum health of this Unit.

        :rtype: int
        """
        return self._max_health

    @property
    def max_mining_power(self):
        """The maximum mining power of this Unit.

        :rtype: int
        """
        return self._max_mining_power

    @property
    def max_moves(self):
        """The maximum moves this Unit can have.

        :rtype: int
        """
        return self._max_moves

    @property
    def mining_power(self):
        """The remaining mining power this Unit has this turn.

        :rtype: int
        """
        return self._mining_power

    @property
    def moves(self):
        """The number of moves this Unit has left this turn.

        :rtype: int
        """
        return self._moves

    @property
    def ore(self):
        """The amount of ore carried by this Unit. (0 to job capacity - other carried materials).

        :rtype: int
        """
        return self._ore

    @property
    def owner(self):
        """The Player that owns and can control this Unit.

        :rtype: games.coreminer.player.Player
        """
        return self._owner

    @property
    def tile(self):
        """The Tile this Unit is on.

        :rtype: games.coreminer.tile.Tile
        """
        return self._tile

    @property
    def upgrade_level(self):
        """The upgrade level of this unit. Starts at 0.

        :rtype: int
        """
        return self._upgrade_level

    def build(self, tile, type):
        """ Builds a support, shield, or ladder on Unit's tile, or an adjacent Tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile to build on.
            type (str): The structure to build (support, ladder, or shield).

        Returns:
            bool: True if successfully built, False otherwise.
        """
        return self._run_on_server('build', tile=tile, type=type)

    def buy(self, resource, amount):
        """ Purchase a resource from the player's base or hopper.

        Args:
            resource (str): The type of resource to buy.
            amount (int): The amount of resource to buy.

        Returns:
            bool: True if successfully purchased, False otherwise.
        """
        return self._run_on_server('buy', resource=resource, amount=amount)

    def dump(self, tile, material, amount):
        """ Dumps materials from cargo to an adjacent tile. If the tile is a base or hopper tile, materials are sold instead of placed.

        Args:
            tile (games.coreminer.tile.Tile): The tile the materials will be dumped on.
            material (str): The material the Unit will drop. 'dirt', 'ore', or 'bomb'.
            amount (int): The number of materials to drop. Amounts <= 0 will drop all the materials.

        Returns:
            bool: True if successfully dumped materials, False otherwise.
        """
        return self._run_on_server('dump', tile=tile, material=material, amount=amount)

    def mine(self, tile, amount):
        """ Mines the Tile the Unit is on or an adjacent tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile the materials will be mined from.
            amount (int): The amount of material to mine up. Amounts <= 0 will mine all the materials that the Unit can.

        Returns:
            bool: True if successfully mined, False otherwise.
        """
        return self._run_on_server('mine', tile=tile, amount=amount)

    def move(self, tile):
        """ Moves this Unit from its current Tile to an adjacent Tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile this Unit should move to.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', tile=tile)

    def transfer(self, unit, resource, amount):
        """ Transfers a resource from the one Unit to another.

        Args:
            unit (games.coreminer.unit.Unit): The Unit to transfer materials to.
            resource (str): The type of resource to transfer.
            amount (int): The amount of resource to transfer.

        Returns:
            bool: True if successfully transfered, False otherwise.
        """
        return self._run_on_server('transfer', unit=unit, resource=resource, amount=amount)

    def upgrade(self):
        """ Upgrade this Unit.

        Returns:
            bool: True if successfully upgraded, False otherwise.
        """
        return self._run_on_server('upgrade')



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
