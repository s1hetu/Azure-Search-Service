### Azure AI Search

Azure AI Search is an Azure resource used for adding a full text search experience.

**Search Service** : search-query-csv

**Resource Group** : Search_CSV_Data

**Index name** : azureblob-index

**Document_Key** : AzureSearch_DocumentKey 

**Searchable Fields** : Department, Gender, JobRole

<br>
<br>

### Project Setup
```python
pip install -r requirements.txt
```

### Run Project
```python
python main.py
```

When you run the above command, it will task you to enter a text to be searched. The results will be provided on the basis of text you enter.

<br>

**_NOTE_** : _Here **IBM-Dataset.csv** file is used as reference for seraching the data._