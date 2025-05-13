from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class TerrariaArchipelagoOptions:
    terraria_include_calamity: TerrariaIncludeCalamity
    terraria_include_hidden_bosses: TerrariaIncludeHiddenBosses


class TerrariaGame(Game):
    name = "Terraria"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = TerrariaArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat one of the following Bosses: BOSS",
                data={
                    "BOSS": (self.bosses, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Defeat one of the following Bosses with a CLASS Weapon: BOSS",
                data={
                    "BOSS": (self.bosses, 2),
                    "CLASS": (self.weapon_classes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Have the NPC move in",
                data={
                    "NPC": (self.npcs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
        ]
    
    @property
    def include_calamity(self) -> bool:
        return bool(self.archipelago_options.terraria_include_calamity.value)
    
    @property
    def include_hidden_bosses(self) -> bool:
        return bool(self.archipelago_options.terraria_include_hidden_bosses.value)

    @functools.cached_property
    def base_bosses(self) -> List[str]:
        return [
            "King Slime",
            "Eye of Cthulhu",
            "Eater of Worlds",
            "Brain of Cthulhu",
            "Queen Bee",
            "Deerclops",
            "Skeletron",
            "Wall of Flesh",
            "Queen Slime",
            "The Twins",
            "The Destroyer",
            "Skeletron Prime",
            "Plantera",
            "Golem",
            "Duke Fishron",
            "Empress of Light",
            "Lunatic Cultist",
            "Moon Lord",
            "Dark Mage",
            "Ogre",
            "Betsy",
            "Flying Dutchman",
            "Mourning Wood",
            "Pumpking",
            "Everscream",
            "Santa-NK1",
            "Ice Queen",
            "Martian Saucer",
            "The Celestial Pillars",
        ]
    
    @functools.cached_property
    def calamity_bosses(self) -> List[str]:
        return [
            "Desert Scourge",
            "Crabulon",
            "The Hive Mind",
            "The Perforators",
            "The Slime God",
            "Cryogen",
            "Aquatic Scourge",
            "Brimstone Elemental",
            "Calamitas Clone",
            "Leviathan and Anahita",
            "Astrum Aureus",
            "The Plaguebringer Goliath",
            "Ravager",
            "Astrum Deus",
            "Profaned Guardians",
            "Dragonfolly",
            "Providence, The Profaned Goddess",
            "Storm Weaver",
            "Ceaseless Void",
            "Signus, Envoy of The Devourer",
            "Polterghast",
            "The Old Duke",
            "The Devourer of Gods",
            "Yharon, Dragon of Rebirth",
            "Exo Mechs",
            "Supreme Witch, Calamitas",
            "Giant Clam",
            "Cragmaw Mire",
            "Great Sand Shark",
            "Mauler",
            "Nuclear Terror",
        ]
    
    @functools.cached_property
    def hidden_bosses(self) -> List[str]:
        return [
            "Primordial Wyrm",
            "XB-∞ Hekate",
            "Supreme Alchemist, Cirrus",
            "THE LORDE",
        ]
    
    def bosses(self) -> List[str]:
        bosses: List[str] = self.base_bosses[:]

        if self.include_calamity:
            bosses.extend(self.calamity_bosses[:])
            if self.include_hidden_bosses:
                bosses.extend(self.hidden_bosses[:])

        return sorted(bosses)
    
    @functools.cached_property
    def base_weapon_classes(self) -> List[str]:
        return [
            "Melee",
            "Ranged",
            "Magic",
            "Summoning",
        ]
    
    @functools.cached_property
    def calamity_weapon_classes(self) -> List[str]:
        return [
            "True Melee",
            "Rogue",
        ]
    
    def weapon_classes(self) -> List[str]:
        weapon_classes: List[str] = self.base_weapon_classes[:]

        if self.include_calamity:
            weapon_classes.extend(self.calamity_weapon_classes[:])

        return sorted(weapon_classes)
    
    @functools.cached_property
    def base_npcs(self) -> List[str]:
        return [
            "Merchant",
            "Nurse",
            "Demolitionist",
            "Dye Trader",
            "Angler",
            "Zoologist",
            "Dryad",
            "Painter",
            "Golfer",
            "Arms Dealer",
            "Tavernkeep",
            "Stylist",
            "Goblin Tinkerer",
            "Witch Doctor",
            "Clothier",
            "Mechanic",
            "Party Girl",
            "Wizard",
            "Tax Collector",
            "Truffle",
            "Pirate",
            "Steampunker",
            "Cyborg",
            "Princess",
            "Nerdy Slime",
            "Cool Slime",
            "Elder Slime",
            "Clumsy Slime",
            "Diva Slime",
            "Surly Slime",
            "Mystic Slime",
            "Squire Slime",
        ]
    
    @functools.cached_property
    def calamity_npcs(self) -> List[str]:
        return [
            "Sea King",
            "Bandit",
            "Drunk Princess",
            "Archmage",
            "Brimstone Witch",
        ]
    
    def npcs(self) -> List[str]:
        npcs: List[str] = self.base_npcs[:]

        if self.include_calamity:
            npcs.extend(self.calamity_npcs[:])

        return sorted(npcs)

# Archipelago Options
class TerrariaIncludeCalamity(Toggle):
    """
    Indicates whether to include the Terraria Calamity mod when generating Terraria objectives.
    """

    display_name = "Terraria Include Calamity"

class TerrariaIncludeHiddenBosses(Toggle):
    """
    Indicates whether to include Hidden Bosses when generating Terraria objectives.
    Only works if Include Calamity is set to True.
    """

    diplay_name = "Terraria Include Hidden Bosses"