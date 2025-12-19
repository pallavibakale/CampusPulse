from students.models.gender import Gender
from students.views.base import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView

class GenderListView(BaseListView):
    model = Gender

class GenderCreateView(BaseCreateView):
    model = Gender

class GenderDeleteView(BaseDeleteView):
    model = Gender

class GenderDetailView(BaseDetailView):
    model = Gender

class GenderUpdateView(BaseUpdateView):
    model = Gender