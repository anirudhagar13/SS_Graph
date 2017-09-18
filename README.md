# SS(Semantic Similarity)-Graph
Custom Semantic Graph based on Wordnet
--------------------------------------

> The system leverages this graph to semantically compare two documents and gives back a similarity score.
> User can view paths over UI as to how words are related to each other in our custom semantic graph.

#Steps to Create:
-------------------
	1. Install python2.7.
	2. Download nltk package in python via pip-install/easy-install.
    3. Get wordnet, penntreebank from nltk corpus in python, incase any dependency missed get it using nltk.download() > dependency.
    4. Run Creator.sh to create graphdata.
    5. If using Powershell, run the above file as 'Measure-Command {start-process sh Creator.sh -Wait}', if bash, run 'time Creator.sh'
    6. Incase of any failures, clear Shelves folder and rerun Creator.sh
    7. The System is now good to go, Open UI.
    8. Set direct paths to respective folders in views.py inside ssgraph/graph.
    8. Run server using 'python manage.py runserver'.
    9. Open link displayed on cosole, have fun with the platform.

#How to Use:
-------------------
    1. After the screen renders, either type two documents.
    2. Compare them by clicking on Compare button.
    3. To see semantic matches of word found in the other document, select wordtree radio button and click on word.
    4. To see how in graph the words are related, select network graph radio button and click on colored word buttons.
    5. To know details about each node just click on node, and see details appear below.
    6. To know edge meanings refer to the color coded legends on the side.
    7. To see how document gets broken down into sentences and then into words, go to logs and read each log.
    8. Can be used to compare patents by uploading files, .txt or .docx only.
    9. Select the section of patent you want to compare and click on compare.
    10. Read logs to know the intricacies of patent comparison.
    11. No Network graph and wordtree created for file uploads to avoid cluttering.