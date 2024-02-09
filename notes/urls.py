from django.urls import path
from notes import views
import notes


urlpatterns=[
    path ("add_note/<int:parent>", notes.views.add_note, name = "add_note"),
    path ("display_note/<int:req_note>", notes.views.display_note, name = "display_note"),
    path ("edit_note/<int:req_note>",notes.views.edit_note, name = 'edit_note' ),
    path ("delete_note/<int:req_note>", notes.views.delete_note, name = 'delete_note'),



]