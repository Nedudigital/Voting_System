from django.db import models

# Create your models here.

#so here we creatre tables that will reflect in our database

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    #we used foreignkey because we canted to relate question to the question model.
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
       