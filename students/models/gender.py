from students.models.base import BaseModel


class Gender(BaseModel):
    @classmethod
    def get_url_name(cls):
        return 'gender'

    class Meta(BaseModel.Meta):
        verbose_name = "Gender"
        verbose_name_plural = 'Genders'
