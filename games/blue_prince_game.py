from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms



class BluePrinceGame(Game):
    name = "Blue Prince"
    platform = KeymastersKeepGamePlatforms.PC

    is_adult_only_or_unrated = False

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
           
        ]

    @staticmethod
    def rooms() -> List[str]:
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
            "The Armory",
            "Mount Holly Gift Shop",
            "Lavatory",
            "Chapel",
            "Maid's Chamber",
            "Archives",
            "Gymnasium",
            "Darkroom",
            "Weight Room",
            "Furnace",
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
            "Tool Shed",
            "Shelter",
            "Schoolhouse",
            "Shrine",
            "Root Cellar",
            "Hovel",
            "Trading Post",
            "Tomb"
        ]
    
    @staticmethod
    def secrets() -> List[str]:
        return [
            ""
        ]

# Archipelago Options