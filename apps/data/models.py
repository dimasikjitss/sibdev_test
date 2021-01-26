from django.db import models


class CsvFile(models.Model):
    username = models.CharField(max_length=255,null=True)
    gems = models.CharField(max_length=255,null=True)
    spent_money = models.IntegerField(null=True)
    csv = models.FileField()

    def __str__(self):
        return "{} -- {} -- {} ".format(self.username, self.gems, self.spent_money)