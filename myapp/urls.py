from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, Form, Detail, Tale, NewsletterSignup

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('form/', Form.as_view(), name = "folkForm"),
    path('tale/<int:post_id>/', Tale.as_view(), name='tale'),
    path('detail/', Detail.as_view(), name="detail"),
    path('newsletter/', NewsletterSignup.as_view(), name='newsletter_signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
