from django.contrib import admin

# Register your models here.
from django.contrib import admin

from drugs.models import Compound
from drugs.models import Target
from drugs.models import Publications


# show fields of Compound table on django admin
class CompoundAdmin(admin.ModelAdmin):
    list_display = ['compound_name', 'chembl_id']
    search_fields = ('compound_name', 'chembl_id')

# show fields of Target table on django admin
class TargetAdmin(admin.ModelAdmin):
    list_display = ['uniprot_id', 'gene_name','target_pref_name']
    search_fields = ('uniprot_id', 'gene_name','target_pref_name')

# show fields of Publications table on django admin
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['authors', 'pubmed_id']
    search_fields = ('authors', 'pubmed_id')


admin.site.register(Compound,CompoundAdmin)
admin.site.register(Target,TargetAdmin)
admin.site.register(Publications,PublicationsAdmin)










