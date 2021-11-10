import json

import pytest
from wagtail_typograf import __version__

from django.test import RequestFactory
from django.conf import settings


@pytest.fixture
def django_settings():
    settings.configure(
        WAGTAIL_TYPOGRAF="wagtail_typograf.handlers.Typograf",
    )

    return settings


def test_version():
    assert __version__ == "0.1.2"


def test_view(django_settings):
    from wagtail_typograf.views import typograf_api

    data = {
        "blocks": [
            {
                "key": "34hib",
                "text": "\"'Vinnie' - is my favourite book\", - he says.",
                "type": "unstyled",
                "depth": 0,
                "inlineStyleRanges": [],
                "entityRanges": [],
                "data": {},
            }
        ],
    }

    request = RequestFactory().post(
        "/api/typograf/",
        data,
        content_type="application/json",
    )
    request.user = type(
        "User",
        (),
        {
            "is_staff": True,
            "is_active": True,
        },
    )

    response = typograf_api(request)
    assert response.status_code == 200

    data = json.loads(response.content)
    assert data["success"] == True
    assert (
        data["data"]["blocks"][0]["text"]
        == "“‘Vinnie’\u202f—\u2009is\xa0my\xa0favourite book”,—\u2009he\xa0says."
    )
