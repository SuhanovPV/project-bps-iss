from selene import browser, have, command, be

from project_bps_iss.data.Users import User


class MainPage:
    def open(self):
        browser.open('/')
        return self

    def open_direction(self, value):
        browser.all("nav .nav__item > a").element_by(have.exact_text("НАПРАВЛЕНИЯ")).click()
        browser.element(f'[href^="/direction/{value}"]').click()
        return self

    def scroll_to_contact_form(self):
        browser.element('form.form').perform(command.js.scroll_into_view)
        return self

    def fill_form(self, user:User, massage:str):
        self.fill_name(user.name) \
        .fill_company(user.company) \
        .fill_phone(user.phone) \
        .fill_email(user.email) \
        .fill_message(massage) \
        .set_checkbox_accept_terms()
        return self

    def fill_name(self, value):
        browser.element('[name=name]').should(be.blank).type(value)
        return self

    def fill_company(self, value):
        browser.element('[name=company]').should(be.blank).type(value)
        return self

    def fill_phone(self, value):
        browser.element('[name=tel]').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('[name=email]').should(be.blank).type(value)
        return self

    def fill_message(self, value):
        browser.element('[name=msg]').should(be.blank).type(value)
        return self

    def set_checkbox_accept_terms(self):
        browser.element('[href="/person/"]').element('..').click()
        return self