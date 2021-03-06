class Mapping(dict):
    def __getitem__(self, item):
        try:
            return super(Mapping, self).__getitem__(item)
        except KeyError:
            self[item] = []
            return self[item]
