import requests


import spacy
from spacy import displacy

import en_core_web_sm







from pycorenlp import StanfordCoreNLP



nlp = StanfordCoreNLP('http://127.0.0.1:7000')
Nlp = en_core_web_sm.load()

def get_featured_sents(corenlp_output):
    sents = []
    openies=[]
    for sentence in corenlp_output['sentences']:
        sent_start_ind = sentence['index']
        sent = []
        print("\n");
        if(len(sentence['openie'])>0):
          print(sentence['openie'])
          openies.append(sentence['openie'])
        for token in sentence['tokens']:
            token_start_ind = token['index']
            word = token['originalText']
            lower_word = word.lower()
            if (word[0] == word[0].upper() and word[0] != word[0].lower()):
                case_tag = 'UP'
            else:
                case_tag = 'LOW'
            ner_tag = token['ner']
            pos_tag = token['pos']
            sent.append(({'token': lower_word, 'ner': ner_tag, 'case_tag': case_tag, 'pos_tag': pos_tag,}))
        sents.append(sent)
    #print(sent)
    return sents,openies
def generation(text):
    output= nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,ner,openie',
        'outputFormat': 'json'})
    #print(output)
    sents,openies=get_featured_sents(output)
    print(openies)
    return openies
def main():
    dict1={}
    
    open('n.txt', 'w').close()
    filehandle = open("text.txt", 'r')
    textinput = filehandle.read()
    
    targets = ['Dr.', 'i.e.', 'etc.','0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9',
               '4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0','6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9',
               '7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','A.','B.','C.','D.',
               'E.','F.','G.','H.','I.','J.','K.','L.','M.','N.','O.','P.','Q.','R.','S.','T.','U.','V.','W.','X.','Y.','Z.']
    replacements = [t.replace('.', 'XYZ') for t in targets]
    for i in range(len(targets)):
         textinput = textinput.replace(targets[i], replacements[i])
    output = textinput.split('.')
    output.pop()
    print(output)
    for o in output:
     output = o.replace('XYZ', '.') 
     
     with open('n.txt', 'a') as the_file:
         the_file.write(output)
         the_file.write('.')
         the_file.write('\n')
    the_file.close()
    
    filehandle.close()
    
    file1 = open("n.txt", 'r')
    text = file1.read()
    print(text)
    
    print('\n-----------INPUT END---------------\n')
    openies=generation(text)
    doc = Nlp(text)
    for x in doc.ents:
        dict1[x.text]=x.label_
    print("\n")
    print(dict1)
    for i in openies:
        j=0;
        
        for key in dict1:
          
          if i[j]['subject']==key:
              #print(i[j]['subject'],key)
              if dict1[key]== 'PERSON':
                  print('who' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='NORP':
                  print('who' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='ORG':
                   print('which' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                   print(i[j]['subject'] )
              elif dict1[key]=='DATE':
                  print('when' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i['subject'] )
              elif dict1[key]=='MONEY':
                  print('how much' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='FAC':
                  print('which' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='GPE':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )

              elif dict1[key]=='GPE':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='LOC':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )

              elif dict1[key]=='PRODUCT':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='EVENT':
                  print('what' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              
              elif dict1[key]=='WORK_OF_ART':
                  print('which' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='LANGUAGE':
                  print('which language' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
                
              elif dict1[key]=='TIME':
                  print('at what time' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='PERCENT':
                  print('How much percent' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='QUANTITY':
                  print('How much ' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
        j=j+1;  
                  
            
                  
                  
                  
              
                  
        
    

if __name__ == "__main__":
    main()
