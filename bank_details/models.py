from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    head_office = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE, null=True, default=None)
    branch_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.branch_name} ({self.bank.name})"
