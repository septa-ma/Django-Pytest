import pytest
from core.app.models import Product

@pytest.mark.parametrize(
    "category, description, price, title, validity",
    [
        (1, 'new description', 8.88, 'newTitle',  True),
        (1, 'new description', 7.98, 'newTitle',  True),
    ],
)
def test_product_param(db, product_factory, title, description, price, category, validity):
   
   test = product_factory(
        category_id = category,
        description = description, 
        price = price, 
        title = title
    )
   item = Product.objects.all().count()
   print(item)
   assert item == validity