from typing import Any

from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from events.models import Event
from students.models import Student
from getting_to_graduation.common.util.web_plotter import count_plot, hist_plot

class EventListView(generic.ListView):
    model = Event
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        for event in context["event_list"]:
            event.attendance = event.students_attended.count()
        
        return context
    
class EventDetailView(generic.DetailView):
    model = Event
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context["event"].attendees = context["event"].students_attended.all()
        
        gender_count_plot_queryset = context["event"].attendees.values_list("gender__name", flat=True)
        ethnicity_count_plot_queryset = context["event"].attendees.values_list("ethnicity__name", flat=True)
        year_in_school_count_plot_queryset = context["event"].attendees.values_list("year_in_school__name", flat=True)
        context["event"].gender_plot = count_plot(
            queryset=gender_count_plot_queryset,
            xlabel="Gender",
            title="Gender Distribution"
        )
        context["event"].ethnicity_plot = count_plot(
            queryset=ethnicity_count_plot_queryset,
            xlabel="Ethincity",
            title="Ethincity Distribution",
            y_major_locator=2
        )
        context["event"].year_in_school_plot = count_plot(
            queryset=year_in_school_count_plot_queryset,
            xlabel="Year In School",
            title="Year In School Distribution"
        )
        return context
    
class EventCreateView(generic.CreateView):
    model = Event
    fields = "__all__"
    
    def get_success_url(self) -> str:
        return reverse('event-list')
    
class EventUpdateView(generic.UpdateView):
    model = Event
    fields = "__all__"
    success_url = reverse_lazy("event-list")
    
class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy("event-list")
    

def add_students_to_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        pfw_ids = request.POST.get('pfw_ids')
        if pfw_ids:
            pfw_id_list = []
            pfw_email_list = []
            for pfw_id in pfw_ids.split():
                if pfw_id.strip():
                    if pfw_id.isdigit():
                        pfw_id_list.append(int(pfw_id))
                    elif pfw_id.endswith("@pfw.edu"):
                        pfw_email_list.append(pfw_id)
                    elif pfw_id.startswith("(") and pfw_id.endswith("@pfw.edu)"):
                        email = pfw_id.replace("(","").replace(")","")
                        pfw_email_list.append(email)
                
            students = Student.objects.filter(pk__in=pfw_id_list) | Student.objects.filter(email__in=pfw_email_list)
            event.students_attended.add(*students)
            return redirect('event-detail', pk=event_id)

    return render(request, 'events/add_students_to_event.html', {'event': event})
    