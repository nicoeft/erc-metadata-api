from django.urls import path, include

urlpatterns = [
    path("", include("project.metadata.urls")),
]
