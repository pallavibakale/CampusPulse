from django.db.models import Model, CharField, ForeignKey, EmailField, PROTECT, IntegerField, Sum
from datetime import date

from getting_to_graduation.common.util.dates import format_dates

class Student(Model):
    
    pfw_id = IntegerField(unique=True, primary_key=True)
    name = CharField(max_length=100)
    email = EmailField(unique=True)
    gender = ForeignKey(to="Gender", on_delete=PROTECT)
    ethnicity = ForeignKey(to="Ethnicity", on_delete=PROTECT)
    major = ForeignKey(to="Major", on_delete=PROTECT)
    year_in_school = ForeignKey(to="YearInSchool", on_delete=PROTECT)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

    def get_total_points(self, start_date:date|None = None, end_date:date|None = None)-> int:
        
        # start_date = date(year=2023, month=1, day=1)
        
        start_date, end_date = format_dates(start_date=start_date, end_date=end_date)
        
        return self.event_set.filter(date__gte=start_date, date__lte=end_date).aggregate(Sum('points'))['points__sum'] or 0

    def get_category_points(self, category, start_date:date|None = None, end_date:date|None = None)-> int:
        
        start_date, end_date = format_dates(start_date=start_date, end_date=end_date)
        
        return self.event_set.filter(category__name=category, date__gte=start_date, date__lte=end_date).aggregate(Sum('points'))['points__sum'] or 0
