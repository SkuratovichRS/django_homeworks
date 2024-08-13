import pytest

from tests.conftest import client, course_factory
from students.models import Course


@pytest.mark.django_db
def test_first_course_retrieve(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get(f"/api/v1/courses/{courses[0].id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == courses[0].id
    assert data["name"] == courses[0].name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    for i, course in enumerate(data):
        assert course["id"] == courses[i].id
        assert course["name"] == courses[i].name


@pytest.mark.django_db
def test_list_courses_filter_id(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get("/api/v1/courses/", data={"id": courses[2].id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["id"] == courses[2].id
    assert data[0]["name"] == courses[2].name


@pytest.mark.django_db
def test_list_courses_filter_name(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get("/api/v1/courses/", data={"name": courses[3].name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["id"] == courses[3].id
    assert data[0]["name"] == courses[3].name


@pytest.mark.django_db
def test_create_course(client):
    response = client.post("/api/v1/courses/", data={"name": "test_course"})
    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert Course.objects.all()[0].name == "test_course"


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=5)
    course_id = courses[1].id
    response = client.put(f"/api/v1/courses/{course_id}/", data={"name": "changed_name"})
    assert response.status_code == 200
    assert Course.objects.all().filter(id=course_id)[0].name == "changed_name"


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=5)
    count = Course.objects.count()
    course_id = courses[2].id
    response = client.delete(f"/api/v1/courses/{course_id}/")
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    assert course_id not in Course.objects.all().filter(id=course_id)
