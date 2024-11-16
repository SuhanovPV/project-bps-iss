from project_bps_iss.data import Users

from project_bps_iss.pages.events_page import EventsPage
from project_bps_iss.pages.main_page import MainPage
from project_bps_iss.pages.search_page import SearchPage
from project_bps_iss.pages.solution_page import SolutionPage


def test_open_direction_from_menu():
    main_page = MainPage()
    main_page.open()
    main_page.open_direction('ekosistemy')

    solution_page = SolutionPage()
    solution_page.should_have_banner('ЭКОСИСТЕМЫ И ЦИФРОВАЯ\nТРАНСФОРМАЦИЯ')
    solution_page.should_have_solutions([
        'МАРКЕТПЛЕЙС',
        'УМНЫЙ ГОРОД',
        'ЭЛЕКТРОННОЕ ГОСУДАРСТВО',
        'ЦИФРОВАЯ ЭКОСИСТЕМА СЕРВИСОВ / ИНТЕГРАЦИОННАЯ ПЛАТФОРМА / API'
    ])


def test_search_article_by_keyword_article_found():
    text = 'Эльбрус'
    search_page = SearchPage()
    search_page.open()
    search_page.search_text(text)

    search_page.should_find_results_with_text(text)


def test_search_article_by_keyword_article_not_found():
    text = 'Кawabanga'
    search_page = SearchPage()
    search_page.open()
    search_page.search_text(text)

    search_page.should_not_found_results()


def test_fill_event_registration_form():
    events_page = EventsPage()
    events_page.open()
    events_page.open_registration_form()
    events_page.fill_form(Users.test_person)
    events_page.close_form()

def test_fill_request_form():
    main_page = MainPage()
    main_page.open()
    main_page.scroll_to_contact_form()
    main_page.fill_form(Users.test_person, "Create my tests")
