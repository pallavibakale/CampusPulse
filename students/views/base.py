from django.views import generic
from django.urls import reverse_lazy
from django.db.models.query import RawQuerySet
from typing import Any
from django.db.models import Sum
from getting_to_graduation.common.util.web_plotter import bar_plot, count_plot
from students.models.base import BaseModel

class BaseListView(generic.ListView):
    model = BaseModel
    
    def get_template_names(self) -> list[str]:
        return ["students/model_list.html"]

    def get_context_object_name(self, object_list: RawQuerySet) -> str | None:
        return "object"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["object"].name = self.model.__name__
        context["object"].detail_url_name = f"{self.model.get_url_name()}-detail"
        context["object"].create_url_name = f"{self.model.get_url_name()}-create"
        context["plot"] = {}

        object_count_list = []
        for object in context["object"]:
            object_count_list.extend([object.name]*object.student_set.count())

        object_total_points_list = {}
        for object in context["object"]:
            object_total_points_list[object.name] = 0
            for student in object.student_set.all():
                object_total_points_list[object.name] += student.event_set.aggregate(Sum('points'))['points__sum'] or 0

        context["plot"]["count_plot"] = count_plot(
            queryset=object_count_list,
            xlabel=self.model.__name__,
            title=f"{self.model.__name__} Distribution",
            y_major_locator=2
        )

        context["plot"]["total_points_plot"] = bar_plot(
            queryset={self.model.__name__:object_total_points_list.keys(), "Total Points": object_total_points_list.values()},
            xlabel=self.model.__name__,
            title=f"{self.model.__name__}-wise Total Points",
        )

        return context

class BaseCreateView(generic.CreateView):
    fields = "__all__"
    success_url = reverse_lazy("student-list")

    def get_template_names(self) -> list[str]:
        return ["students/model_form.html"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["form"].action = "Add"
        context["form"].model = self.model.__name__

        return context

class BaseDeleteView(generic.DeleteView):
    template_name = "students/model_confirm_delete.html"
    success_url = reverse_lazy("student-list")

class BaseDetailView(generic.DetailView):
    fields = "__all__"
    success_url = reverse_lazy("student-list")
    template_name = "students/model_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["object"].type = self.model.__name__
        context["object"].students = context["object"].student_set.all()
        context["object"].count = len(context["object"].students)
        
        context["object"].total_points = 0
        for student in context["object"].students:
            student.total_points = student.event_set.aggregate(Sum('points'))['points__sum'] or 0
            student.total_points = int(student.total_points)
            context["object"].total_points += int(student.total_points)
            
        context["object"].average_points = round(context["object"].total_points/context["object"].count)
        
        context["object"].update_url_name = f"{self.model.get_url_name()}-update"
        context["object"].delete_url_name = f"{self.model.get_url_name()}-delete"

        return context

class BaseUpdateView(generic.UpdateView):
    fields = "__all__"
    template_name = "students/model_form.html"
    success_url = reverse_lazy("student-list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["form"].action = "Update"
        context["form"].model = self.model.__name__
        return context