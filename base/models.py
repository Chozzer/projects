from django.db import models

# Create your models here.

class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=64)





class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=64)


class projects(models.Model):
    id = models.IntegerField(primary_key=True)
    parent = models.IntegerField(default=0) # = parent project, else it is a subproject with a parent of parent number
    name = models.CharField(max_length=64)
    type = models.ForeignKey(Type, on_delete=models.CASCADE) 
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    completed = models.BooleanField()
    archived = models.BooleanField()
    lastActivity = models.DateField()
    

    def __str__(self):
        return self.name
    
    
class user_roles(models.Model):
    userid = models.IntegerField(primary_key=True) #this needs changing to point to the users id field
    project_id = models.ForeignKey(projects, on_delete=models.CASCADE)
    role = models.TextField(max_length=32)


class notes(models.Model):
    id = models.IntegerField(primary_key=True)
    ref = models.ForeignKey(projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()

class links(models.Model):
    id = models.IntegerField(primary_key=True)
    ref = models.ForeignKey(projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)

class tasks(models.Model):
    id = models.IntegerField(primary_key=True)
    ref = models.ForeignKey(projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    task = models.TextField()
    order = models.IntegerField(unique=True)


class documents(models.Model):
    id = models.IntegerField(primary_key=True)
    ref = models.ForeignKey(projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    doc = models.BinaryField()


