# automatic-question-generator
we need to start standard core nlp server  which is simple web api server
server has different default properties 
a)output format is json 
b)the default enabled annotators(Here are the basic Natural Language Processing capabilities (or annotators) that are usually necessary to extract language units from textual data for sake of search and other applications: Sentence breaker - to split text (usually, text paragraphs) to sentences) are 
tokenize-split the words
ssplit-split text into sentences
pos-parts of speech tagging
lemma-lemmatization conversion of wordforms into root 
ner-named entity recognition tagging
depparse-dependendency parser means find the relation between the words. 
coref-Coreference resolution is the task of finding all expressions that refer to the same entity in a text. It is an important step for a lot of higher level NLP tasks that involve natural language understanding such as document summarization, question answering, and information extraction.
natlog-natural logic annotator it places an operator annotation and polarity annotation on tokens
openie-open information extraction refers to extraction of relation tuples(sub,rel,obj)
we use spacy which is used to build information extraction or natural language understanding systems, or to pre-process text for deep learning.
at first we split the text into proper sentences for that we have done some text cleaning
later we generate openie for each sentence.
then we load spacy and then apply to the text.
then we create a dictionary in which key is token and value is ner.
if subjects in openie and keys in dictionary are equal then we create a question by replacing subject with question tag and combined it with relation and object and the respecive subject will be answer.
