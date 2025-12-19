from students.models.ethnicity import Ethnicity
from students.views.base import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView

class EthnicityListView(BaseListView):
    model = Ethnicity

class EthnicityCreateView(BaseCreateView):
    model = Ethnicity

class EthnicityDeleteView(BaseDeleteView):
    model = Ethnicity

class EthnicityDetailView(BaseDetailView):
    model = Ethnicity

class EthnicityUpdateView(BaseUpdateView):
    model = Ethnicity