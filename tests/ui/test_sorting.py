import pytest
pytestmark = pytest.mark.ui

@pytest.mark.parametrize(
    "opcion, reverso",
    [("lohi", False), ("hilo", True)],
)
def test_ordenar_por_precio(inventory_page, opcion, reverso):
    inventory_page.sort_by(opcion)
    precios = inventory_page.get_prices()
    assert precios == sorted(precios, reverse=reverso)


@pytest.mark.parametrize(
    "opcion, reverso",
    [("az", False), ("za", True)],
)
def test_ordenar_por_nombre(inventory_page, opcion, reverso):
    inventory_page.sort_by(opcion)
    nombres = inventory_page.get_names()
    assert nombres == sorted(nombres, reverse=reverso)