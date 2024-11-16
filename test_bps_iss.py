from selene import browser, have, command, be


def test_open_direction_from_menu():
    browser.open('/')
    browser.all("nav .nav__item > a").element_by(have.exact_text("НАПРАВЛЕНИЯ")).click()
    browser.element('[href="/direction/ekosistemy-i-tsifrovaya-transformatsiya/"]').click()
    browser.element("h1.service-banner__title").should(have.exact_text('ЭКОСИСТЕМЫ И ЦИФРОВАЯ\nТРАНСФОРМАЦИЯ'))
    browser.all(".platforms h3").should(have.exact_texts(
        'МАРКЕТПЛЕЙС',
        'УМНЫЙ ГОРОД',
        'ЭЛЕКТРОННОЕ ГОСУДАРСТВО',
        'ЦИФРОВАЯ ЭКОСИСТЕМА СЕРВИСОВ / ИНТЕГРАЦИОННАЯ ПЛАТФОРМА / API'
    ))

def test_search_article_by_keyword_article_found():
    browser.open('/search/')
    browser.element('.scan [name=q]').should(be.blank).type('Эльбрус')
    browser.element('.scan [type="submit"]').click()
    results = browser.all('.scan a').all('.scan-item__desc')
    for result in results:
        result.should(have.text('Эльбрус'))

def test_search_article_by_keyword_article_not_found():
    browser.open('/search/')
    browser.element('.scan [name=q]').should(be.blank).type('Кawabanga')
    browser.element('.scan [type="submit"]').click()
    browser.element('.scan__result').should(have.exact_text('К сожалению, на ваш поисковый запрос ничего не найдено.'))


def test_fill_event_registration_form():
    browser.open('/events/')
    browser.element('.banner__btn[data-event=openForm]').click()
    browser.element('[data-event="sendForm"]').element('[name=name]').should(be.blank).type('Павел Викторович Суханов')
    browser.element('[data-event="sendForm"]').element('[name=company]').should(be.blank).type('MyCompany')
    browser.element('[data-event="sendForm"]').element('[name=email]').should(be.blank).type('pavel@mail.ru')
    browser.element('[data-event="sendForm"]').element('[name=industry]').click()
    browser.element('[data-event="sendForm"]').element('[name=industry]').perform(command.js.set_value('Энергетика'))
    browser.element('[data-event="sendForm"]').element('[name=tel]').should(be.blank).type('+790999999999')
    browser.element('[data-event="sendForm"]').element('[name=count]').perform(command.js.set_value('101-500'))
    browser.element('[data-event="sendForm"]').element('[name=city]').should(be.blank).type('Санкт-Петербург')
    browser.element('[data-event="sendForm"]').element('[name=job]').should(be.blank).type('qa engineer')
    browser.element('[data-event="sendForm"]').element('[name=goal]').should(be.blank).\
        type('Выполнить тестовое задание\nдля сдачи домашней работы в qa guru')
    browser.element('[data-event="sendForm"]').element('[name=corpEmail]').should(be.blank).type('mycompany@mail.ru')
    browser.element('[data-event="sendForm"]').element('[name=site]').should(be.blank).type('mycompany.ru')
    browser.element('[data-event="sendForm"]').element('[data-event=closeForm]').click()

def test_fill_request_form():
    browser.open('/')
    browser.element('form.form').perform(command.js.scroll_into_view)
    browser.element('[name=name]').should(be.blank).type('Павел')
    browser.element('[name=company]').should(be.blank).type('MyCompany')
    browser.element('[name=tel]').should(be.blank).type('+790999999999')
    browser.element('[name=email]').should(be.blank).type('pavel@mail.ru')
    browser.element('[name=msg]').should(be.blank).type('делаю демо')
    browser.element('[href="/person/"]').element('..').click()


