import pytest

pytestmark = pytest.mark.api


def test_listar_posts_devuelve_100(api):
    r = api.get("/posts")

    assert r.status_code == 200
    assert r.headers["Content-Type"].startswith("application/json")
    assert len(r.json()) == 100


def test_obtener_post_tiene_estructura_correcta(api):
    r = api.get("/posts/1")

    assert r.status_code == 200
    body = r.json()
    assert set(body.keys()) == {"userId", "id", "title", "body"}
    assert body["id"] == 1
    assert isinstance(body["title"], str)


def test_post_inexistente_devuelve_404(api):
    r = api.get("/posts/99999")

    assert r.status_code == 404


def test_filtrar_posts_por_usuario(api):
    r = api.get("/posts", params={"userId": 1})

    assert r.status_code == 200
    posts = r.json()
    assert len(posts) > 0
    assert all(p["userId"] == 1 for p in posts)


def test_crear_post(api):
    payload = {"title": "Mi post de prueba", "body": "Contenido", "userId": 1}

    r = api.post("/posts", json=payload)

    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


def test_actualizar_post(api):
    payload = {"id": 1, "title": "Título nuevo",
               "body": "Texto nuevo", "userId": 1}

    r = api.put("/posts/1", json=payload)

    assert r.status_code == 200
    assert r.json()["title"] == "Título nuevo"


def test_eliminar_post(api):
    r = api.delete("/posts/1")

    assert r.status_code == 200


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_comentarios_pertenecen_al_post(api, post_id):
    r = api.get(f"/posts/{post_id}/comments")

    assert r.status_code == 200
    comentarios = r.json()
    assert len(comentarios) > 0
    assert all(c["postId"] == post_id for c in comentarios)
