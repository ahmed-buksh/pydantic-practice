class Location:
    def __init__(self, data):
        self.city_name = data[0]
        self.city_lng = [data[1]]
        self.city_lat = [data[2]]


def playground():
    sample_location = ('New York, NY', '-73.98647', '40.756679999999996')
    location = Location(sample_location)
    print(location.city_name)
    print(location.city_lng)
    print(location.city_lat)


if __name__ == '__main__':
    playground()
