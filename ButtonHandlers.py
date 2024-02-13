from InterestingPlacesButtons import ParksButton, MuseumsButton
from MainMenuButtons import *
from SportButtons import SectionsButton
from sections_buttons.badminton import BadmintonButton
from sections_buttons.beach_volleyball import BeachVolleyballButton


class ButtonHandlers:
    def __init__(self):
        self.handlers = {
            #Основное меню
            '1': AboutUsButton(),
            '2': InterestingPlacesButton(),
            '3': SportsButton(),
            '4': ShopsButton(),
            '5': SuggestionButton(),
            '6': TransportButton(),
            '7': StoriesButton(),

            'parks': ParksButton(),
            'museums': MuseumsButton(),

            'sections': SectionsButton(),

            'badminton': BadmintonButton(),
            'beach_volleyball': BeachVolleyballButton(),

            #Кнопки возврата
            'back_to_sport': SportsButton(),
            'back_to_sections': SectionsButton(),
            'back_to_interesting_places': InterestingPlacesButton()
        }

    def get_handler(self, key):
        return self.handlers.get(key, None)

    def has_handler(self, key):
        return key in self.handlers

    def get_internal_handler(self, parent_key, child_key):
        parent_handler = self.get_handler(parent_key)
        if parent_handler and hasattr(parent_handler, 'internal_handlers'):
            return parent_handler.internal_handlers.get(child_key, None)
        return None
