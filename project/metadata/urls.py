from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from project.metadata.views import Metadata


urlpatterns = [
    path(
        "metadata/<slug:contract_address>/<int:token_id>/",
        view=Metadata.as_view(),
        name="metadata",
    ),
]
