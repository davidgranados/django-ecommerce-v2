import pytest
from inventory import models


@pytest.mark.db_fixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_db_fixture(db, db_fixture_setup, id, name, slug, is_active):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "is_active",
    [
        (1),
        (1),
        (1),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, is_active):
    result = category_factory.create(is_active=is_active)
    assert result.is_active == is_active
