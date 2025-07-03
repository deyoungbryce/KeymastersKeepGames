from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class Destiny2ArchipelagoOptions:
    destiny_2_subclasses: Destiny2Subclasses


class Destiny2Game(Game):
    name = "Destiny 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = Destiny2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win 3 Crucible matches in any mode while playing SUBCLASS",
                data={
                    "SUBCLASS": (self.subclasses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete a Pathfinder in the PLAYLIST playlist",
                data={
                    "PLAYLIST": (self.playlists, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete a Dares of Eternity run with over 100K score while playing SUBCLASS",
                data={
                    "SUBCLASS": (self.subclasses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete DUNGEON",
                data={
                    "DUNGEON": (self.dungeons, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete RAID",
                data={
                    "RAID": (self.raids, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the current Grandmaster (or next highest difficulty if not available) Nightfall as SUBCLASS",
                data={
                    "SUBCLASS": (self.subclasses, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
        ]

    def subclasses(self) -> List[str]:
        return sorted(self.archipelago_options.destiny_2_subclasses.value)
    
    @staticmethod
    def playlists() -> List[str]:
        return [
            "Vanguard",
            "Crucible",
        ]
                
    @staticmethod
    def dungeons() -> List[str]:
        return [
           "Shattered Throne",
           "Pit of Heresy",
           "Prophecy",
           "Grasp of Avarice",
           "Duality",
           "Spire of the Watcher",
           "Ghosts of the Deep",
           "Warlord's Ruin",
           "Vesper's Host", 
        ]

    @staticmethod
    def raids() -> List[str]:
        return [
            "Vault of Glass",
            "Crota's End",
            "King's Fall",
            "Garden of Salvation",
            "Deep Stone Crypt",
            "Vow of the Disciple",
            "Root of Nightmares",
            "Salvation's Edge",
        ]

# Archipelago Options
class Destiny2Subclasses(OptionSet):
    """
    Indicates which Destiny 2 Subclasses can be used when generating objectives.
    """

    display_name = "Available Subclasses"
    valid_keys = [
            "Solar Hunter",
            "Arc Hunter",
            "Void Hunter",
            "Stasis Hunter",
            "Strand Hunter",
            "Prismatic Hunter",
            "Solar Titan",
            "Arc Titan",
            "Void Titan",
            "Stasis Titan",
            "Strand Titan",
            "Prismatic Titan",
            "Solar Warlock",
            "Arc Warlock",
            "Void Warlock",
            "Stasis Warlock",
            "Strand Warlock",
            "Prismatic Warlock",
        ]

    default = valid_keys