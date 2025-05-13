from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class TemplateArchipelagoOptions:
    template_include_hard_levels: TemplateIncludeHardLevels
    template_dlc_owned: TemplateDLCOwned

# Main Class
class TemplateGame(Game):
    name = "Template"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = TemplateArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot take UPGRADE",
                data={
                    "UPGRADE": (self.upgrades, 1),
                },
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Beat the following levels: LEVELS",
                data={
                    "LEVELS": (self.levels, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Beat LEVEL with CHARACTER",
                data={
                    "LEVEL": (self.levels, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat COUNT ENEMY in LEVEL",
                data={
                    "COUNT": (self.enemy_count, 1),
                    "ENEMY": (self.enemies, 1),
                    "LEVEL": (self.levels, 1),
                },
            ),
        ]

    # "Template Include Hard Stuff" Option Property
    @property
    def include_hard_levels(self) -> bool:
        return bool(self.archipelago_options.template_include_hard_levels.value)

    # "Template DLC Owned" Option Properties
    @property
    def dlc_owned(self) -> Set[str]:
        return self.archipelago_options.template_dlc_owned.value
    
    @property
    def has_dlc1(self) -> bool:
        return "DLC 1" in self.dlc_owned
    
    @property
    def has_dlc2(self) -> bool:
        return "DLC 2" in self.dlc_owned

    # Datasets
    @staticmethod
    def upgrades() -> List[str]:
        return [
            "Upgrade 1",
            "Upgrade 2",
            "Upgrade 3",
        ]
    
    @functools.cached_property
    def levels_base(self) -> List[str]:
        return [
            "Level 1",
            "Level 2",
            "Level 3",
        ]
    
    @functools.cached_property
    def hard_levels(self) -> List[str]:
        return [
            "Hard Level 1",
            "Hard Level 2",
            "Hard Level 3"
        ]
    
    def levels(self) -> List[str]:
        levels: List[str] = self.levels_base[:]

        # Check if hard levels are included, and include them if so
        if self.include_hard_levels:
            levels.extend(self.hard_levels[:])

        return sorted(levels)
    
    @functools.cached_property
    def characters_base(self) -> List[str]:
        return [
            "Character 1",
            "Character 2",
            "Character 3",
        ]
    
    @functools.cached_property
    def characters_dlc1(self) -> List[str]:
        return [
            "Character 4",
            "Character 5",
        ]
    
    @functools.cached_property
    def characters_dlc2(self) -> List[str]:
        return [
            "Character 6",
            "Character 7",
        ]
    
    def characters(self) -> List[str]:
        characters: List[str] = self.characters_base[:]

        # Check if player owns dlc and add in dlc characters if so
        if self.has_dlc1:
            characters.extend(self.characters_dlc1[:])

        if self.has_dlc2:
            characters.extend(self.characters_dlc2[:])

        return sorted(characters)
    
    @staticmethod
    def enemies() -> List[str]:
        return [
            "Enemy 1",
            "Enemy 2",
            "Enemy 3",
        ]

    # picks a random number from 20-30
    @staticmethod
    def enemy_count() -> range:
        return range(20, 31)

# Archipelago Options
class TemplateIncludeHardLevels(Toggle):
    """
    Indicates whether to include Hard Levels when generating Template objectives.
    """

    display_name = "Template Include Hard Levels"

class TemplateDLCOwned(OptionSet):
    """
    Indicates which DLC the player owns, if any.
    """

    display_name = "Template DLC Owned"
    valid_keys = [
        "DLC 1",
        "DLC 2",
    ]
    
    default = valid_keys