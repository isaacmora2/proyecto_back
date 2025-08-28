from django.db import models
from django.contrib.auth.models import User

class Assignee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(null=False)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignees')

    def _str_(self):
        return f"{self.name} ({self.email})"


class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_applications')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Priority(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    def _str_(self):
        return self.name

class Complexity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    def _str_(self):
        return self.name

class TestingType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    def _str_(self):
        return self.name

class TestCase(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    steps = models.TextField()
    prerequisites = models.TextField()
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE, related_name='test_cases')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='test_cases')
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    complexity = models.ForeignKey(Complexity, on_delete=models.PROTECT)
    testing_type = models.ForeignKey(TestingType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_test_cases')

    def _str_(self):
        return self.name


class TestPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    test_cases = models.ManyToManyField(TestCase, related_name='test_plans')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='test_plans')
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_test_plans')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name