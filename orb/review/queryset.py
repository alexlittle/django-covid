from django.db import models
from django.db.models import Q


class CriteriaQueryset(models.QuerySet):

    def general(self):
        return self.filter(role__isnull=True)

    def for_role(self, role):
        """Returns both general and role specific criteria"""
        return self.filter(Q(role=role) | Q(role__isnull=True))
