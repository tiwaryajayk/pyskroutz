from typing import List

from pydantic import BaseModel, HttpUrl

from .base import ItemBase, WebUriBaseItem


class PaymentMethodsItem(BaseModel):
    credit_card: bool
    paypal: bool
    bank: bool
    spot_cash: bool
    installments: str


class ShippingItem(BaseModel):
    free: bool
    free_from: int
    free_from_info: str
    min_price: str
    shipping_cost_enabled: bool


class ExtraInfoItem(BaseModel):
    time_on_platform: str
    orders_per_week: str


class ShopItem(ItemBase, WebUriBaseItem):
    link: HttpUrl
    phone: str
    image_url: HttpUrl
    thumbshot_url: HttpUrl
    reviews_count: int
    latest_reviews_count: int
    review_score: float
    payment_methods: PaymentMethodsItem
    shipping: ShippingItem
    extra_info: ExtraInfoItem
    top_positive_reasons: List[str]