from app.services.entries import FieldEnum, House, Number


class FieldGetter:
    def __init__(self, field: FieldEnum):
        self.field = field

    def get(self, house: House) -> Number:
        if self.field == FieldEnum.YEAR:
            return house.year
        if self.field == FieldEnum.PRICE:
            return house.price
        if self.field == FieldEnum.APARTMENTS:
            return house.apartments
