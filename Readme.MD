Note: For windows users, please install Microsoft visual studio tools latest from https://visualstudio.microsoft.com/downloads/.

This is required for Spacy to install on windows.

It should be fine for Linux based users I guess. :)

The API endpoint is : http://127.0.0.1:8000/text_summarizer/summary.

It is ideal if you create a virtual environment for the project.

Steps(Run these commands in sequence):
1. pip install -r requirements.txt
2. python manage.py runserver 
3. python -m spacy download en
