import tours.data as data


def pars(tour_id: int):
    stars = ''
    i = 0
    while i < int(data.tours[tour_id]['stars']):
        stars += '★'
        i += 1
    return {
        "stars": stars,
        "data": data.tours[tour_id],
        "departure_ru": data.departures[data.tours[tour_id]["departure"]]
    }

