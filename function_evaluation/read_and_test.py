import os
import sys
from importlib.util import (spec_from_file_location,
                            module_from_spec)
from pre_setted_tests import main_test

origin_path = os.getcwd()
path = os.path.join(origin_path,'student_module')
lista_de_arquivos = os.listdir(path)
lista_de_arquivos.remove('__pycache__')
lista_de_arquivos.remove('reports')

def report_extract(module,path):
    path = path.replace('.py','')
    path = path+'.txt' 
    with open(path,'w') as output:
        score, reasons = main_test(module)
        output.write('\n'+str(score))
        output.write('\n'+str(reasons))
    return None
    

def read_module_arquive(path,nome_arquivo):
    full_path = os.path.join(path,nome_arquivo)
    spec = spec_from_file_location('student_module',full_path)
    student_module = module_from_spec(spec)
    spec.loader.exec_module(student_module)
    return student_module 

def failed_report_extract(error,path):
    path = path.replace('.py','')
    path = path+'.txt' 
    with open(path,'w') as output:
        output.write(os.path.basename(path).replace('.txt',''))
        score, reasons = 0,str(error)
        output.write('\n'+str(score))
        output.write('\n'+str(reasons))
    return None

if __name__ == "__main__":
    for nome_arquivo in lista_de_arquivos:
        report_output_path = os.path.join(path,'reports',str(nome_arquivo)+'.txt')
        try:
            student_module = read_module_arquive(path,nome_arquivo)
            report_extract(student_module,report_output_path)
        except Exception as error:
            failed_report_extract(error,report_output_path)
        continue


