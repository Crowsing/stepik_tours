from random import randint
import tours.data as data


def pars():
    result_tour = {}

    for i in range(6):
        tour_index = randint(1, 12)

        while tour_index in result_tour.keys():
            tour_index = randint(1, 12)

        picture = data.tours[tour_index]["picture"]
        title = data.tours[tour_index]["title"]
        description = data.tours[tour_index]["description"]

        result_tour[tour_index] = {
                    "picture": picture,
                    "title": title,
                    "description": description
                }

    return {
        "result_tour": result_tour
    }

