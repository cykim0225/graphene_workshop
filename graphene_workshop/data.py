from schema.types import Unit, Property

unit_101 = Unit(id="101", squareFeet=700, bedrooms=1, amenity=["RESERVED_PARKING"])

unit_102 = Unit(
    id="102", squareFeet=1000, bedrooms=2, amenity=["RESERVED_PARKING", "EV_PARKING"]
)

unit_203 = Unit(id="103", squareFeet=1500, bedrooms=3)

abc_APT = Property(
    id="1234",
    name="ABC Apartment",
    address="123 Astor Court",
    units=[unit_101, unit_102],
)

xyz_APT = Property(
    id="5678", name="XYZ Apartment", address="567 106th AVE", units=[unit_203]
)

unit_data = {"101": unit_101, "102": unit_102, "203": unit_203}

property_data = {"1234": abc_APT, "5678": xyz_APT}


def get_unit_by_id(id):
    return unit_data.get(str(id))


def get_property_by_id(id):
    return property_data.get(str(id))
