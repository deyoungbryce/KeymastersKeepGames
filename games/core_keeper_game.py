from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class CoreKeeperArchipelagoOptions:
    corekeeper_include_nonfish_items: CoreKeeperIncludeNonFishItems
    corekeeper_include_rare_ingredients: CoreKeeperIncludeRareIngredients


class CoreKeeperGame(Game):
    name = "Core Keeper"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = CoreKeeperArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat the following Boss: BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat the following Boss with a CLASS weapon: BOSS",
                data={
                    "CLASS": (self.weapon_classes, 1),
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Obtain a FISH while fishing",
                data={
                    "FISH": (self.fishing, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Catch RANGE FISH",
                data={
                    "RANGE": (self.fishing_range, 1),
                    "FISH": (self.fish, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Hatch the following Pet: PET",
                data={
                    "PET": (self.pets, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Cook and eat a dish using the following ingredients: INGREDIENTS",
                data={
                    "INGREDIENTS": (self.ingredients, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]

    @property
    def include_nonfish_items(self) -> bool:
        return bool(self.archipelago_options.corekeeper_include_nonfish_items.value)
    
    @property
    def include_rare_ingredients(self) -> bool:
        return bool(self.archipelago_options.core_keeper_include_rare_ingredients.value)

    @staticmethod
    def bosses() -> List[str]:
        return [
            "Glurch, The Abominous Mass",
            "Ghorm, The Devourer",
            "Malugaz, The Corrupted",
            "Azeos, The Sky Titan",
            "Omoroth, The Sea Titan",
            "Ra-Akar, The Sand Titan",
            "Druidra, The Wild Titan",
            "Crydra, The Ice Titan",
            "Pyrdra, The Fire Titan",
            "Core Commander",
            "The Hive Mother",
            "Ivy, The Poisonous Mass",
            "Morpha, The Aquatic Mass",
            "Igneous, The Molten Mass",
            "King Slime",
            "Atlantean Worm",
            "Urschleim",
            "Nimruza, Queen of The Burrowed Sands",
        ]
    
    @staticmethod
    def weapon_classes() -> List[str]:
        return [
            "Melee",
            "Ranged",
            "Magic",
        ]
    
    @functools.cached_property
    def fishing_base(self) -> List[str]:
        return [
            "Orange Cave Gupppy",
            "Blue Cave Guppy",
            "Rock Jaw",
            "Gem Crab",
            "Yellow Blister Head",
            "Green Blister Head",
            "Devil Worm",
            "Vampire Eel",
            "Dagger Fin",
            "Pink Palace Fish",
            "Teal Palace Fish",
            "Crown Squid",
            "Azure Feather Fish",
            "Emerald Feather Fish",
            "Spirit Veil",
            "Astral Jelly",
            "Mold Shark",
            "Rot Fish",
            "Black Steel Urchin",
            "Bottom Tracer",
            "Silver Dart",
            "Golden Dart",
            "Pink Coralotl",
            "White Coralotl",
            "Solid Spikeback",
            "Sandy Spikeback",
            "Brown Dune Tail",
            "Grey Dune Tail",
            "Tornis Kingfish",
            "Dark Lava Eater",
            "Bright Lava Eater",
            "Elder Dragonfish",
            "Verdant Dragonfish",
            "Starlight Nautilus",
            "Beryll Angle Fish",
            "Glistening Deepstalker",
            "Jasper Angle Fish",
            "Splendid Deepstalker",
            "Cosmic Form",
            "Terra Trilobite",
            "Litho Trilobite",
            "Pinkhorn Pico",
            "Greenhorn Pico",
            "Riftian Lampfish",
        ]
    
    @functools.cached_property
    def non_fish(self) -> List[str]:
        return [
            "Green Kelp",
            "Scrap Parts",
            "Copper Ore",
            "Fiber",
            "Wood",
            "Rusty Spoon",
            "Amber Fish Egg",
            "Cave Guppy Necklace",
            "Scuba Fins",
            "Golden Starfish",
            "Copper Key",
            "Locked Copper Chest",
            "Crude Bomb",
            "Small Fish Pouch",
            "Yellow Kelp",
            "Tin Ore",
            "Mucus Amoeba",
            "Paraside Fossil",
            "Rusted Ring",
            "Neptune Necklace",
            "Golden Cocoon",
            "Grub Pearl",
            "Iron Key",
            "Locked Iron Chest",
            "Wildgarden Necklace",
            "Bomb",
            "Grey Kelp",
            "Iron Ore",
            "Gold Ore",
            "Soft Sponge",
            "Adder Stone",
            "Caveling Perfume",
            "Bubble Pearl Necklace",
            "Goldfish Ring",
            "Enhydro Crystal",
            "Trenchcoat",
            "Deceased Explorer",
            "Large Bomb",
            "Red Kelp",
            "Scarlet Ore",
            "Lost Paddle",
            "Feather Fish Scale",
            "Caveling Medal",
            "Rainbow Kelp",
            "Sea Foam Ring",
            "Scarlet Key",
            "Locked Scarlet Chest",
            "Mercenary Headband",
            "Mercenary Pants",
            "Mercenary Tank Top",
            "Scarlet Hand Drill",
            "Lily Pad Hat",
            "Lily Pad Tunic",
            "Lily Pad Shorts",
            "Pale Kelp",
            "Giant Germ",
            "Mold Shell",
            "Ceremonial Flute",
            "Data Slate",
            "Kelp Mantle",
            "Plague Mask",
            "Blue Kelp",
            "Octarine Ore",
            "Giant Squid Eye",
            "Golden Needle",
            "Polished Shell",
            "Opabinia Fossil",
            "Golden Jellyfish",
            "Diving Helm",
            "Octarine Key",
            "Locked Octarine Chest",
            "Octarine Sledge Hammer",
            "Wildwarden Pants",
            "Pearl Lantern",
            "Crescent Necklace",
            "Large Fish Pouch",
            "Flesh Kelp",
            "Galaxite Ore",
            "Ancient Fishing Hook",
            "Broken Gourd",
            "Broken Toy Ship",
            "Kingfish Scale",
            "Noble Ring",
            "Double Ring",
            "Oracle Card 'Temperance'",
            "Galaxite Key",
            "Locked Galaxite Chest",
            "Puppet Ring",
            "Desert Guardian Mask",
            "Desert Guardian Tunic",
            "Paladin Pants",
            "Large Fish Pouch",
            "Dark Blue Kelp",
            "Ancient Gemstone",
            "Ancient Fishing Hook",
            "Fusion Alloy",
            "Starlight Shards",
            "Miner's Protective Helm",
            "Fusioned Chunk Necklace",
            "Core Iris",
            "Crystal Kelp",
            "Solarite Ore",
            "Crystal Bone",
            "Triops Fossil",
            "Catalyst Gemstone",
            "Gleam Wood Seed",
            "Sunrice Seed",
            "Lunacorn Seed",
            "Solarite Key",
            "Ninja Cowl",
            "Ninja Garments",
            "Ninja Leggings",
            "Sulfur Bud",
            "Pandorium Ore",
        ]
    
    @staticmethod
    def fishing_range() -> range:
        return range(5, 16)
    
    def fishing(self) -> List[str]:
        fishing: List[str] = self.fishing_base[:]

        if self.include_nonfish_items:
            fishing.extend(self.non_fish[:])

        return sorted(fishing)
    
    def fish(self) -> List[str]:
        fish: List[str] = self.fishing_base[:]

        return sorted(fish)
    
    @staticmethod
    def pets() -> List[str]:
        return [
            "Subterrier",
            "Embertail",
            "Owlux",
            "Fanhare",
            "Electro-Pet",
            "Pheromoth",
            "Arcane Symbiote",
            "Snugglygrade",
            "Jr. Orange Slime",
            "Prince Slime",
            "Jr. Purple Slime",
            "Jr. Blue Slime",
            "Jr. Lava Slime",
        ]
    
    @functools.cached_property
    def ingredients_base(self) -> List[str]:
        return [
            "Mushroom",
            "Heart Berry",
            "Glow Tulip",
            "Bomb Pepper",
            "Carrock",
            "Bloat Oat",
            "Puffungi",
            "Pewpaya",
            "Pinegrapple",
            "Sunrice",
            "Lunacorn",
            "Grumpkin",
            "Orange Cave Guppy",
            "Blue Cave Guppy",
            "Rock Jaw",
            "Gem Crab",
            "Green Blister Head",
            "Yellow Blister Head",
            "Devil Worm",
            "Vampire Eel",
            "Dagger Fin",
            "Pink Palace Fish",
            "Teal Palace Fish",
            "Crown Squid",
            "Azure Feather Fish",
            "Emerald Feather Fish",
            "Spirit Veil",
            "Astral Jelly",
            "Mold Shark",
            "Rot Fish",
            "Black Steel Urchin",
            "Bottom Tracer",
            "Silver Dart",
            "Golden Dart",
            "Pink Coralotl",
            "White Coralotl",
            "Solid Spikeback",
            "Sandy Spikeback",
            "Brown Dune Tail",
            "Grey Dune Tail",
            "Tornis Kingfish",
            "Dark Lava Eater",
            "Bright Lava Eater",
            "Elder Dragonfish",
            "Verdant Dragonfish",
            "Starlight Nautilus",
            "Beryll Angle Fish",
            "Cosmic Form",
            "Glistening Deepstalker",
            "Jasper Angle Fish",
            "Spledid Deepstalker",
            "Terra Trilobite",
            "Litho Trilobite",
            "Pinkhorn Pico",
            "Greenhorn Pico",
            "Riftian Lampfish",
            "Larva Meat",
            "Marbled Meat",
            "Dodo Egg",
        ]
    
    @functools.cached_property
    def rare_ingredients(self) -> List[str]:
        return [
            "Golden Heart Berry",
            "Golden Glow Tulip",
            "Golden Bomb Pepper",
            "Golden Carrock",
            "Golden Bloat Oat",
            "Golden Puffungi",
            "Golden Pewpaya",
            "Golden Pinegrapple",
            "Golden Sunrice",
            "Golden Lunacorn",
            "Golden Grumpkin",
            "Shiny Larva Meat",
            "Giant Mushroom",
        ]
    
    def ingredients(self) -> List[str]:
        ingredients: List[str] = self.ingredients_base[:]

        if self.include_rare_ingredients:
            ingredients.extend(self.rare_ingredients[:])

        return sorted(ingredients)

# Archipelago Options
class CoreKeeperIncludeNonFishItems(Toggle):
    """
    Indicates whether to include non-fish items when generating Core Keeper fishing objectives.
    This would include many very rare items into the pool. (<1% chance)
    """

    display_name = "Core Keeper Include Non-Fish Items"

class CoreKeeperIncludeRareIngredients(Toggle):
    """
    Indicated whether to include rare ingredients when generating Core Keeper cooking objectives.
    This would include the golden/shiny variants of cooking ingredients.
    """

    display_name = "Core Keeper Include Rare Ingredients"