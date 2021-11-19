import json
from glob import glob
import requests
from rouge import Rouge

def get_rouge_score():

    '''
    Summarize some BBC News articles and compute their rouge-1, rouge-2 and rouge-l scores.
    '''

    url = 'http://127.0.0.1:5000/summarize'

    news = glob('test/resources/News Articles/*/*.txt')

    news.sort(key=lambda x: x.split('/')[-1])

    r1_recall_list=[]
    r1_precision_list=[]
    r1_f1_list=[]
    r2_recall_list=[]
    r2_precision_list=[]
    r2_f1_list=[]
    rl_recall_list=[]
    rl_precision_list=[]
    rl_f1_list=[]

    for i in news[:20]:
        with open(i, 'r') as truth_file:
            req = requests.post(url, json = json.dumps({'text': truth_file.read()})).json()
            summary = req['summary']

            scores = Rouge().get_scores(truth_file.read(), summary, avg=True)

            print("Original")
            print(truth_file.read())
            print("#########################################################################")
            print("Summary")
            print(summary)
            print("#########################################################################")
            print("Rouge metrics")
            print(scores)

            r1_recall_list.append(scores['rouge-1']['r'])
            r1_precision_list.append(scores['rouge-1']['p'])
            r1_f1_list.append(scores['rouge-1']['f'])

            r2_recall_list.append(scores['rouge-2']['r'])
            r2_precision_list.append(scores['rouge-2']['p'])
            r2_f1_list.append(scores['rouge-2']['f'])

            rl_recall_list.append(scores['rouge-l']['r'])
            rl_precision_list.append(scores['rouge-l']['p'])
            rl_f1_list.append(scores['rouge-l']['f'])

    print("Mean Rouge-N1 Recall: " + str(sum(r1_recall_list)/len(r1_recall_list)))
    print("Mean Rouge-N1 Precision: " + str(sum(r1_precision_list)/len(r1_precision_list)))
    print("Mean Rouge-N1 F1: " + str(sum(r1_f1_list)/len(r1_f1_list)))
    print("Mean Rouge-N2 Recall: " + str(sum(r2_recall_list)/len(r1_recall_list)))
    print("Mean Rouge-N2 Precision: " + str(sum(r2_precision_list)/len(r1_precision_list)))
    print("Mean Rouge-N2 F1: " + str(sum(r2_f1_list)/len(r1_f1_list)))
    print("Mean Rouge-L Recall: " + str(sum(rl_recall_list)/len(r1_f1_list)))
    print("Mean Rouge-L Precision: " + str(sum(rl_precision_list)/len(r1_f1_list)))
    print("Mean Rouge-L F1: " + str(sum(rl_f1_list)/len(r1_f1_list)))


if __name__== "__main__":
    get_rouge_score()
