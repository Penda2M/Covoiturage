from django.db import models

class Person(models.Model):
    nom = models.CharField(max_length=250, null=False)
    prenom = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.prenom

class Conducteur(models.Model):
    nbre_place = models.IntegerField(null=False, default=0)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.prenom

class Passager(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.prenom

class Trajet(models.Model):
    depart = models.CharField(max_length=255, null=False)
    arrive = models.CharField(max_length=255, null=False)
    prix = models.FloatField(null=False)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    passager = models.ManyToManyField(Passager)

    


