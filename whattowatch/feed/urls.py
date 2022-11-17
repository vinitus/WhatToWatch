from django.urls import path
from . import views

app_name = 'feed'
urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    # # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

