"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from Task import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks',views.Viewset_task_status)
router.register('tasks',views.Viewset_task_priority)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/tasks/' ,views.task_List),
    path('rest/tasks/<int:pk>' ,views.Task_pk.as_view()),
    path('rest/tasks_status/', include(router.urls)),
    path('rest/tasks_prio/', include(router.urls)),

]
