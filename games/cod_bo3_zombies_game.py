from __future__ import annotations

import functools
from typing import List, Set, Dict, NamedTuple

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class BO3ZombiesArchipelagoOptions:
    bo3zombies_maps: BO3ZombiesMaps
    bo3zombies_custom_maps: BO3ZombiesCustomMaps

class MapData(NamedTuple):
    weapons: str
    wonder_weapons: str

dlc_content: Dict[str, MapData] = {
    "Shadows of Evil": MapData({"Bloodhound"}, {"Apothicon Servant"}),
    "The Giant": MapData({}, {}),
    "Der Eisendrache": MapData({}, {}),
    "Zetsubou No Shima": MapData({}, {}),
    "Gorod Krovi": MapData({}, {}),
    "Revelations": MapData({}, {}),
    "Nacht der Untoten": MapData({}, {}),
    "Verruckt": MapData({}, {}),
    "Shi No Numa": MapData({}, {}),
    "Kino der Toten": MapData({}, {}),
    "Ascension": MapData({}, {}),
    "Shangri-La": MapData({}, {}),
    "Moon": MapData({}, {}),
    "Origins": MapData({}, {}),
}

class BO3ZombiesGame(Game):
    name = "Call of Duty: Black Ops 3 Zombies"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS3,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.X360,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = True

    options_cls = BO3ZombiesArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Reach round ROUND on MAP",
                data={
                    "ROUND": (self.round_count, 1),
                    "MAP": (self.maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Pack-a-Punch the WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Acquire the WONDER",
                data={
                    "WONDER": (self.wonder_weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]

    def maps(self) -> List[str]:
        maps: List[str] = self.archipelago_options.bo3zombiesmaps.value
        maps.extend(self.archipelago_options.bo3zombiescustommaps.value)

        return sorted(maps)
    
    
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Bloodhound",
            "RK5",
            "L-CAR",
            "MR6",
            "Marshal 16 Dual Wield",
            "Rift E9",
            "Mauser C96",
            "1911",
            "Kuda",
            "VMP",
            "Weevil",
            "Vesper",
            "Pharo",
            "Bootlegger",
            "Razorback",
            "HG 40",
            "PPSh-41",
            "MP40",
            "AK-74u",
            "KN-44",
            "HVK-30",
            "ICR-1",
            "Man-O-War",
            "Sheiva",
            "M8A7",
            "MX Garand",
            "M14",
            "FFAR",
            "Peacekeeper MK2",
            "M16",
            "Galil",
            "StG-44",
            "BRM",
            "Dingo",
            "Gorgon",
            "48 Dredge",
            "RPK",
            "MG-08",
            "Drakon",
            "Locus",
            "SVG-100",
            "KRM-262",
            "205 Brecci",
            "Haymaker 12",
            "Argus",
            "Banshii",
            "XM-53",
            "L4 Siege",
            "NX ShadowClaw Dual Wield",
        ]
    
    @staticmethod
    def wonder_weapons() -> List[str]:
        return [
            "Ray Gun",
            "Apothicon Servant",
            "Wunderwaffe DG-2",
            "Wrath of the Ancients",
            "KT-4",
            "GKZ-45 Mk3",
            "Thundergun",
            "Ray Gun Mark II",
            "31-79 JGb215",
            "Wave Gun",
            "Staff of Ice",
            "Staff of Fire",
            "Staff of Wind",
            "Staff of Lightning",
        ]
    
    @staticmethod
    def perks() -> List[str]:
        return [
            "Quick Revive",
            "Speed Cola",
            "Stamin-Up",
            "Double Tap Root Beer",
            "Deadshot Daiquiri",
            "Mule Kick",
            "Juggernog",
            "Electric Cherry",
            "Widow's Wine"
        ]
    
    @staticmethod
    def round_count() -> range:
        return range(10, 21)

# Archipelago Options
class BO3ZombiesMaps(OptionSet):
    """
    Indicates which zombies maps should be included when generating Black Ops 3 Zombies objectives.
    """

    display_name = "Black Ops 3 Zombies Maps"
    valid_keys = [
        "Shadows of Evil",
        "The Giant",
        "Der Eisendrache",
        "Zetsubou No Shima",
        "Gorod Krovi",
        "Revelations",
        "Nacht der Untoten",
        "Verruckt",
        "Shi No Numa",
        "Kino der Toten",
        "Ascension",
        "Shangri-La",
        "Moon",
        "Origins",
    ]

    default = valid_keys

class BO3ZombiesCustomMaps(OptionSet):
    """
    Indicates which Custom Zombies Maps should be considered when generating Black Ops 3 Zombies objectives.
    Adding custom maps that don't follow the general structure of an official map could lead to impossible objectives.
    """

    display_name = "Black Ops 3 Zombies Custom Maps"

    default = list()