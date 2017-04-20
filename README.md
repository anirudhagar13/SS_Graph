# SS(Semantic Similarity)-Graph
Custom Semantic Graph based on Wordnet

-The System leverages this graph to semantically compare two documents and give back a similarity score.
-User can view paths over UI as to how words are related to each other in our custom semantic graph

#Steps to Create:
-------------------
	1. Install python2.7
	2. Download nltk package in python using pip-install/easy-install
    3. Get wordnet, penntreebank from nltk corpus in python, incase any dependency missed get it using nltk.download() > dependency 
    4. Run Creator.sh to create graphdata, it is a shell file
    5. If using Powershell run 'Measure-Command {start-process sh Creator.sh -Wait}', if bash run 'time Creator.sh'
    6. Incase of any failures, clear Shelves folder and rerun Creator.sh
    7. The System is now good to go, Open UI.
    8. Set paths in Commons and views.py inside ssgraph/graph
    8. Run server using 'python manage.py runserver'
    9. Open link displayed on cosole, have fun with the system.