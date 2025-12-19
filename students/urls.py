from django.urls import path
from .views.students import (
    StudentListView, StudentDetailView, StudentCreateView, StudentDeleteView, StudentUpdateView, students_points_view, download_csv
)
from .views.gender import (
    GenderCreateView, GenderDeleteView, GenderDetailView, GenderListView, GenderUpdateView
)

from .views.major import (
    MajorCreateView, MajorListView, MajorDeleteView, MajorDetailView, MajorUpdateView
)

from .views.ethnicity import (
    EthnicityCreateView, EthnicityDetailView, EthnicityListView, EthnicityDeleteView, EthnicityUpdateView
)

from .views.year_in_school import (
    YearInSchoolCreateView, YearInSchoolDetailView, YearInSchoolListView, YearInSchoolDeleteView, YearInSchoolUpdateView
)

urlpatterns = [
    # Student URLs
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('gender/<int:pk>/', GenderDetailView.as_view(), name='gender-detail'),
    path('gender/delete/<int:pk>', GenderDeleteView.as_view(), name='gender-delete'),
    path('gender/update/<int:pk>', GenderUpdateView.as_view(), name='gender-update'),
    path('gender/create/', GenderCreateView.as_view(), name='gender-create'),
    path('gender/', GenderListView.as_view(), name='gender-list'),
    path('major/delete/<int:pk>', MajorDeleteView.as_view(), name='major-delete'),
    path('major/update/<int:pk>', MajorUpdateView.as_view(), name='major-update'),
    path('major/<int:pk>/', MajorDetailView.as_view(), name='major-detail'),
    path('major/create/', MajorCreateView.as_view(), name='major-create'),
    path('major/', MajorListView.as_view(), name='major-list'),
    path('ethnicity/delete/<int:pk>', EthnicityDeleteView.as_view(), name='ethnicity-delete'),
    path('ethnicity/update/<int:pk>', EthnicityUpdateView.as_view(), name='ethnicity-update'),
    path('ethnicity/<int:pk>/', EthnicityDetailView.as_view(), name='ethnicity-detail'),
    path('ethnicity/create/', EthnicityCreateView.as_view(), name='ethnicity-create'),
    path('ethnicity/', EthnicityListView.as_view(), name='ethnicity-list'),
    path('year-in-school/delete/<int:pk>', YearInSchoolDeleteView.as_view(), name='year-in-school-delete'),
    path('year-in-school/update/<int:pk>', YearInSchoolUpdateView.as_view(), name='year-in-school-update'),
    path('year-in-school/<int:pk>/', YearInSchoolDetailView.as_view(), name='year-in-school-detail'),
    path('year-in-school/create/', YearInSchoolCreateView.as_view(), name='year-in-school-create'),
    path('year-in-school/', YearInSchoolListView.as_view(), name='year-in-school-list'),
    path('download_csv/', download_csv, name='student-download-csv'),
    path('winners/', students_points_view, name='student-winners'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('', StudentListView.as_view(), name='student-list'),
]
