import factory
from faker import Faker
from inventory import models
from pytest_factoryboy import register

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "cat_name_%d" % n)
    # slug = fake.lexify(text="cat-slug-??????")
    slug = factory.Sequence(lambda n: "cat-slug-%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug = factory.Sequence(lambda n: "prod-slug-%d" % n)
    name = factory.Sequence(lambda n: "product name %d" % n)
    description = fake.text()
    is_active = True
    created_at = fake.date_this_month()
    updated_at = fake.date_this_month()

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


register(CategoryFactory)
register(ProductFactory)
