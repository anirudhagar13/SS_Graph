# SS(Semantic Similarity)-Graph
Custom Semantic Graph based on Wordnet

-The System leverages this graph to semantically compare two documents and give back a similarity score.
-User can view paths over UI as to how words are related to each other in our custom semantic graph

#Steps to Create:
-------------------
	> Install python2.7
	> Download nltk package in python using pip-install/easy-install
    > Get wordnet, penntreebank from nltk corpus in python, incase any dependency missed get it using nltk.download() > dependency 
    > Run Creator.sh to create graphdata, it is a shell file
    > If using Powershell run 'Measure-Command {start-process sh Creator.sh -Wait}', if bash run 'time Creator.sh'
    > Incase of any failures, clear Shelves folder and rerun Creator.sh
    > The System is now good to go, Open UI and have fun :)