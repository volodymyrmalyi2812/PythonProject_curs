import shelve

def add_link(service, short_link, full_link):
    with shelve.open(service.database_name) as links:
        links[short_link] = full_link

def find_link(service, short_link):
    with shelve.open(service.database_name) as links:
        if short_link in links:
            return links[short_link]

        return None