from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from getting_to_graduation.common.util.web_plotter import count_plot
from students.models import Student
from django.db.models import Sum, Q
from events.models import Category
from django.shortcuts import render
import csv
from datetime import datetime
from django.http import HttpResponse
from datetime import date, datetime

from getting_to_graduation.common.util.dates import format_dates

CATEGORIES = Category.objects.values_list('name', flat=True)

class StudentListView(generic.ListView):
    model = Student
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        total_points = 0
        inactive_students = 0
        for student in context['student_list']:
            student.total_points = student.get_total_points()
            total_points += student.total_points
            if student.total_points == 0:
                inactive_students += 1
            
            # Add points for each category
            for category in CATEGORIES:
                setattr(student, f'{category.lower()}_points', student.get_category_points(category))
        
        context["stats"] = {}
        context["stats"]["total_points"] = int(total_points)
        context["stats"]["avg_points"] = round(total_points/len(context['student_list']))
        context["stats"]["inactive"] = inactive_students
            
        return context
    
class StudentDetailView(generic.DetailView):
    model = Student
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context["student"].points = {
            "total": context['student'].get_total_points()
        }
        
        for category in CATEGORIES:
            context["student"].points[category] = context['student'].get_category_points(category)
            
        context["student"].events = context["student"].event_set.all()
        return context
    
    
class StudentCreateView(generic.CreateView):
    model = Student
    fields = "__all__"
    
    success_url = reverse_lazy("student-list")
    
    
class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("student-list")
    
class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")

def students_points_view(request):
    
    start_date, end_date = format_dates()
    
    # Query to get all students who have more than 150 points
    students_150_points = Student.objects.annotate(total_points=Sum('event__points', filter=Q(event__date__gte=start_date, event__date__lte=end_date))).filter(total_points__gte=150).order_by('-total_points')

    # Query to get all students who have more than 300 points
    students_300_points = Student.objects.annotate(total_points=Sum('event__points', filter=Q(event__date__gte=start_date, event__date__lte=end_date))).filter(total_points__gte=300).order_by('-total_points')

    # Query to get top 5 students in terms of points
    top_10_students = Student.objects.annotate(total_points=Sum('event__points', filter=Q(event__date__gte=start_date, event__date__lte=end_date))).order_by('-total_points')[:10]

    context = {
        'students_150_points': students_150_points,
        'students_300_points': students_300_points,
        'top_10_students': top_10_students,
    }

    return render(request, 'students/students_winners.html', context)

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    now = datetime.now()
    response['Content-Disposition'] = 'attachment; filename="Getting-To-Graduation-{}.csv"'.format(now.strftime("%H-%M-%S-%m-%d-%Y"))

    writer = csv.writer(response)

    students = Student.objects.all()
    if now.month >= 8:  # August to December -> academic year starts this year
        start_academic_year = date(now.year, 8, 1)
        end_academic_year = date(now.year + 1, 5, 31)
    else:  # January to July -> academic year started last year
        start_academic_year = date(now.year - 1, 8, 1)
        end_academic_year = date(now.year, 5, 31)

    # Create a list to store student data
    student_data = []

    for student in students:
        total_points = student.get_total_points(start_date=start_academic_year)
        social_points = student.get_category_points('Social', start_date=start_academic_year)
        educational_points = student.get_category_points('Educational', start_date=start_academic_year)
        cultural_points = student.get_category_points('Cultural', start_date=start_academic_year)

        # Get the events attended by the student within the academic year
        events = student.event_set.filter(date__gte=start_academic_year, date__lte=end_academic_year)

        # Format the events as "Event 1 (E), Event 2 (C), Event 3 (S) ..."
        events_str = ', '.join([f'{event.title} ({event.category.name[0]})' for event in events])

        student_data.append([
            student.name, student.email, student.gender.name, student.ethnicity.name,
            student.major.name, student.year_in_school.name, total_points,
            social_points, educational_points, cultural_points, events_str
        ])

    # Sort students by total points in descending order
    student_data.sort(key=lambda x: x[6], reverse=True)  # Sorting by total_points (index 6)

    # Assign rankings (handling ties)
    rank = 1
    previous_points = None
    rankings = []
    for i, data in enumerate(student_data):
        if previous_points is not None and data[6] != previous_points:
            rank = i + 1  # Rank changes only if points are different
        rankings.append(rank)
        previous_points = data[6]

    # Write to CSV with ranking
    writer.writerow(["Rank", "Name", "Email", "Gender", "Ethnicity", "Major", "Year", 
                    "Total Points", "Social Points", "Educational Points", "Cultural Points", "Events"])

    for rank, student_info in zip(rankings, student_data):
        writer.writerow([rank] + student_info)

    return response
 