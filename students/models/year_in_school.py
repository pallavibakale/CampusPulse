from students.models.base import BaseModel


class YearInSchool(BaseModel):
    @classmethod
    def get_url_name(cls):
        return 'year-in-school'

    class Meta(BaseModel.Meta):
        ordering = ['id']
        verbose_name = "Year In School"
        verbose_name_plural = 'Years In School'
