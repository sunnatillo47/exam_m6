from django.db import models

class Languages(models.Model):
    lan_name = models.CharField(max_length=50, verbose_name="Language name")
    lan_info = models.CharField(max_length=255, verbose_name="Language info")

    def __str__(self):
        return self.lan_name

    class Meta:
        db_table = 'languages'
        verbose_name = 'Language'

class Freamworks(models.Model):
    fw_name = models.CharField(max_length=50, verbose_name="Freamwork name")
    fw_info = models.CharField(max_length=255, verbose_name="Freamwork info")
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)

    def __str__(self):
        return self.fw_name

    class Meta:
        db_table = 'freamworks'
        verbose_name = 'FREAMWORKS'
