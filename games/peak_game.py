from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from enums import KeymastersKeepGamePlatforms


@dataclass
class PeakArchipelagoOptions:
    peak_include_side_quests: PeakIncludeSideQuests


class PeakGame(Game):
    name = "PEAK"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = []

    is_adult_only_or_unrated = False

    options_cls = PeakArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()

        objectives += [
            GameObjectiveTemplate(
                label="Climb past the LEVEL without losing a team member",
                data={
                    "LEVEL": (self.levels, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Eat the following food: FOOD",
                data={
                    "FOOD": (self.foods, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Cook and eat the following food: FOOD",
                data={
                    "FOOD": (self.foods, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Obtain and make use of the following equipment: EQUIPMENT",
                data={
                    "EQUIPMENT": (self.equipment, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]

        if self.include_side_quests:
            objectives += [
                GameObjectiveTemplate(
                    label="SIDE QUEST",
                    data={
                        "SIDE QUEST": (self.side_quests, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
            ]

        return objectives
    
    @property
    def include_side_quests(self) -> bool:
        return bool(self.archipelago_options.peak_include_side_quests.value)
    
    @staticmethod
    def levels() -> List[str]:
        return [
            "Shore",
            "Tropics",
            "Alpines",
            "Caldera",
            "Kiln",
        ]
    
    @staticmethod
    def foods() -> List[str]:
        return [
            "Trail Mix",
            "Granola Bar",
            "Thick Mints",
            "Sports Drink",
            "Airline Food",
            "Energy Drink",
            "Big Lollipop",
            "Red Crispberry",
            "Green Crispberry",
            "Yellow Crispberry",
            "Coconut",
            "Marshmallow",
            "Scorchberry",
            "Purple Kingberry",
            "Yellow Kingberry",
            "Green Kingberry",
            "Medicinal Root",
            "Yellow Berrynana",
            "Pink Berrynana",
            "Blue Berrynana",
            "Brown Berrynana",
            "Honeycomb",
            "Tick",
            "Yellow Clusterberry",
            "Orange Winderberry",
            "Yellow Winterberry",
            "Napberry",
            "Egg",
            "Chubby Shroom",
            "Cluster Shroom",
            "Bugle Shroom",
            "Button Shroom",
        ]
    
    @staticmethod
    def equipment() -> List[str]:
        return [
            "Bandages",
            "Medkit",
            "Rope Spool",
            "Anti-Rope Spool",
            "Piton",
            "Blowgun",
            "Rope Cannon",
            "Anti-Rope Cannon",
            "Chain Cannon",
            "Shelf Shroom",
            "Remedy Fungus",
            "Magic Bean",
            "Antidote",
            "Flare",
            "Faerie Lantern",
            "Heat Pack",
            "Bugle of Friendship",
            "Pirate's Compass",
            "Scout Effigy",
        ]
    
    @staticmethod
    def side_quests() -> List[str]:
        return [
            "Open an Ancient Luggage",
            "Slip on a Jellyfish",
            "Make a Bridge Collapse",
            "Slip on a Berrynana Peel",
            "Make a Sploding Bush Explode",
            "Make a Gassy Bush Release its Toxins",
            "Pull a Tick off of a fellow player",
            "Get Attacked by Bees",
            "Get Blinded by a Flashpod",
            "Get a Boost from a Geyser",
            "Serenade the Capybaras",
            "Bring Bing Bong to the Peak",
            "Escape the Island without eating any Packaged Food",
            "Escape the Island without using Equipment",
            "Escape the Island without taking any Fall Damage",
            "Cook Bing Bong",
            "Eat a Poisonous Shroom",
            "Signal for the Helicopter and then Jump off of the Mountain",
            "Save a teammate from dying",
        ]
    

# Archipelago Options
class PeakIncludeSideQuests(Toggle):
    """
    Indicates whether to include random side quests when generating PEAK objectives.
    This includes anything ranging from collecting a specific badge to reaching the Peak with an added challenge.
    """

    display_name = "PEAK Include Side Quests"