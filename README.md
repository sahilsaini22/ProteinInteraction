# ProteinInteraction

This application allows the user to upload protein interaction related information in the form of a CSV file to a Postgresql database, and view and filter the interaction details based on the various parameters.


How to run the application locally:

1. Run an instance of pgAdmin<br/>
  1.1 Create a database 
2. In ./interactions/setting.py, enter the database details in "DATABASES" section.
3. In the terminal, run the following commands in order:<br/>
    python manage.py makemigrations<br/>
    python manage.py migrate
    
This will sync the application with the database. To validate, in pgAdmin, you can view the application related table in "Databases/<Your_Database_Name>/Schemas/public/Tables/"

4. Run the following command in the terminal to launch the application locally:<br/>
  python manage.py runserver
  
  
Application Functonalities:
1. Upload the Protein Intertaction Information<br/>
  1. Click on the link to upload
  2. Click on "Upload a file"
  3. Browse the file 
  4. Click in "Upload"
  
  File Structure:
  The upload file should be a CSV file(without a header) with the following field sequence:<br/>
  COEXPRESSION<br/>
  COMBINED_SCORE<br/>
  COOCCURANCE<br/>
  DATABASE<br/>
  EXPERIMENTAL<br/>
  FUSION<br/>
  NEIGHBORHOOD<br/>
  PROTEIN1<br/>
  PROTEIN2<br/>
  TEXTMINING
  
 2. Filter Interaction Data<br/>
  1. Enter the filter criteria in the desired fields
  2. Numeric fields have the option of filtering for more than, less than, equal to, not equal to the entered value
  3. Click on "Filter"
    
