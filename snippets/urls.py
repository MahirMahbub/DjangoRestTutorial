from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # path(r'snippets/', views.snippet_list),
    # path(r'snippets/<int:pk>', views.snippet_detail),
    path(r'snippets/', views.SnippetList.as_view()),
    path(r'snippets/<int:pk>/', views.SnippetDetails.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path(
    #     "docs/",
    #     SpectacularSwaggerView.as_view(
    #         template_name="swagger-ui.html",
    #         url_name="schema"
    #     ),
    #     name="swagger-ui",
    # ),
    # path('snippets/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)