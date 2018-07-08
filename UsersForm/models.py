# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)