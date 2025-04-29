from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class CelesteArchipelagoOptions:
    celeste_include_farewell: CelesteIncludeFarewell
    celeste_include_bsides: CelesteIncludeBSides
    celeste_include_csides: CelesteIncludeCSides


class CelesteGame(Game):
    name = "Celeste"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = CelesteArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete CHAPTER",
                data={
                    "CHAPTER": (self.chapters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete CHAPTER after collecting at least BERRIES Strawberries",
                data={
                    "CHAPTER": (self.berry_chapters, 1),
                    "BERRIES": (self.berry_count_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Collect the Crystal Heart in CHAPTER",
                data={
                    "CHAPTER": (self.chapters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the following Chapters: CHAPTERS",
                data={
                    "CHAPTERS": (self.chapters, 3),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            )
        ]
    
    @property
    def include_farewell(self) -> bool:
        return bool(self.archipelago_options.celeste_include_farewell.value)
    
    @property
    def include_bsides(self) -> bool:
        return bool(self.archipelago_options.celeste_include_bsides.value)
    
    @property
    def include_csides(self) -> bool:
        return bool(self.archipelago_options.celeste_include_csides.value)

    @functools.cached_property
    def chapters_base() -> List[str]:
        return [
            "Forsaken City (A-Side)",
            "Old Site (A-Side)",
            "Celestial Resort (A-Side)",
            "Golden Ridge (A-Side)",
            "Mirror Temple (A-Side)",
            "Reflection (A-Side)",
            "The Summit (A-Side)",
            "Core (A-Side)",
        ]
    
    @functools.cached_property
    def chapters_bside() -> List[str]:
        return [
            "Forsaken City (B-Side)",
            "Old Site (B-Side)",
            "Celestial Resort (B-Side)",
            "Golden Ridge (B-Side)",
            "Mirror Temple (B-Side)",
            "Reflection (B-Side)",
            "The Summit (B-Side)",
            "Core (B-Side)",
        ]
    
    @functools.cached_property
    def chapters_cside() -> List[str]:
        return [
            "Forsaken City (C-Side)",
            "Old Site (C-Side)",
            "Celestial Resort (C-Side)",
            "Golden Ridge (C-Side)",
            "Mirror Temple (C-Side)",
            "Reflection (C-Side)",
            "The Summit (C-Side)",
            "Core (C-Side)",
        ]

    def chapters(self) -> List[str]:
        chapters: List[str] = self.chapters_base[:]

        if self.include_bsides:
            chapters.extend(self.chapters_bside[:])

        elif self.include_csides:
            chapters.extend(self.chapters_cside[:])

        elif self.include_farewell:
            chapters.extend(["Farewell"])

        return sorted(chapters)
    
    @staticmethod
    def berry_chapters() -> List[str]:
        return [
            "Forsaken City",
            "Old Site",
            "Celestial Resort",
            "Golden Ridge",
            "Mirror Temple",
            "The Summit",
        ]
    
    @staticmethod
    def berry_count_range() -> range:
        return range(5, 19)

# Archipelago Options
class CelesteIncludeFarewell(Toggle):
    """
    Indicates whether to include Chapter 9: Farewell when generating Celeste objectives.
    """

    display_name = "Celeste Include Farewell"

class CelesteIncludeBSides(Toggle):
    """
    Indicates whether to include Chapter B-Sides when generating Celeste objectives.
    """

    display_name = "Celeste Include B-Sides"

class CelesteIncludeCSides(Toggle):
    """
    Indicates whether to include Chapter C-Sides when generating Celeste objectives.
    """

    display_name = "Celeste Include C-Sides"