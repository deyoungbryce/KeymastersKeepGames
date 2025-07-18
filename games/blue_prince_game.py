from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class BluePrinceArchipelagoOptions:
    blueprince_include_lategame_rooms: BluePrinceIncludeLateGameRooms

class BluePrinceGame(Game):
    name = "Blue Prince"
    platform = KeymastersKeepGamePlatforms.PC

    is_adult_only_or_unrated = False

    options_cls = BluePrinceArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
           GameObjectiveTemplate(
               label="Draft the ROOM",
               data={
                   "ROOM": (self.rooms, 1),
               },
               is_time_consuming=False,
               is_difficult=False,
               weight=3,
           ),
           GameObjectiveTemplate(
               label="Draft the following rooms in a single day: ROOMS",
               data={
                    "ROOMS": (self.rooms_multiple, 3),
               },
               is_time_consuming=True,
               is_difficult=False,
               weight=2,
           ),
           GameObjectiveTemplate(
               label="Complete a PUZZLE puzzle",
               data={
                   "PUZZLE": (self.puzzles, 1),
               },
               is_time_consuming=False,
               is_difficult=False,
               weight=3,
           ),
           GameObjectiveTemplate(
               label="Draft 5 TYPE rooms in a single day",
               data={
                   "TYPE": (self.room_types, 1),
               },
               is_time_consuming=True,
               is_difficult=False,
               weight=2,
           ),
           GameObjectiveTemplate(
               label="Collect the following items in a single day: ITEMS",
               data={
                   "ITEMS": (self.items, 2),
               },
               is_time_consuming=False,
               is_difficult=False,
               weight=2,
           ),
           GameObjectiveTemplate(
               label="Create the CONTRAPTION Contraption in the Workshop",
               data={
                   "CONTRAPTION": (self.contraptions, 1),
               },
               is_time_consuming=True,
               is_difficult=True,
               weight=2
           ),
        ]
    
    @property
    def include_lategame_rooms(self) -> bool:
        return bool(self.archipelago_options.blueprince_include_lategame_rooms.value)

    @functools.cached_property
    def base_rooms(self) -> List[str]:
        return [
            "Spare Room",
            "Rotunda",
            "Parlor",
            "Billiard Room",
            "Gallery",
            "Closet",
            "Walk-in Closet",
            "Attic",
            "Storeroom",
            "Nook",
            "Garage",
            "Music Room",
            "Locker Room",
            "Den",
            "Wine Cellar",
            "Trophy Room",
            "Ballroom",
            "Pantry",
            "Rumpus Room",
            "Vault",
            "Office",
            "Drawing Room",
            "Study",
            "Library",
            "Chamber of Mirrors",
            "The Pool",
            "Drafting Studio",
            "Utility Closet",
            "Boiler Room",
            "Pump Room",
            "Security",
            "Workshop",
            "Laboratory",
            "Sauna",
            "Coat Check",
            "Mail Room",
            "Freezer",
            "Dining Room",
            "Observatory",
            "Conference Room",
            "Aquarium",
            "Bedroom",
            "Boudoir",
            "Guest Bedroom",
            "Nursery",
            "Servant's Quarters",
            "Bunk Room",
            "Her Ladyship's Chambers",
            "Master Bedroom",
            "Hallway",
            "West Wing Hall",
            "East Wing Hall",
            "Corridor",
            "Passageway",
            "Secret Passage",
            "Foyer",
            "Great Hall",
            "Terrace",
            "Patio",
            "Courtyard",
            "Cloister",
            "Veranda",
            "Greenhouse",
            "Morning Room",
            "Secret Garden",
            "Commissary",
            "Kitchen",
            "Locksmith",
            "Showroom",
            "Laundry Room",
            "Bookshop",
            "Lavatory",
            "Chapel",
            "Maid's Chamber",
            "Archives",
            "Gymnasium",
            "Darkroom",
            "Weight Room",
            "Furnace",
        ]
    
    @functools.cached_property
    def late_game_rooms(self) -> List[str]:
        return [
            "Dovecote",
            "The Kennel",
            "Clock Tower",
            "Classroom",
            "Solarium",
            "Dormitory",
            "Vestibule",
            "Casino",
            "Mechanarium",
            "Treasure Trove",
            "Throne Room",
            "Tunnel",
            "Conservatory",
            "Lost and Found",
            "Closed Exhibit",
            "The Armory",
            "Mount Holly Gift Shop",
        ]
    
    @functools.cached_property
    def outside_rooms(self) -> List[str]:
        return [
            "Tool Shed",
            "Shelter",
            "Schoolhouse",
            "Shrine",
            "Root Cellar",
            "Hovel",
            "Trading Post",
            "Tomb",
        ]
    
    def rooms(self) -> List[str]:
        rooms: List[str] = self.base_rooms[:]

        rooms.extend(self.outside_rooms[:])

        if self.include_lategame_rooms:
            rooms.extend(self.late_game_rooms[:])

        return sorted(rooms)
    
    def rooms_multiple(self) -> List[str]:
        rooms: List[str] = self.base_rooms[:]

        if self.include_lategame_rooms:
            rooms.extend(self.late_game_rooms[:])

        return sorted(rooms)
    
    @staticmethod
    def puzzles() -> List[str]:
        return [
            "Parlor",
            "Billiard",
        ]

    @staticmethod
    def room_types() -> List[str]:
        return [
            "Bedroom",
            "Hallway",
            "Green",
            "Shop",
            "Red",
        ]

    @staticmethod
    def items() -> List[str]:
        return [
            "Battery Pack",
            "Broken Lever",
            "Car Keys",
            "Coin Purse",
            "Compass",
            "Coupon Book",
            "Keycard",
            "Lockpick",
            "Lucky Rabbit's Foot",
            "Magnifying Glass",
            "Metal Detector",
            "Running Shoes",
            "Salt Shaker",
            "Shovel",
            "Silver Key",
            "Sledgehammer",
            "Sleeping Mask",
            "Watering Can",
        ]
    
    @staticmethod
    def contraptions() -> List[str]:
        return [
            "Burning Glass",
            "Detector Shovel",
            "Dowsing Rod",
            "Electromagnet",
            "Jack Hammer",
            "Lucky Purse",
            "Pick Sound Amplifier",
            "Power Hammer",
        ]

# Archipelago Options
class BluePrinceIncludeLateGameRooms(Toggle):
    """
    Indicates whether to include lategame rooms when generating Blue Prince objectives.
    Includes: rooms added by Studio, rooms found while exploring the estate, and outdoor rooms.
    Recommended to only set to true if playing on a 100% save file.
    """

    display_name = "Blue Prince Include Lategame Rooms"