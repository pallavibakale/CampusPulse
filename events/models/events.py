from django.db.models import Model, TextField, CharField, AutoField, FloatField, ManyToManyField, DateField, ForeignKey, PROTECT

class Event(Model):
    
    id = AutoField(primary_key=True)
    title = CharField(max_length=50, null=False, blank=False)
    subtitle = CharField(max_length=50, null=True, blank=True)
    points = FloatField(blank=False, null=False)
    category = ForeignKey(to="Category", on_delete=PROTECT)
    date = DateField(blank=False, null=False)
    
    students_attended = ManyToManyField(to="students.Student", blank=True)
    
    def __str__(self) -> str:
        return f"{self.title} - {self.date}"
    
    class Meta:
        unique_together = ('title', 'date')
        ordering = ['-date']
    
