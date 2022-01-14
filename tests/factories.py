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


register(CategoryFactory)
