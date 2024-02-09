from django.urls import path
from links import views
import links


urlpatterns=[
    path ("add_link/<int:parent>", links.views.add_link, name='add_link'),
    path ("delete_link/<int:link_id>", links.views.delete_link, name='delete_link')

]