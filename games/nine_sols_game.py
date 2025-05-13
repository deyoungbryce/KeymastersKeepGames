from __future__ import annotations

import functools
from typing import List, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class NineSolsArchipelagoOptions:
    ninesols_objectives: NineSolsObjectives

class NineSolsGame(Game):
    name = "Nine Sols"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = NineSolsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()
        if self.objective_battlememories:
            objectives += self.battlememories_objectives()
        if self.objective_gifts:
            objectives += self.gifts_objectives()
        if self.objective_mapchips:
            objectives += self.mapchips_objectives()
        if self.objective_minibosses:
            objectives += self.minibosses_objectives()

        return objectives

    def battlememories_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat BOSS | Jades: THREE, TWO, ONE | Spell Style: STYLE | Arrow: ARROW",
                data={
                    "BOSS": (self.bosses, 1),
                    "THREE": (self.three_cost_jades, 1),
                    "TWO": (self.two_cost_jades, 3),
                    "ONE": (self.one_cost_jades, 1),
                    "STYLE": (self.spell_styles, 1),
                    "ARROW": (self.arrows, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS without using heals",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]
    
    def gifts_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Gift the GIFT to Shuanshuan",
                data={
                    "GIFT": (self.gifts, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
        ]
    
    def mapchips_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Collect the CHIP Map Data Chip from Shanhai",
                data={
                    "CHIP": (self.map_chips, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
        ]
    
    def minibosses_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat MINIBOSS",
                data={
                    "MINIBOSS": (self.minibosses, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
        ]

    @property
    def objectives(self) -> Set[str]:
        return self.archipelago_options.ninesols_objectives.value

    @property
    def objective_battlememories(self) -> bool:
        return "Battle Memories" in self.objectives
    
    @property
    def objective_gifts(self) -> bool:
        return "Shuanshuan Gifts" in self.objectives
    
    @property
    def objective_mapchips(self) -> bool:
        return "Map Data Chips" in self.objectives
    
    @property
    def objective_minibosses(self) -> bool:
        return "Minibosses" in self.objectives

    @staticmethod
    def minibosses() -> List[str]:
        return [
            "Baichang",
            "Kuiyan",
            "Yanren",
            "Lieguan",
            "Jiaoduan",
            "Wuqiang",
            "Shuigui",
            "Shangui",
            "Tieyan",
            "Huanxian",
            "Yinyue",
            "Tianshou",
            "Cixing",
            "Xingtian",
            "Kanghui",
            "Headless Xingtian"
        ]
    
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Yingzhao",
            "Goumang",
            "Yanlao",
            "Jiequan",
            "Lady Ethereal",
            "Ji",
            "The Fengs",
            "Eigong",
        ]

    @staticmethod
    def gifts() -> List[str]:
        return [
            "Four Treasures of the Study",
            "Multi-Tool Kit",
            "Ancient Sheet Music",
            "Unknown Seed",
            "Ready-to-Eat Rations",
            "Qiankun Board",
            "Tiandao Academy Periodical",
            "Kunlun Immortal Portrait",
            "GM Fertiliser",
            "Fusang Amulet",
            "Virtual Reality Device",
            "Antique Vinyl Record",
            "Sword of Jie",
            "Penglai Recipe Collection",
            "Red Guifang Clay",
        ]
    
    @staticmethod
    def map_chips() -> List[str]:
        return [
            "Power Reservoir",
            "Agricultural Zone",
            "Warehouse Zone",
            "Abandoned Mines",
            "Transmutation Zone",
            "Central Core",
            "Empyrean District",
            "Grotto of Scriptures",
            "Research Institute"
        ]
    
    @staticmethod
    def one_cost_jades() -> List[str]:
        return [
            "Pauper Jade",
            "Soul Reaper Jade",
            "Harness Force Jade",
            "Ricochet Jade",
            "Swift Descent Jade",
        ]
    
    @staticmethod
    def two_cost_jades() -> List[str]:
        return [
            "Stasis Jade",
            "Mob Quell Jade - Yin",
            "Mob Quell Jade - Yang",
            "Steely Jade",
            "Avarice Jade",
            "Cultivation Jade",
            "Immovable Jade",
            "Swift Blade Jade",
            "Health Thief Jade",
            "Reciprocation Jade",
            "Bearing Jade",
            "Divine Hand Jade",
            "Last Stand Jade",
            "Breather Jade",
            "Recovery Jade",
            "Medical Jade",
            "Quick Dose Jade",
            "Revival Jade",
        ]
    
    @staticmethod
    def three_cost_jades() -> List[str]:
        return [
            "Qi Blade Jade",
            "Focus Jade",
            "Hedgehog Jade",
            "Qi Swipe Jade",
            "Iron Skin Jade",
        ]
    
    @staticmethod
    def spell_styles() -> List[str]:
        return [
            "Qi Blast",
            "Water Flow",
            "Full Control",
        ]
    
    @staticmethod
    def arrows() -> List[str]:
        return [
            "Cloud Piercer",
            "Thunder Buster",
            "Shadow Hunter",
        ]


# Archipelago Options
class NineSolsObjectives(OptionSet):
    """
    Indicates which types of objectives will be generated for Nine Sols.
    Everything other than Battle Memories may require a time-consuming amount of progression or starting from a fresh save file.
    At least one objective type must be included here.
    """

    display_name = "Nine Sols Objectives"
    valid_keys = [
        "Battle Memories",
        "Shuanshuan Gifts",
        "Map Data Chips",
        "Minibosses",
    ]

    default = valid_keys