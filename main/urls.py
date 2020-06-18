from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index')
    ,path('view-lecture/<int:lecture_number>', views.view_lecture, name='view_lecture')
    ,path('tinymce/', include('tinymce.urls'))
]
