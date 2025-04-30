from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class NineSolsArchipelagoOptions:
    pass

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
        return [
            GameObjectiveTemplate(
                label="Defeat the following Miniboss: MINIBOSS",
                data={
                    "MINIBOSS": (self.minibosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
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
                label="Gift the GIFT to Shuanshuan",
                data={
                    "GIFT": (self.gifts, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Acquire the CHIP Map Data Chip from Shanhai",
                data={
                    "CHIP": (self.map_chips, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat the following Miniboss and Boss: MINIBOSS, BOSS",
                data={
                    "MINIBOSS": (self.minibosses, 1),
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            )
        ]

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
        ]
    
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Yingzhao",
            "Goumang",
            "Xingtian",
            "Yanlao",
            "Kanghui",
            "Jiequan",
            "Lady Ethereal",
            "Ji",
            "The Fengs",
            "Headless Xingtian",
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
    def jades() -> List[str]:
        return [
            ""
        ]
    
    @staticmethod
    def spell_style() -> List[str]:
        return [
            ""
        ]
    
    @staticmethod
    def equipment() -> List[str]:
        return [
            ""
        ]


# Archipelago Options