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

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
melon_list = make_melon_types(new_melons)


