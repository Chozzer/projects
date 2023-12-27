from django.urls import path
from tasks import views
import tasks




urlpatterns = [
    path("add_task/<int:parent>", tasks.add_task, name='add_task'),

]