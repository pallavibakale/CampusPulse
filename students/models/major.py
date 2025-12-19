from students.models.base import BaseModel


class Major(BaseModel):
    @classmethod
    def get_url_name(cls):
        return 'major'

    class Meta(BaseModel.Meta):
        verbose_name = "Major"
        verbose_name_plural = 'Majors'
