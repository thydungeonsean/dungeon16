from source.objects.map_objects.map_object import MapObject


class Actor(MapObject):

    def __init__(self, (x, y)):
        MapObject.__init__(self, (x, y))

