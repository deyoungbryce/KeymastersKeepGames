from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DomeKeeperArchipelagoOptions:
    domekeeper_include_challenging_assignments: DomeKeeperIncludeChallengingAssignments

class DomeKeeperGame(Game):
    name = "Dome Keeper"
    platform = KeymastersKeepGamePlatforms.PC

    is_adult_only_or_unrated = False

    options_cls = DomeKeeperArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()

        objectives += [
            GameObjectiveTemplate(
                label="Complete a Relic Hunt | Dome: DOME | Character: CHARACTER | Starting Gadget: GADGET",
                data={
                    "DOME": (self.domes, 1),
                    "CHARACTER": (self.characters, 1),
                    "GADGET": (self.gadgets, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete the following Guild Assignment: ASSIGNMENT",
                data={
                    "ASSIGNMENT": (self.guild_assignments, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Add the following gadget to your dome and fully upgrade it: GADGET",
                data={
                    "GADGET": (self.other_gadgets, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
        ]
        if self.include_challenging_assignments:
            objectives += self.challenging_objectives()

        return objectives

    def challenging_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete the following Guild Assignment on the Challenging Difficulty: ASSIGNMENT",
                data={
                    "ASSIGNMENT": (self.guild_assignments, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]

    @property
    def include_challenging_assignments(self) -> bool:
        return bool(self.archipelago_options.domekeeper_include_challenging_assignments.value)

    @staticmethod
    def domes() -> List[str]:
        return [
            "Laser Dome",
            "Sword Dome",
            "Artillery Dome",
            "Tesla Dome",
        ]
    
    @staticmethod
    def characters() -> List[str]:
        return [
            "Engineer",
            "Assessor",
        ]
    
    @staticmethod
    def gadgets() -> List[str]:
        return [
            "Shield",
            "Repellant",
            "Orchard",
            "Droneyard"
        ]

    @staticmethod
    def other_gadgets() -> List[str]:
        return [
            "Auto Cannon",
            "Blast Mining",
            "Buzz Saw",
            "Condenser",
            "Dome Armor",
            "Drillbert",
            "Drilling Rig",
            "Furnace",
            "Iron Worms",
            "Lift",
            "Missile Launcher",
            "Mushroom Farm",
            "Probe",
            "Prospecting Meter",
            "Resource Converter",
            "Resource Packer",
            "Shockwave Hammer",
            "Spire",
            "Stun Laser",
            "Suit Blaster",
            "Teleporter",
            "Underground Station",
        ]
    
    @staticmethod
    def guild_assignments() -> List[str]:
        return [
            "Showdown",
            "Iron Contribution",
            "Upside Down",
            "Maze",
            "Projectile Hell",
            "Dense Iron",
            "Barren Lands",
            "Defective Weapon",
            "Heavy Hitters",
            "Swiss Cheese",
            "Logistical Problem",
            "High Risk",
            "Monster Masses",
            "Iron Shortage",
            "Mining Problem",
            "Cobalt Contribution",
        ]

# Archipelago Options
class DomeKeeperIncludeChallengingAssignments(Toggle):
    """
    Indicates whether to include challenging guild assignments when generating Dome Keeper objectives.
    """

    display_name = "Dome Keeper Include Challenging Assignments"