# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys, time

from django.shortcuts import render
from django.http import JsonResponse
import os
import sys
sys.path.insert(0, 'C:/Users/aniragar/Documents/School/SS_Graph/ssgraph/mainapp')
from settings import PROJECT_ROOT


# Create your views here.
 # howdy/views.py
from django.views.generic import TemplateView

sys.path.append('C:/Users/aniragar/Documents/School/SS_Graph')
from Parser import *

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'base.html', context=None)


def debug_ajax(request):
    input_data1 = request.GET.get('input_data1', None)
    input_data2 = request.GET.get('input_data2', None)

    print input_data1, input_data2
    dd = Documentclient(doc_1=Unicode(input_data1),doc_2=Unicode(input_data2))
    dd.getmetric()

    wordmap = dd.getWordMap()
    score = dd.getScore()
    allpaths = dd.getPaths()

    dict1 = wordmap[0]
    dict2 = wordmap[1]
    
    ret_data = { 'working' : True,
                 'score' : score,
                 'dict1' : dict1,
                 'dict2' : dict2,
                 'allpaths' : allpaths
               }
    time.sleep(2)
    return JsonResponse(ret_data)

def process_wordhash(request):
    print 'CAME HERE *****************'
    Shelveopen('Hash#1.shelve')
    input_data = request.GET.get('label', None)
    print input_data

def process_synset(request):
    label = Unicode(request.GET.get('synset',None))
    hash2 = Shelveopen('Hash#2.shelve')
    synset = hash2[label]
    dic = {}
    if synset.definition():
        dic['definition'] = synset.definition()

    return JsonResponse(dic)

def log_reader(request):
    filename = request.GET.get('name', None)
    file_ = open(os.path.join(PROJECT_ROOT, Unicode(filename)))
    dic = {'data':file_.readlines()}
    return JsonResponse(dic)

def logs_page(request):
    return render(request, 'log.html', context=None)

def analyze_page(request):
    return render(request, 'analyze.html', context=None)

def patent_parser(request):
    patent1 = Unicode(request.GET.get('patent1',None))
    patent2 = Unicode(request.GET.get('patent2',None))
    patentpart = Unicode(request.GET.get('patentpart',None)).upper()
    doc1 = Patent(patent=patent1)
    doc2 = Patent(patent=patent2)
    dd = Documentclient(doc_1=doc1.getTemplate(patentpart),doc_2=doc2.getTemplate(patentpart))
    score = dd.getmetric()
    dic = {'score':score}
    return JsonResponse(dic)