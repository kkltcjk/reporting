from handlers import landing

mappings = [
    (r"/landing-page/filters", landing.FiltersHandler),
    (r"/landing-page/scenarios", landing.ScenariosHandler)
]
