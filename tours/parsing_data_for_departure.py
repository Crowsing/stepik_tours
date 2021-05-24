import tours.data as data


def pars(departure):
    departure_ru = data.departures[departure]
    result_tours = []

    for tour in data.tours:
        if data.tours[tour]["departure"] == departure:
            tmp_result = data.tours[tour]
            tmp_result["index"] = tour
            result_tours.append(tmp_result)

    min_price = min([tour["price"] for tour in result_tours])
    max_price = max([tour["price"] for tour in result_tours])

    min_night = min([tour["nights"] for tour in result_tours])
    max_night = max([tour["nights"] for tour in result_tours])

    return {
        "number_of_tours": len(result_tours),
        "departure_ru": departure_ru,
        "tours": result_tours,
        "min_price": min_price,
        "max_price": max_price,
        "min_night": min_night,
        "max_night": max_night
    }
