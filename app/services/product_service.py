from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.product_pricing import ProductPricing
from app.models.product_attributes import ProductAttributes
from app.models.attribute_value import AttributeValue
from app.schemas.product_schema import ProductCreate
import app.repositories.product_repository as ProductRepository
import app.repositories.product_pricing_repository as ProductPricingRepository
import app.repositories.attribute_values_repository as AttributeValuesRepository
import app.repositories.product_attributes_repository as ProductAttributesRepository
import app.repositories.attribute_repository as AttributesRepository


def create_product(db: Session, product_data: ProductCreate):
    # Create the product
    product = ProductRepository.create_product(db, product=Product(
        name=product_data.name,
        description=product_data.description,
        sku=product_data.sku
    ))

    # Create related product pricings
    for pricing_data in product_data.pricings:
        ProductPricingRepository.create_product_pricing(
            db=db,
            product_pricing=ProductPricing(
                product_id=product.id,
                rental_period_id=pricing_data.rental_period_id,
                region_id=pricing_data.region_id,
                price=pricing_data.price
            )
        )

    # Create related product attributes and attribute values
    for attribute_data in product_data.attributes:
        attribute_value = AttributeValuesRepository.create_attribute_value(
            db=db,
            attribute_value=AttributeValue(
                attribute_id=attribute_data.attribute_id,
                value=attribute_data.value
            )
        )
        ProductAttributesRepository.create_product_attribute(
            db=db,
            product_attribute=ProductAttributes(
                product_id=product.id,
                attribute_value_id=attribute_value.id
            )
        )

    return product
