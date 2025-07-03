from __future__ import annotations

import functools
from typing import List, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms



@dataclass
class NightreignArchipelagoOptions:
    nightreign_character_selection: NightreignCharacterSelection
    nightreign_boss_selection: NightreignBossSelection


class NightreignGame(Game):
    name = "Elden Ring Nightreign"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = NightreignArchipelagoOptions

    def optional_game_constraint_template(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_template(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with 3 CHARACTERs",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with CHARACTERS",
                data={
                    "BOSS": (self.bosses, 1),
                    "CHARACTERS": (self.characters, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]
    
    def characters(self) -> Set[str]:
        return self.archipelago_options.nightreign_character_selection.value
    
    def bosses(self) -> Set[str]:
        return self.archipelago_options.nightreign_boss_selection.value

#Archipelago Options
class NightreignCharacterSelection(OptionSet):
    """
    Indicates which Nightreign characters will be considered when generating Nightreign objectives.
    """

    display_name = "Nightreign Character Selection"

    valid_keys = [
        "Wylder",
        "Guardian",
        "Ironeye",
        "Duchess",
        "Raider",
        "Revenant",
        "Recluse",
        "Executor",
    ]

    default = valid_keys

class NightreignBossSelection(OptionSet):
    """
    Indicates which Nightreign bosses will be considered when generating Nightreign objectives.
    """

    display_name = "Nightreign Boss Selection"

    valid_keys = [
        "Tricephalos",
        "Gaping Jaw",
        "Sentient Pest",
        "Augur",
        "Equilibrious Beast",
        "Darkdrift Knight",
        "Fissure in the Fog",
        "Night Aspect",
        "the current Everdark Sovereign Boss",
    ]

    default = valid_keys