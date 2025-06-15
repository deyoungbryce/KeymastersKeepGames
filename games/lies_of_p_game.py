from __future__ import annotations

import functools
import random
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class LiesOfPArchipelagoOptions:
    liesofp_include_weapon_objectives: LiesofPIncludeWeaponObjectives
    liesofp_include_difficulties: LiesofPIncludeDifficulties


class LiesOfPGame(Game):
    name = "Lies of P"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = LiesOfPArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Do not use consumables",
                data={},
            ),
            GameObjectiveTemplate(
                label="Play with LOAD load",
                data={
                    "LOAD": (self.weight, 1),
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()
        objectives += self.base_objectivess()
        if self.include_weapon_objectives:
            objectives += self.weapon_objectives()
        if self.include_difficulties:
            objectives += self.difficulty_objectives()
        
        return objectives
    
    def base_objectivess(self) -> List[GameObjectiveTemplate]:
        return [
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
                label="Defeat the following bosses in a Death March on any difficulty: BOSSES",
                data={
                    "BOSSES": (self.bosses, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]
    
    def weapon_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat BOSS while using the following weapon: WEAPON",
                data={
                    "BOSS": (self.bosses, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]
    
    def difficulty_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat BOSS on difficulty DIFFICULTY",
                data={
                    "BOSS": (self.bosses, 1),
                    "DIFFICULTY": (self.difficulty, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]
    
    @property
    def include_weapon_objectives(self) -> bool:
        return self.archipelago_options.liesofp_include_weapon_objectives.value
    
    @property
    def include_difficulties(self) -> bool:
        return self.archipelago_options.liesofp_include_difficulties.value
    
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Parade Master",
            "Scrapped Watchman",
            "King's Flame, Fuoco",
            "Fallen Archbishop Andreus",
            "Black Rabbit Brotherhood (V)",
            "King of Puppets",
            "Champion Victor",
            "Green Monster of the Swamp",
            "Corrupted Parade Master",
            "Black Rabbit Brotherhood (X)",
            "Laxasia the Complete",
            "Simon Manus, Arm of God",
            "Nameless Puppet",
            "Markiona, Puppeteer of Death",
            "Two-faced Overseer",
            "Anguished Guardian of the Ruins",
            "Arlecchino, the Blood Artist",
        ]
    
    @functools.cached_property
    def weapon_blades(self) -> List[str]:
        return [
            "Acidic Crystal Spear Blade",
            "Acidic Great Curved Sword Blade",
            "Arche's Guardian Blade",
            "Big Pipe Wrench Head",
            "Black Steel Cutter Blade",
            "Blind Man's Double-Sided Spear",
            "Bone-Cutting Sawblade",
            "Booster Glaive Blade",
            "Bramble Curved Sword Blade",
            "Carcass Crystal Axe Blade",
            "Circular Electric Chainsaw Blade",
            "City Longspear Blade",
            "Clock Sword Blade",
            "Coil Miolnir Head",
            "Cursed Knights Halberd Blade",
            "Dancer's Curved Sword Blade",
            "Electric Coil Stick Head",
            "Exploding Pickaxe Blade",
            "Fire Axe Blade",
            "Greatsword of Fate Blade",
            "Krat Police Baton Head",
            "Lavendetta Head",
            "Live Puppet's Axe Blade",
            "Lorenzini Bolt Blade",
            "Maniac's Pinwheel Blade",
            "Master Chef's Knife Blade",
            "Military Shovel Blade",
            "Pistol Rock Drill Blade",
            "Puppet's Saber Blade",
            "Puppet of The Future Welder's Blade",
            "Salamander Dagger Blade",
            "Silent Evangelist's Mace Head",
            "Spear of Honor Blade",
            "Tyrant Murderer's Dagger Blade",
            "Wintry Rapier's Blade",
        ]
    
    @functools.cached_property
    def weapon_handles(self) -> List[str]:
        return [
            "Acidic Crystal Spear Handle",
            "Acidic Great Curved Sword Handle",
            "Arche's Guardian Handle",
            "Big Pipe Wrench Handle",
            "Black Steel Cutter Handle",
            "Blind Man's Double Sided Spear Handle",
            "Bone-Cutting Handle",
            "Booster Glaive Handle",
            "Bramble Curved Sword Handle",
            "Carcass Crystal Axe Handle",
            "Circular Electric Chainsaw Handle",
            "City Longspear Handle",
            "Clock Sword Handle",
            "Coil Miolnir Handle",
            "Cursed Knight's Halberd Handle",
            "Dancer's Curved Sword Handle",
            "Electric Coil Stick Handle",
            "Exploding Pickaxe Handle",
            "Fire Axe Handle",
            "Greatsword of Fate Handle",
            "Krat Police Baton Handle",
            "Lavendetta Handle",
            "Live Puppet's Axe Handle",
            "Lorenzini Bolt Handle",
            "Maniac's Pinwheel Handle",
            "Master Chef's Knife Handle",
            "Military Shovel Handle",
            "Pistol Rock Drill Handle",
            "Puppet's Saber Handle",
            "Puppet of The Future Welder's Handle",
            "Salamander Dagger Handle",
            "Silent Evangelist's Mace Handle",
            "Spear of Honor Handle",
            "Tyrant Murderer's Dagger Handle",
            "Wintry Rapier Handle",
        ]
    
    @functools.cached_property
    def special_weapons(self) -> List[str]:
        return [
            "Death's Talons",
            "Monad's Rose Sword",
            "Pale Knight",
            "Royal Horn Bow",
            "Azure Dragon Crescent Glaive",
            "Etiquette",
            "Frozen Feast",
            "Golden Lie",
            "Holy Sword of The Ark",
            "Noblesse Oblige",
            "Proof of Humanity",
            "Puppet Ripper",
            "Seven-Coil Spring Sword",
            "Trident of The Covenant",
            "Two Dragon's Sword",
            "Uroboros's Eye",
        ]
    
    def weapons(self) -> List[str]:
        weapons: List[str] = self.special_weapons[:]
        random_blade: List[str] = random.sample(self.weapon_blades, len(self.weapon_blades))
        random_handle: List[str] = random.sample(self.weapon_handles, len(self.weapon_handles))

        assembled_weapons = []
        for a, b in zip(random_blade, random_handle):
            assembled_weapons.append(a + " + " + b)

        weapons.extend(assembled_weapons[:])

        return sorted(weapons)
    
    @staticmethod
    def difficulty() -> range:
        return range(1, 6)
    
    @staticmethod
    def weight() -> List[str]:
        return [
            "Light",
            "Slightly Heavy",
            "Heavy",
        ]

# Archipelago Options
class LiesofPIncludeWeaponObjectives(Toggle):
    """
    Indicates whether to include using random weapons when generating Lies of P Objectives.
    Recommended to only set to true if you have a save file with all weapons unlocked/upgraded.
    """

    display_name = "Lies of P Include Weapon Objectives"

class LiesofPIncludeDifficulties(Toggle):
    """
    Indicates whether to include objectives that require beating bosses on a random difficulty.
    Could be any difficulty from 1-5
    """

    display_name = "Lies of P Include Difficulties"