# intelligencia-final-task
Data-engineering-task In this task the goal was to create a data streaming by inserting spesific data from a third part API into a local postgresql. In the following paragraphs you will see two titles. In BRAIN STORMING paragraph, I will write down and explain the whole logic behind the implementation of the project. The way that I created my database, the way that I chose to retrieve my data,etc.In MANUAL paragraph I will extensively describe the whole procedure that someone has to do in order to run the project.

**BRAIN STORMING**

The main goal as I mentioned before, is to retrieve data from an API (especially spesific fields) and store them in a postgresql database. The 6 fields of data that I had to retrieve are : compound_name, chembl_id, uniprot_id, gene_name, target_pref_name,authors and pubmed_id. In a nutshell, compound_name represents the name of the compound that it is possible to bind in a protein, chembl_id is respectively the id of each compound in a spesific database called chembl. Furthermore, gene_name represents the name of the gene that it is responsible for the production of proteins. Uniprot_id represent the id of a protein in a databas called uniprot, while the target_pref_name is mainly the name of the protein or enzyme. On the other hand, pubmed_id is an id that refers to a spesific scientific article, while authors field update us for the name of the authors of each article. Due to the previous descriptions of the retrieved fields, I have implemented a database called """" with three tables:

1. Compound (fields: compound_name,chembl_id)

2. Target (fields: uniprot_id, gene_name, target_pref_name)

3. Puplications (fields: authors,pubmed_id) This three tables, have relations. To find them, I throught the following: One compound, can be in many Targets and in many targets ( if the compound does not target to only one protein). One Target can have many compounds. In these two tables we have many to many relation between Compound-Target. One Compound can be found in many publications, while one publication can refer to may targets. Again here we have many to many relation between Compound - Publications. On Target can have many publications where one publication can refer to many targets. Again here, we have a many to many relation between Target-Publications . These considerations have been created based on the format of the datbase in target common page and the respectively paper. After the database relationship creation, I have entered some constraints in order to ensure the data integrity. These are the following:

1. Constraints for the uniqueness of each row inserted in the database ( avoid duplications function )

2. Constraints for the nature of data that inserted into the datatable (Character, integers,etc)

Validators for the data that may one user wants to add in django admin page. For example, some fields need to be only numbers, while some others both numbers and characters. All the previous statements, had to do with the architecture of the database. Now, for the retrieval of the data from the API, I read the instructions and the scientific article for the target common database and I saw, that the data occur paginated. In each page I can retrieve max 500. So, my pagination fuction retrieves 500 items in each iteration and increases the offset which again has the value 500 starting from 0. Due to the fact that the total count of data from the API are about 14bilions, the retrieval and insertion in database is a bit slow . About 100.000 per hour insert into the database. delete data in table quicly:

**Compound.objects.all().delete()**
**Target.objects.all().delete()**
**Publications.objects.all().delete()**

**target = Target.objects.get(id=379)**
**target.gene_name = F('gene_name')**
**target.uniprot_id = F('uniprot')**
**target.gene_name = 'gggg'**
**target.uniprot_id = '333'**
**target.save()**
Now, in bonous section you asked to make system capable of incremental updates. Incremental updates in data pipelines is a spesific procedure that has two explanations:

Be able to update fields in a database without running the whole database
Make the system able if the API has new records ,to insert these records win postgresql without running again the whole database. From the previous two options, I have implemented the first one. User can update value either from django admin panel or through python code in command line. The command for example to update values in a record is:
The second option, I couldn't implement it, as I observed I haven't a field from the API that could informed be about the last record inserted or something like the time each record inserted in order to syhcronize with my code. However, my idea is exactly that,

**MANUAL**

Here are represented instructions for the set up of the application. As I mentioned before, the application has bee n developed with the use of Python Django framework and Postgresql database. You must do the following steps for the application to be executed:

1. Open an editor where the project will be able to execute (eg. Pycharm)
2. Clone the project from the github link that I have provided you with.
3. You can observe that in the files of the project, you can find a file call requirements.txt. In this text file are provided the necessary packages that the project uses and you have to install in your environment.
4. Now, you have to install some applications for the postgresql. The first is called pgAdmin and you can download it from the following url (either for MACOS or WINDOWS): postgresql.org/ftp/pgadmin/ .
5. The next you have to download is the POSTGRESQL server. The link for that is the following: postgresql.org/downloads and choose you operating system.
6. Open now the pgAdmin you downloaded in step 4. You will asked to insert a password. You are free to insert what you want. However, I have inserted as master password "admin" .
7. Now, open the application postgreSQL in step 6. Install and set up the application. Again here you will asked to insert a password (YOU HAVE TO REMEMBER THE PASSOWRD- here I have inserted pass1234).
8. Now, if we open the pdAdmin it will request us the two passwords, so insert them.
9. Now, we have to create a database in the pdAdmin panel ( databases -> right click -> create -> database) and give a name. 10. My database name for example is called bioactivities.
11. The next step is to set the name of the database in you settings.py folder of the project that you have cloned. In my case for example "bioactivities".
12.Then you have to set up the virtual envs and install the packages that I have created by typing the following command: 
**pip -r install requirements.txt**
13. Then type on the terminal of pycharm the following commands: python manage.py makemigrations python manage.py migrate
Our database is ready! Now run the Views.py and drugs_info. The second one will show you a destination. You click on it and add at the end the word /admin. The url is like this: **http://127.0.0.1:8000/admin/**
14. You have to enter here the login username and password. We have to create for the database a superuser. Go back to the terminal of pycharm and type: 
**python manage.py createsuperuser**
**enter user name: maria** 
**enter password: lioli**
15. Your new user for django admin panel has been created. Enter credentials, run Views.py and you will see thath django panel will have records inside.
