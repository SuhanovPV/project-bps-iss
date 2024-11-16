from selene import browser, have


class SolutionPage:
    def should_have_banner(self, value):
        browser.element("h1.service-banner__title").should(have.exact_text(value))
        return self

    def should_have_solutions(self, values: iter):
        browser.all(".platforms h3").should(have.exact_texts(values))
        return self
