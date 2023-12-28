from django.urls import path
from tasks import views
import tasks




urlpatterns = [
    path("add_task/<int:parent>", tasks.views.add_task, name='add_task'),
    path("display_task/<int:req_task>", tasks.views.display_task, name="display_task"),
    path("edit_task/<int:req_task>", tasks.views.edit_task, name="edit_task"),
    path("delete_task/<int:req_task>", tasks.views.delete_task, name="delete_task"),
    

]