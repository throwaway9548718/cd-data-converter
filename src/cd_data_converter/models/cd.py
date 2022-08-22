from decimal import Decimal, InvalidOperation
from functools import cached_property
from typing import Any, List, Optional

from pydantic import BaseModel, Field
from pydantic.utils import GetterDict

VAT_FRACTION = Decimal("0.25")


class CDXMLGetter(GetterDict):
    @cached_property
    def _split_name(self) -> List[str]:
        return self._obj.find("ARTIST").text.rsplit(" ", 1)

    def performer_firstname(self, *_) -> str:
        return self._split_name[0]

    def performer_lastname(self, *_) -> str:
        try:
            return self._split_name[1]
        except IndexError:
            return self._split_name[0]

    @cached_property
    def _price(self) -> Decimal:
        try:
            return Decimal(self._obj.find("PRICE").text)
        except InvalidOperation as e:
            raise ValueError(e)

    def price_no_vat(self, *_) -> Decimal:
        return self._price - (self._price * VAT_FRACTION)

    def vat(self, *_) -> Decimal:
        return self._price * VAT_FRACTION

    def default(self, key: str, default: Optional[Any] = ...) -> Any:
        try:
            return self._obj.find(key).text
        except (AttributeError, KeyError):
            return default

    def get(self, key: str, default: Optional[Any] = ...) -> Any:
        return getattr(self, key, self.default)(key, default)


class CD(BaseModel):
    title: str = Field(alias="TITLE")
    performer_lastname: str
    performer_firstname: str
    origin: str = Field(alias="COUNTRY")
    published: int = Field(alias="YEAR")
    price_no_vat: float
    vat: float
    tot: float = Field(alias="PRICE")

    class Config:
        orm_mode = True
        getter_dict = CDXMLGetter
