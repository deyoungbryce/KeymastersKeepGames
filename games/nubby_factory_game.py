from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class NubbyArchipelagoOptions:
    nubby_include_rare_items: NubbyIncludeRareItems


class NubbyGame(Game):
    name = "Nubby's Number Factory"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [

    ]

    is_adult_only_or_unrated = False

    options_cls = NubbyArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Obtain and upgrade the following item: ITEM",
                data={
                    "ITEM": (self.items, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a run using the following items: ITEMS",
                data={
                    "ITEMS": (self.items, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Purchase the following items from the Cafe in one run: ITEMS",
                data={
                    "ITEMS": (self.cafe_items, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a run using the following Black Market item: ITEM",
                data={
                    "ITEM": (self.black_market_items, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Purchase and trigger the PERK perk",
                data={
                    "PERK": (self.perks, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a run using the following supervisor: SUPERVISOR",
                data={
                    "SUPERVISOR": (self.supervisors, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Beat the CHALLENGE challenge",
                data={
                    "CHALLENGE": (self.challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]
    
    @property
    def include_rare_items(self) -> bool:
        return bool(self.archipelago_options.nubby_include_rare_items.value)

    @functools.cached_property
    def base_items(self) -> List[str]:
        return [
            "Pants",
            "Cactus",
            "Flame Thrower",
            "Monstrosity",
            "Crazy Straw",
            "Evil Goose",
            "Flaming Skull",
            "Sea Cucumber",
            "Pedro",
            "Finger Puppet",
            "Jacks",
            "1 Ton of Feathers",
            "Dancing Dino",
            "Squirmy",
            "Broken Socket",
            "Kazoo",
            "Uranium Rod",
            "Happy Seal",
            "Friendly Rock",
            "Tardigrade",
            "Plastic Tree",
            "Asbestos",
            "Cheese House",
            "Disguise",
            "Two Headed Turtle",
            "Poop Butt",
            "E-Block",
            "T-Block",
        ]
    
    @functools.cached_property
    def rare_items(self) -> List[str]:
        return [
            "Lobster Claw",
            "Nose",
            "Rubber Chicken",
            "Yeti",
            "Squid",
            "3D-Glasses",
            "Laser Pointer",
            "All-Seeing Pyramid",
            "Inflatable Dolphin",
            "Horse Pill",
        ]
    
    def items(self) -> List[str]:
        items: List[str] = self.base_items[:]

        if self.include_rare_items:
            items.extend(self.rare_items[:])

        return sorted(items)
    
    @staticmethod
    def cafe_items() -> List[str]:
        return [
            "Noodle",
            "Strawberry",
            "Tart Lard",
            "Croissant",
            "Donut",
            "HotDog-Dog",
            "Dave",
            "Shish Kebab",
            "Kidney Bean",
            "Pickle Rat",
            "Lentil",
            "Chip",
            "Avocado",
            "Fava Bean",
            "Starfruit",
            "Soup Crackers",
        ]
    
    @staticmethod
    def black_market_items() -> List[str]:
        return [
            "Jake the Snake",
            "Fly Agaric",
            "Toy Fish",
            "The Pointer",
            "The Mollusk",
            "Clay-Man-Guy",
            "Wingless Fly",
            "King Baby",
            "Mannequin Head",
            "Fish Man",
            "Pregnancy Test",
            "Ouroboros",
            "Alien",
            "Flibby Flobbies",
        ]

    @staticmethod
    def perks() -> List[str]:
        return [
            "Snakey",
            "Kebab",
            "Ray-Gun",
            "Speedy",
            "Battery",
            "Cheesy",
            "Waffle",
            "Chaotic",
            "Zombie",
            "Springy",
            "Mystery Box",
            "Trophy",
            "Penny",
            "Meaty",
            "Cubey",
            "Charity",
            "Candle",
            "Tornado",
            "Drainer",
            "House 'O' Cards",
            "Eggy",
            "Buckshot",
            "Void",
            "Enlightened",
            "Warlock",
            "Gourmet",
            "Lunar",
            "Croissant",
        ]
    
    @staticmethod
    def supervisors() -> List[str]:
        return [
            "Tony",
            "Octo-ny",
            "Tony Jr",
            "Goblony",
            "Mutant Tony",
            "Glass Tony",
            "Hunter Tony",
            "Balogna Tony",
            "Criminal Tony",
            "C.E.O Tony",
            "Immortal Tony",
        ]
    
    @staticmethod
    def challenges() -> List[str]:
        return [
            "Short on Change",
            "Plain Jane",
            "Nubbelocke",
            "One-Shot McGee",
            "Pol's Bane",
            "Amnesiac",
            "Pheebie Mode",
            "Times Up!",
            "Expiration Date",
            "Stay There!",
        ]

# Archipelago Options
class NubbyIncludeRareItems(Toggle):
    """
    Indicates whether to include rare and ultra rare items when generating Nubby's Number Factory objectives.
    This could require getting multiple rare or ultra rare items.
    """

    display_name = "Nubby Include Rare Items"