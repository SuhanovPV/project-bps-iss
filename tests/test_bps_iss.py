import allure

from project_bps_iss.data import Users
from project_bps_iss.pages.events_page import EventsPage
from project_bps_iss.pages.main_page import MainPage
from project_bps_iss.pages.search_page import SearchPage
from project_bps_iss.pages.solution_page import SolutionPage


@allure.title("Test open direction page via main menu")
@allure.severity(allure.severity_level.MINOR)
@allure.tag('Main page', 'Directions')
def test_open_direction_from_menu():
    main_page = MainPage()
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("choose direction page in menu"):
        main_page.open_direction('ekosistemy')

    solution_page = SolutionPage()
    with allure.step('Check title of open page'):
        solution_page.should_have_banner('ЭКОСИСТЕМЫ И ЦИФРОВАЯ\nТРАНСФОРМАЦИЯ')
    with allure.step('check content of open page'):
        solution_page.should_have_solutions([
            'МАРКЕТПЛЕЙС',
            'УМНЫЙ ГОРОД',
            'ЭЛЕКТРОННОЕ ГОСУДАРСТВО',
            'ЦИФРОВАЯ ЭКОСИСТЕМА СЕРВИСОВ / ИНТЕГРАЦИОННАЯ ПЛАТФОРМА / API'
        ])

@allure.title("Test success search article by keyword")
@allure.tag('Search')
@allure.severity(allure.severity_level.NORMAL)
def test_search_article_by_keyword_article_found():
    text = 'Эльбрус'
    search_page = SearchPage()
    with allure.step('Open search page'):
        search_page.open()
    with allure.step(f'Perform search by keyword {text}'):
        search_page.search_text(text)
    with allure.step(f'Check search results contain required text {text}'):
        search_page.should_find_results_with_text(text)

@allure.title("Test search by keyword returned no results")
@allure.tag('Search')
@allure.severity(allure.severity_level.MINOR)
def test_search_article_by_keyword_article_not_found():
    text = 'Кawabanga'
    search_page = SearchPage()
    with allure.step('Open search page'):
        search_page.open()
    with allure.step(f'Perform search by keyword {text}'):
        search_page.search_text(text)
    with allure.step(f'Check articles not found by keyword {text}'):
        search_page.should_not_found_results()

@allure.title("Test fill event registration form")
@allure.tag('Evetn page', 'registration form')
@allure.severity(allure.severity_level.BLOCKER)
def test_fill_event_registration_form():
    events_page = EventsPage()
    person = Users.test_person
    with allure.step('Open events page'):
        events_page.open()
    with allure.step('Open event registration form'):
        events_page.open_registration_form()
    with allure.step(f'Fill event registration form with data {person}'):
        events_page.fill_form(person)
    with allure.step('Close registration form'):
        events_page.close_form()

@allure.title("Test fill feedback form")
@allure.tag('Main page', 'feedback form')
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_feedback_form():
    person = Users.test_person
    message = "Create my tests"
    main_page = MainPage()
    with allure.step('Open page'):
        main_page.open()
    with allure.step('Go to feedback form'):
        main_page.scroll_to_contact_form()
    with allure.step(f'Fill feedback form'):
        main_page.fill_form(person, message)
