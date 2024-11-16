from selene import browser, be, command
from project_bps_iss.data.Users import User


class EventsPage:
    def open(self):
        browser.open('/events/')
        return self

    def open_registration_form(self):
        browser.element('.banner__btn[data-event=openForm]').click()
        return self

    def fill_form(self, user: User):
        self.fill_name(user.name) \
            .fill_company(user.company) \
            .fill_email(user.email) \
            .choose_industry(user.industry) \
            .fill_phone(user.phone) \
            .set_personal_amount(user.personal_count) \
            .fill_city(user.city) \
            .fill_job(user.job) \
            .fill_goal(user.goal) \
            .fill_corp_email(user.corp_email) \
            .fill_corp_site(user.corp_site)

    def fill_name(self, value):
        browser.element('[data-event="sendForm"]').element('[name=name]').should(be.blank).type(value)
        return self

    def fill_company(self, value):
        browser.element('[data-event="sendForm"]').element('[name=company]').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('[data-event="sendForm"]').element('[name=email]').should(be.blank).type(value)
        return self

    def choose_industry(self, value):
        browser.element('[data-event="sendForm"]').element('[name=industry]').click()
        browser.element('[data-event="sendForm"]').element('[name=industry]').perform(
            command.js.set_value(value))
        return self

    def fill_phone(self, value):
        browser.element('[data-event="sendForm"]').element('[name=tel]').should(be.blank).type(value)
        return self

    def set_personal_amount(self, value):
        browser.element('[data-event="sendForm"]').element('[name=count]').perform(command.js.set_value('101-500'))
        return self

    def fill_city(self, value):
        browser.element('[data-event="sendForm"]').element('[name=city]').should(be.blank).type(value)
        return self

    def fill_job(self, value):
        browser.element('[data-event="sendForm"]').element('[name=job]').should(be.blank).type(value)
        return self

    def fill_goal(self, value):
        browser.element('[data-event="sendForm"]').element('[name=goal]').should(be.blank).type(value)
        return self

    def fill_corp_email(self, value):
        browser.element('[data-event="sendForm"]').element('[name=corpEmail]').should(be.blank).type(value)
        return self

    def fill_corp_site(self, value):
        browser.element('[data-event="sendForm"]').element('[name=site]').should(be.blank).type(value)
        return self

    def close_form(self):
        browser.element('[data-event="sendForm"]').element('[data-event=closeForm]').click()
        return self
