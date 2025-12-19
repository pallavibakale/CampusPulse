from students.models.major import Major
from students.views.base import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView

class MajorListView(BaseListView):
    model = Major

class MajorCreateView(BaseCreateView):
    model = Major

class MajorDeleteView(BaseDeleteView):
    model = Major

class MajorDetailView(BaseDetailView):
    model = Major

class MajorUpdateView(BaseUpdateView):
    model = Major