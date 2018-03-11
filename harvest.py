############
# Part 1   #
############
new_melons = {
    "muskmelon": {
        "code": "musk",
        "first_harvest": 1998,
        "color": "green",
        "pairings": ["mint"],
        "is_seedless": True,
        "is_bestseller": True
    },
    "casaba": {
        "code": "cas",
        "first_harvest": 2003,
        "color": "orange",
        "pairings": ["strawberries", "mint"],
        "is_seedless": False,
        "is_bestseller": False
    },
    "crenshaw": {
        "code": "cren",
        "first_harvest": 1996,
        "color": "green",
        "pairings": ["proscuitto"],
        "is_seedless": False,
        "is_bestseller": False
    },
    "yellow watermelon": {
        "code": "yw",
        "first_harvest": 2013,
        "color": "yellow",
        "pairings": ["ice cream"],
        "is_seedless": False,
        "is_bestseller": True
    }
}

sellable_melons = {
    "melon1": {
        "melon_type": "yw",
        "shape_rating": 8,
        "color_rating": 7,
        "harvest_field": 2,
        "harvest_by": "Sheila"
    },
    "melon2": {
        "melon_type": "yw",
        "shape_rating": 3,
        "color_rating": 4,
        "harvest_field": 2,
        "harvest_by": "Sheila"
    },
    "melon3": {
        "melon_type": "yw",
        "shape_rating": 9,
        "color_rating": 8,
        "harvest_field": 3,
        "harvest_by": "Sheila"
    },
    "melon4": {
        "melon_type": "cas",
        "shape_rating": 10,
        "color_rating": 6,
        "harvest_field": 35,
        "harvest_by": "Sheila"
    },
    "melon5": {
        "melon_type": "cren",
        "shape_rating": 8,
        "color_rating": 9,
        "harvest_field": 35,
        "harvest_by": "Michael"
    },
    "melon6": {
        "melon_type": "cren",
        "shape_rating": 8,
        "color_rating": 2,
        "harvest_field": 35,
        "harvest_by": "Michael"
    },
    "melon7": {
        "melon_type": "cren",
        "shape_rating": 2,
        "color_rating": 3,
        "harvest_field": 4,
        "harvest_by": "Michael"
    },
    "melon8": {
        "melon_type": "musk",
        "shape_rating": 6,
        "color_rating": 7,
        "harvest_field": 4,
        "harvest_by": "Michael"
    },
    "melon9": {
        "melon_type": "yw",
        "shape_rating": 7,
        "color_rating": 10,
        "harvest_field": 3,
        "harvest_by": "Sheila"
    }
}


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name,pairing):
        """Initialize a melon."""
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = pairing


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types(new_melons):
    """Returns a list of current melon types."""

    all_melon_types = []

    for item in new_melons:
        melon = MelonType(new_melons[item]["code"],
            new_melons[item]["first_harvest"],new_melons[item]["color"],
            new_melons[item]["is_seedless"],
            new_melons[item]["is_bestseller"],item,
            new_melons[item]["pairings"])
        all_melon_types.append(melon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "{} pairs with".format(melon.name.title())
        for pairing in melon.pairings:
            print "- {}".format(pairing)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvest_field,
        harvest_by, name):
        """Initialize harvested melon attributes"""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvest_by = harvest_by
        self.is_sellable = None
        self.name = name

    def is_sellable(self):
        """ Check whether color rating & shape rating >5, did not come from field 3"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            self.is_sellable = True
        else:
            self.is_sellable = False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    sellable_list = []

    for item in melon_types:
            merchandise = Melon(sellable_melons[item]["melon_type"],
                                sellable_melons[item]["shape_rating"],
                                sellable_melons[item]["color_rating"],
                                sellable_melons[item]["harvest_field"],
                                sellable_melons[item]["harvest_by"],
                                item)
            sellable_list.append(merchandise)

    return sellable_list


def get_sellability_report():
    """Given a list of melon object, prints whether each one is sellable."""

    melon_list = make_melons(sellable_melons)

    print "Sellable Melons:"
    for item in melon_list:
        if item.is_sellable:
            print item.name
            print item.harvest_by
            print item.harvest_field
            print

    print "\n\nMelons That Are NOT Sellable:"
    for item in melon_list:
        if not item.is_sellable:
            print item.name
            print item.harvest_by
            print item.harvest_field
            print

# melon_list = make_melon_types(new_melons)
get_sellability_report()


