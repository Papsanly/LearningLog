from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # Page with all topics
    path('topics/', views.topics, name='topics'),
    # Page for a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page to add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to add new entry to a topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to edit existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
