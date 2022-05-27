from django.urls import path, include

urlpatterns = [
    path("v1/", include("project.api.v1.urls")),
]
