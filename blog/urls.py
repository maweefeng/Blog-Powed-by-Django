from django.urls import path,include
import blog.views

urlpatterns = [
    path("hello_world",blog.views.hello_world),
    path("index",blog.views.get_index_summary_page),
    path("detail/<int:summary_id>",blog.views.get_detail_page,name = 'get_detail_page')

]