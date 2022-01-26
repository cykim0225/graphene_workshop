from schema.types import Property

abc_APT = Property(id="1234", name="ABC Apartment", address="123 Astor Court")

xyz_APT = Property(id="5678", name="XYZ Apartment", address="567 106th AVE")

property_data = {"1234": abc_APT, "5678": xyz_APT}


def get_property_by_id(id):
    return property_data.get(str(id))
