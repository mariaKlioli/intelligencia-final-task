import requests
import json
import django
import time
from django.db.models import F
django.setup()
from drugs.models import Compound
from drugs.models import Target
from drugs.models import Publications

# initial values in database
value_offset = 0
initial_url = 'https://drugtargetcommons.fimm.fi/api/data/bioactivity/'
initial_response = requests.get(initial_url)
initial_response_to_json = json.loads(initial_response.text)
initial_bioactivity_list = initial_response_to_json.get('bioactivities')
retrieve_meta_field = initial_response_to_json.get('meta')
start_time = time.time()
end_time = 0


# function for to avoid duplications in each table
def avoid_duplications(compound_name, chembl_id, uniprot_id, authors, pubmed_id, gene_name, target_pref_name):
    avoid_douplications_in_Compound = Compound.objects.filter(compound_name=compound_name, chembl_id=chembl_id)
    avoid_douplications_in_Target = Target.objects.filter(gene_name=gene_name, target_pref_name=target_pref_name,
                                                          uniprot_id=uniprot_id)
    avoid_douplications_in_Publications = Publications.objects.filter(pubmed_id=pubmed_id, authors=authors)
    if avoid_douplications_in_Compound.exists() and avoid_douplications_in_Target.exists() and avoid_douplications_in_Publications.exists():
        return avoid_douplications_in_Compound, avoid_douplications_in_Target, avoid_douplications_in_Publications


# function for retrieving data from api and store in bioactivities database
def store_data_in_DB():
    compound_data = ''
    publications_data = ''
    target_data = ''

    for offset in range(0, retrieve_meta_field['total_count'], 500):
        url2 = 'https://drugtargetcommons.fimm.fi/api/data/bioactivity/?limit=500' + '&offset=' + str(offset)
        response = requests.get(url2)
        response_text = json.loads(response.text)
        bioactivities_response = response_text.get('bioactivities')

        for i in bioactivities_response:

            if avoid_duplications(i.get('compound_name'), i.get('chembl_id'), i.get('uniprot_id'), i.get('authors'),
                                  i.get('pubmed_id'),
                                  i.get('gene_name'), i.get('target_pref_name')):
                print('These values already exist')

            else:
                if (i.get('compound_name') or i.get('chembl_id') or i.get('uniprot_id') or i.get('authors') or i.get(
                        'pubmed_id') or i.get('gene_name') or i.get('target_pref_name')):
                    print('at least one value is not empty')

                    publications_data = Publications.objects.create(
                        authors=i.get('authors'),
                        pubmed_id=i.get('pubmed_id'))
                    compound_data = Compound.objects.create(
                        compound_name=i.get('compound_name'),
                        chembl_id=i.get('chembl_id'))
                    target_data = Target.objects.create(
                        uniprot_id=i.get('uniprot_id'),
                        gene_name=i.get('gene_name'),
                        target_pref_name=i.get('target_pref_name')
                    )

                    target_data.publication.add(publications_data)
                    compound_data.target.add(target_data)

        print('The paginated url is' + url2)
        end_time = time.time()
        print("Time passed ", end_time - start_time)

    return compound_data, publications_data, target_data


if __name__ == '__main__':
    store_data_in_DB()
    # Compound.objects.all().delete()
    # Target.objects.all().delete()
    # Publications.objects.all().delete()
