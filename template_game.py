from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

#Replace "Game" with your game's name
@dataclass
class GameArchipelagoOptions:
    game_option_1: GameOption1
    includedlc: IncludeDLC

#Replace "GameName" with your game's name
class GameNameGame(Game):
    name = "GameName"
    #Set platform to whatever platform you're basing your implementation off of
    platform = KeymastersKeepGamePlatforms.PC

    #Set platforms_other to any other platforms that the game is playable on
    #Here are some of the more popular ones, but a full list can be found at:
    #https://github.com/SerpentAI/Archipelago/blob/kk/worlds/keymasters_keep/enums.py
    platforms_other = [
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    #Set this to true if your game is considered adult only or unrated 
    #(basically whether or not it would need to be on the After Dark Server)
    is_adult_only_or_unrated = False

    options_cls = GameArchipelagoOptions

    #Define any option game constraints here
    #label: constraint as presented in the Keymaster's Keep client
    #data: defines what lists to pull data from and the amount of data to pull
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            #This would read out as "Cannot use" and then a random item from the important_items list
            GameObjectiveTemplate(
                label="Cannot use ITEM",
                data={
                    "ITEM": (self.important_items, 1),
                }
            ),
            GameObjectiveTemplate(
                label="Cannot use CHARACTERS",
                data={
                    "CHARACTERS": (self.characters, 3),
                }
            )
        ]

    #Define all game objectives here.
    #label: objective as presented in the Keymaster's Keep client
    #data: defines what lists to pull data from and the amount of data to pull
    #is_time_consuming: whether or not the objective will take a while to complete
    #is_difficult: whether or not the objective should be considered difficult
    #weight: the objective's weight in the pool of this game's objectives.
    #Higher weight means you are more likely to have that objective be pulled
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
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
                label="Collect 5 COLLECTIBLE within TIME minutes",
                data={
                    "COLLECTIBLE": (self.collectibles, 1),
                    "TIME": (self.collect_time, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            )
        ]
    
    #Create datasets/lists here
    @staticmethod
    def characters() -> List[str]:
        return [
            "Character 1",
            "Character 2",
            "Character 3",
            "Character 4",
        ]
    
    @staticmethod
    def important_items() -> List[str]:
        return [
            "Important Item 1",
            "Important Item 2",
            "Important Item 3",
            "Important Item 4",
        ]

    @staticmethod
    def collectibles() -> List[str]:
        return [
            "Collectible Type 1",
            "Collectible Type 2",
            "Collectible Type 3",
        ]
    
    #range of 1-20
    @staticmethod
    def collect_time() -> range:
        return range(1, 21)

# Archipelago Options (YAML)

# Boolean (True/False) Value
class GameOption1(Toggle):
    """
    Option description here.
    """

    display_name = "Option name as presented in the YAML"

# Editable List of Options (example of DLCs to include)
class IncludeDLC(OptionSet):
    """
    Option description here.
    """

    display_name = "Option name as presented in the YAML"
    valid_keys = [
        "dlc 1",
        "dlc 2",
        "dlc 3",
    ]

    default = valid_keys