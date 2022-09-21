from django.db import models


class Strings:
    header = 'Что нужно знать перед тестированием?'
    year = '2022'
    start = 'Начать тест'

class Foreword(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foreword'



