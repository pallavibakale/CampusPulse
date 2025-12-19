from students.models.base import BaseModel


class Ethnicity(BaseModel):
    @classmethod
    def get_url_name(cls):
        return 'ethnicity'

    class Meta(BaseModel.Meta):
        verbose_name = "Ethnicity"
        verbose_name_plural = 'Ethnicities'
