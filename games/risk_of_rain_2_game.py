from __future__ import annotations

import functools
from typing import List, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class RiskofRain2ArchipelagoOptions:
    riskofrain2_dlc_owned: RiskofRain2DLCOwned

class RiskofRain2Game(Game):
    name = "Risk of Rain 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = RiskofRain2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete a run as CHARACTER",
                data={
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Open CHESTS chests in STAGE",
                data={
                    "CHESTS": (self.chests_count, 1),
                    "STAGE": (self.stages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS as CHARACTER",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete a run on Monsoon Difficulty as CHARACTER",
                data={
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            )
        ]
    
    @property
    def dlc_owned(self) -> Set[str]:
        return self.archipelago_options.riskofrain2_dlc_owned.value
    
    @property
    def has_sotv(self) -> bool:
        return "Survivors of The Void" in self.dlc_owned
    
    @property
    def has_sots(self) -> bool:
        return "Seekers of The Storm" in self.dlc_owned

    @functools.cached_property
    def characters_base(self) -> List[str]:
        return [
            "Acrid",
            "Artificer",
            "Bandit",
            "Captain",
            "Commando",
            "Engineer",
            "Heretic",
            "Huntress",
            "Loader",
            "MUL-T",
            "Mercenary",
            "REX",
        ]
    
    @functools.cached_property
    def characters_sotv(self) -> List[str]:
        return [
            "Railgunner",
            "Void Fiend",
        ]
    
    @functools.cached_property
    def characters_sots(self) -> List[str]:
        return [
            "Chef",
            "False Son",
            "Seeker",
        ]
    
    def characters(self) -> List[str]:
        characters: List[str] = self.characters_base[:]

        if self.has_sotv:
            characters.extend(self.characters_sotv[:])

        if self.has_sots:
            characters.extend(self.characters_sots[:])

        return sorted(characters)
    
    @functools.cached_property
    def stages_base(self) -> List[str]:
        return [
            "Distant Roost",
            "Titanic Plains",
            "Verdant Falls",
            "Abandoned Aqueduct",
            "Wetland Aspect",
            "Rallypoint Delta",
            "Scorched Acres",
            "Abyssal Depths",
            "Siren's Call",
            "Sundered Grove",
            "Sky Meadow",
        ]
    
    @functools.cached_property
    def stages_sotv(self) -> List[str]:
        return [
            "Siphoned Forest",
            "Aphelian Sanctuary",
            "Sulfur Pools",
        ]
    
    @functools.cached_property
    def stages_sots(self) -> List[str]:
        return [
            "Viscous Falls",
            "Shattered Abodes",
            "Disturbed Impact",
            "Reformed Altar",
            "Treeborn Colony",
            "Golden Dieback",
            "Prime Meridian",
            "Helminth Hatchery",
        ]
    
    def stages(self) -> List[str]:
        stages: List[str] = self.stages_base[:]

        if self.has_sotv:
            stages.extend(self.stages_sotv[:])

        if self.has_sots:
            stages.extend(self.stages_sots[:])

        return sorted(stages)

    @functools.cached_property
    def bosses_base(self) -> List[str]:
        return [
            "Beetle Queen",
            "Clay Dunestrider",
            "Grandparent",
            "Grovetender",
            "Imp Overlord",
            "Magma Worm",
            "Scavenger",
            "Solus Control Unit",
            "Stone Titan",
            "Wandering Vagrant",
            "Alloy Worship Unit",
            "Aurelionite",
            "Mithrix",
        ]

    @functools.cached_property
    def bosses_sotv(self) -> List[str]:
        return [
            "Xi Construct",
            "Voidling",
        ]
    
    @functools.cached_property
    def bosses_sots(self) -> List[str]:
        return [
            "False Son"
        ]
    
    def bosses(self) -> List[str]:
        bosses: List[str] = self.bosses_base[:]

        if self.has_sotv:
            bosses.extend(self.bosses_sotv[:])

        if self.has_sots:
            bosses.extend(self.bosses_sots[:])

        return sorted(bosses)
    
    @staticmethod
    def chests_count() -> range:
        return range(8, 13)

# Archipelago Options
class RiskofRain2DLCOwned(OptionSet):
    """
    Indicates which Risk of Rain 2 DLC the player owns, if any.
    """

    display_name = "Risk of Rain 2 DLC Owned"
    valid_keys = [
        "Survivors of The Void",
        "Seekers of The Storm",
    ]

    default = valid_keys