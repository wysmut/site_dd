from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
title = models.CharField(max_length=200)
description = models.TextField()

def __str__(self):
    return self.title

class Question(models.Model):
test = models.ForeignKey(Test, on_delete=models.CASCADE)
text = models.TextField()

def __str__(self):
    return self.text[:50]

class Answer(models.Model):
question = models.ForeignKey(Question, on_delete=models.CASCADE)
text = models.CharField(max_length=200)
is_correct = models.BooleanField(default=False)

def __str__(self):
    return self.text

class Result(models.Model):
user = models.ForeignKey(User, on_delete=models.CASCADE)
test = models.ForeignKey(Test, on_delete=models.CASCADE)
score = models.IntegerField()
date_taken = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user.username} - {self.test.title}"
