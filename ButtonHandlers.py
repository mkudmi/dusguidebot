from buttons.main_menu.InterestingPlaces.InterestingPlacesButtons import ParksButton, MuseumsButton, RestaurantsButton
from buttons.main_menu.MainMenuButtons import *
from buttons.main_menu.Sports.SportButtons import SectionsButton
from buttons.main_menu.InterestingPlaces.Restaurants.Restaurants import JenkaButton
from buttons.main_menu.Sports.Sections.badminton import BadmintonButton
from buttons.main_menu.Sports.Sections.beach_volleyball import BeachVolleyballButton


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

            #Интересные места
            'parks': ParksButton(),
            'museums': MuseumsButton(),
            'restaurants': RestaurantsButton(),

            #Рестораны
            'jenka': JenkaButton(),

            #Спорт
            'sections': SectionsButton(),

            #Секции
            'badminton': BadmintonButton(),
            'beach_volleyball': BeachVolleyballButton(),

            #Кнопки возврата
            'back_to_sport': SportsButton(),
            'back_to_sections': SectionsButton(),
            'back_to_interesting_places': InterestingPlacesButton(),
            'back_to_restaurants': RestaurantsButton()
        }

    def get_handler(self, key):
        return self.handlers.get(key, None)

    def has_handler(self, key):
        return key in self.handlers
