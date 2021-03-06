import os
import json
import folium
import pandas as pd
import collections


class MapReviews:

    def __init__(self, reviews_path='../.data/takeout-20190506T143207Z-001/Takeout/'):
        '''
        Initialise the MapReviews object.

        @params:
            reviews_path: string
                            Path to folder, where the mapreviews file is located.
        '''

        self.reviews_path = reviews_path
        self.nothing = None
        self.labelled_path = 'Maps/My labelled places/Labelled places.json'
        self.map_reviews_path = 'Maps (your places)/Reviews.json'
        self.geotag = {'labelled_places': [],
                       'reviewed_places': []}
        self.location_main_file = './something.json'

    def preprocess(self):
        '''
        Function to find the takeout files.

        @params:
            None
        '''
        # Preprocess the lablled places:
        with open(os.path.join(self.reviews_path, self.labelled_path)) as something:
            data = json.load(something)
            for something in data['features']:
                self.geotag['labelled_places'].append({
                    "marker_location": something['geometry']['coordinates'],
                    "address": something["properties"]["address"],
                    "marker_name": something["properties"]["name"],
                })

        with open(os.path.join(self.reviews_path, self.map_reviews_path)) as something:
            json_data = json.load(something)
            for data_points in json_data['features']:
                try:
                    comment = data_points["propoerties"]["Review Comment"]
                except:
                    comment = ""
                self.geotag['reviewed_places'].append({
                    "marker_location": data_points['geometry']['coordinates'],
                    "maps_url": data_points['properties']['Google Maps URL'],
                    "address": data_points["properties"]["Location"]["Address"],
                    "date": data_points['properties']['Published'],
                    "comment": comment,
                    "rating": data_points['properties']['Star Rating']
                })
        with open(self.location_main_file, 'w') as outfile:
            json.dump(self.geotag, outfile)

    def display(self):
        '''
        Function to display all the labelled places and reviewed places on a Leaflet Map using Folium

        @params:
            None
        '''
        xs = []
        ys = []
        values = []
        information = []
        with open(self.location_main_file) as something:
            json_data = json.load(something)
            # for labelled_places in json_data['labelled_places']:
            #     xs.append(labelled_places['marker_location'][0])
            #     ys.append(labelled_places['marker_location'][1])

            for reviews in json_data['reviewed_places']:
                xs.append(reviews['marker_location'][0])
                ys.append(reviews['marker_location'][1])
                information.append("Location: {} ---> Review: {}".format(reviews['address'], reviews['rating']))
                values.append(reviews['rating'])

        data = pd.DataFrame({'lat': xs, 'lon': ys, 'name': information, 'value': values})

        map = folium.Map(location=[20, 0], zoom_start=0)
        folium.TileLayer('cartodbdark_matter').add_to(map)
        fg = folium.FeatureGroup(name="Something")

        for lat, lon, name, value in zip(data['lat'], data['lon'], data['name'], data['value']):
            fg.add_child(folium.Marker(location=[lon, lat], popup=(folium.Popup(name)),
                         icon=folium.Icon(color='red', icon=self.ratings_icon(value))))
        map.add_child(fg)
        map.save(outfile='map.html')

    def ratings_icon(self, something):
        '''
        Function to help sort the .json according to the Ratings of the reviews.

        @params:
            something: int:
                The ratings value

        @returns:
            string:
                Icon name for the ratings (something) input.
        '''
        if something == 4 or something == 5:
            return 'cloud'
        elif something == 3 or something == 2:
            return 'amilia'
        else:
            return 'red'

    def build_coords(self, filename="../.data/takeout-20190506T143207Z-001/takeout/Location History/Location History.json"):
        '''
        Function to get your moving/locations statistics from google

        @params:
            None
        '''
        with open(filename) as something:
            json_data = json.load(something)
            print(pd.DataFrame(json_data).to_csv('./something.csv'))
