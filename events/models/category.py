from django.db.models import Model, AutoField, CharField

class Category(Model):
    
    id = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False, blank=False, unique=True)
    
    def __str__(self) -> str:
        return self.name