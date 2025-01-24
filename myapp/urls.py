from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="homepage"),
    # path('', views.index, name="homepage"),
    path('form/', views.form, name="folkForm"),
    # path('tale/', views.tale, name='tale'),
    path('tale/<int:post_id>/', views.tale, name='tale'),
    path('detail/', views.detail, name="detail"),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
