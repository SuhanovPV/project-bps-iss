from selene import browser, be, have


class SearchPage:

    def open(self):
        browser.open('/search/')
        return self

    def search_text(self, text):
        browser.element('.scan [name=q]').should(be.blank).type(text)
        browser.element('.scan [type="submit"]').click()
        return self

    def should_find_results_with_text(self, text):
        results = browser.all('.scan a').all('.scan-item__desc')
        for result in results:
            result.should(have.text(text))
        return self

    def should_not_found_results(self):
        browser.element('.scan__result') \
            .should(have.exact_text('К сожалению, на ваш поисковый запрос ничего не найдено.'))
        return self
