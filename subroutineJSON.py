import json
import git
import os

from datetime import datetime

def getDateTimeString():
    now = datetime.now()
    return now.strftime("%d_%m_%H_%M")

def retriveJSONOptions(filename,options,results):
    JsonOptions = {
        'commit': None,
        'file': filename,
        'options': options,
        'results_tot': results,
        'description': None,
        'varianti': checkVarianti(options)
    }
    return JsonOptions

def checkVarianti(opt):
    varianti = []
    if len(opt['molecule']['basis']) > 1:
        varianti.append('base')
    if len(opt['varforms']) > 1:
        varianti.append('varform')
    if len(opt['quantum_instance']) > 1:
        varianti.append('quantum_instance')
    if len(opt['optimizer']) > 1:
        varianti.append('optimizer')
    if len(opt['lagrange']['active']) > 1:
        varianti.append('lagrange activity')
    if len(opt['lagrange']['operators']) > 1:
        varianti.append('lagrange operator')
    return varianti

def writeJson(JsonOptions):
    filename = "data/exp_"+getDateTimeString()
    repo = git.Repo(search_parent_directories=True)
    commit = repo.head.object.hexsha
    JsonOptions['commit'] = commit

    description = input("Inserisci una minima descrizione: ")
    JsonOptions['description'] = description

    json_obj = json.dumps(JsonOptions, indent = 4)

    while os.path.exists(filename):
        print('Esiste già un file con questo nome!!')
        filename = input('Inserisci un nuovo nome: ')

    with open(filename, "w") as out:
        out.write(json_obj)
