from students.models.year_in_school import YearInSchool
from students.views.base import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView

class YearInSchoolListView(BaseListView):
    model = YearInSchool

class YearInSchoolCreateView(BaseCreateView):
    model = YearInSchool

class YearInSchoolDeleteView(BaseDeleteView):
    model = YearInSchool

class YearInSchoolDetailView(BaseDetailView):
    model = YearInSchool

class YearInSchoolUpdateView(BaseUpdateView):
    model = YearInSchool