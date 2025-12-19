from django.db.models import Model, AutoField, CharField

class BaseModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    @classmethod
    def get_url_name(cls):
        return cls.__name__.lower()

    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'