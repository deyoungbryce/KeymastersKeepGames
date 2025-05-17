from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MHWildsArchipelagoOptions:
    pass

class MHWildsGame(Game):
    name = "Monster Hunter Wilds"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = MHWildsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Slay the following Monster: MONSTER",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Slay AMOUNT of the following small monster: MONSTER",
                data={
                    "AMOUNT": (self.small_monster_range, 1),
                    "MONSTER": (self.small_monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Slay the following Monster with the WEAPON: MONSTER",
                data={
                    "WEAPON": (self.weapons, 1),
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Hunt 2 Monsters on the following stage: STAGE",
                data={
                    "STAGE": (self.stages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]

    @staticmethod
    def small_monsters() -> List[str]:
        return [
            "Baunos",
            "Blango",
            "Bulaqchi",
            "Ceratonoth",
            "Comaqchi",
            "Conga",
            "Dalthydon",
            "Gajios",
            "Gelidron",
            "Guardian Seikret",
            "Harpios",
            "Kranodath",
            "Nerscylla Hatchling",
            "Piragill",
            "Porkeplume",
            "Rafma",
            "Talioth",
            "Vespoid",
        ]
    
    @staticmethod
    def small_monster_range() -> range:
        return range(5, 11)
    
    @staticmethod
    def monsters() -> List[str]:
        return [
            "Ajarakan",
            "Arkveld",
            "Guardian Arkveld",
            "Balahara",
            "Blangonga",
            "Chatacabra",
            "Congalala",
            "Doshaguma",
            "Guardian Doshaguma",
            "Gore Magala",
            "Gravios",
            "Guardian Ebony Odogaron",
            "Guardian Fulgur Anjanath",
            "Gypceros",
            "Hirabami",
            "Jin Dahaad",
            "Lala Barina",
            "Lagiacrus",
            "Mizutsune",
            "Nerscylla",
            "Nu Udra",
            "Quematrice",
            "Rathalos",
            "Guardian Rathalos",
            "Rathian",
            "Rey Dau",
            "Rompopolo",
            "Uth Duna",
            "Xu Wu",
            "Yian Kut-Ku",
            "Zoh Shia",
        ]
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Great Sword",
            "Sword & Shield",
            "Dual Blades",
            "Long Sword",
            "Hunting Horn",
            "Lance",
            "Gunlance",
            "Hammer",
            "Switch Axe",
            "Charge Blade",
            "Insect Glaive",
            "Bow",
            "Light Bowgun",
            "Heavy Bowgun",
        ]
    
    @staticmethod
    def stages() -> List[str]:
        return [
            "Windward Plains",
            "Scarlet Forest",
            "Oilwell Basin",
            "Iceshard Cliffs",
            "Ruins of Wyveria",
            "Rimechain Peak",
            "Wounded Hollow"
        ]

# Archipelago Options