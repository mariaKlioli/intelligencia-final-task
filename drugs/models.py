from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
# 3 tables : Compound, Publication and Target
# constraints and validators for the tables

class ConcurrentModificationError(Exception):
    def __init__(self, model, pk):
        super(ConcurrentModificationError, self).__init__(
            "Concurrent modification on %s #%s" % (model, pk))


# table for Publications
class Publications(models.Model):
    pubmed_id = models.CharField(max_length=25500, default='', null=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',       # pubmed_id must be only numbers
            message='Invalid Characters! Please insert number',
            code='invalid_character'
        ),
    ])
    authors = models.CharField(max_length=25500, default='', null=True)

    __original_name = None
    _change = models.IntegerField(default=0)

    def __str__(self): #return string result
        return '{} {} '.format(
            self.pubmed_id, self.authors)


    def save(self, force_insert=False, force_update=False, *args,
             **kwargs):  # function for save the changes manually either from django admin or the command line
        if self.pubmed_id != self.__original_name:
            print('Pubmed_id has been changed')
        if self.authors != self.__original_name:
            print('Authors has been changed')

        super(Publications, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_name = self.pubmed_id
        self.__original_name = self.authors


# table for the Targets(proteins)
class Target(models.Model):
    id = models.AutoField(primary_key=True)
    gene_name = models.CharField(max_length=25500, default='', null=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',  #gene name must have letters
            message='Invalid Characters! Please only characters',
            code='invalid_character'
        ),
    ])
    uniprot_id = models.CharField(max_length=25500, default='', null=True, validators=[
        RegexValidator(
            regex='^[A-Z0-9]*$', #uniprot_is must have both letters and numbers
            message='Invalid Characters! Please characters and numbers',
            code='invalid_Characters'
        ),
    ])
    target_pref_name = models.CharField(max_length=25500, default='', null=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',#uniprot_is must have both letters and numbers
            message='Invalid Characters! Please characters and numbers',
            code='invalid_Characters'
        ),
    ])
    _change =models.IntegerField(default=0)
    publication = models.ManyToManyField(Publications)
    __original_name = None

    def __str__(self):
        return '{} {} {}'.format(
            self.gene_name, self.uniprot_id, self.target_pref_name)

    def save(self, force_insert=False, force_update=False, *args,
             **kwargs):  # function for save the changes manually either from django admin or the command line
        if self.gene_name != self.__original_name:
            print('Gene name has changed')
        if self.uniprot_id != self.__original_name:
            print('Uniprot_id  has changed')
        if self.target_pref_name != self.__original_name:
            print('target_pref_name  has changed')


        super(Target, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_name = self.gene_name
        self.__original_name = self.uniprot_id
        self.__original_name = self.target_pref_name


class Compound(models.Model):
    chembl_id = models.CharField(max_length=25500, default='', null=True)
    compound_name = models.CharField(max_length=25500, null=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Please insert values in English',
            code='invalid_language'
        ),
    ])

    _change = models.IntegerField(default=0)
    target = models.ManyToManyField(Target)
    __original_name = None

    def __str__(self):  # function to return string format of data
        return '{} {} '.format(
            self.compound_name, self.chembl_id,

        )


    def save(self, force_insert=False, force_update=False, *args,
             **kwargs):  # function for save the changes manually either from django admin or the command line
        if self.compound_name != self.__original_name:
            print('Compound name has been changed')
        if self.chembl_id != self.__original_name:
            print('Chembl_id has been changed')

        super(Compound, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_name = self.compound_name
        self.__original_name = self.chembl_id


