from Point import Point


def get_user_input():
    ins = input('Insert lat+lng (lat;lng)')

    vals = ins.strip().split(';')
    if len(vals) != 2:
        raise Exception('Wrong input', ins)

    return Point(float(vals[0]), float(vals[1]))


def find_closest_city(point: Point):
    with open('it.csv', 'r') as cities:

        cities.readline()

        closest_name = ''
        closest_distance = ''
        is_first = True


        for line in cities:
            (city,
             lat,
             lng,
             country,
             iso2,
             admin_name,
             capital,
             population,
             population_proper
             ) = line.strip().split(',')

            # print('Evaluating', city, lat, lng)

            if is_first:
                closest_name = city
                closest_distance = point\
                    .distance_from(Point(float(lat), float(lng)))
                is_first = False

            else:
                curr_dist = point.distance_from(Point(float(lat), float(lng)))
                if curr_dist < closest_distance:
                    closest_distance = curr_dist
                    closest_name = city


        return closest_name





def main():
    # 45.092125 8.0465709

    valid = False
    while not valid:
        try:
            p = get_user_input()
            valid = True
        except Exception as e:
            print('Error', e)

    city = find_closest_city(p)

    print(city)


main()
