import tours.data as data


def get_departures(request):
    return {
        "departures": data.departures
    }


def get_title(request):
    return {
        "title": data.title
    }


def get_subtitle(request):
    return {
        "subtitle": data.subtitle
    }


def get_description(request):
    return {
        "description": data.description
    }
