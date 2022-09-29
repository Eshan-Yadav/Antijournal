from ast import Break
from calendar import c 
from matplotlib.pyplot import vlines
from openpyxl import Workbook
from bs4 import BeautifulSoup
import openpyxl

paths=[r'C:\sem 4\Biological DB\Data\Uniprot\uniprot-antigen-filtered-organism__Bos+taurus+(Bovine)+[9913]_+AND--.xlsx',r'C:\sem 4\Biological DB\Data\Uniprot\uniprot-antigen-filtered-organism__Homo+sapiens+(Human)+[9606]_+AN--.xlsx',r'C:\sem 4\Biological DB\Data\Uniprot\uniprot-antigen-filtered-organism__Mus+musculus+(Mouse)+[10090]_+A--.xlsx',r'C:\sem 4\Biological DB\Data\Uniprot\uniprot-antigen-filtered-organism__Rattus+norvegicus+(Rat)+[10116]%2--.xlsx',r'C:\sem 4\Biological DB\Data\Uniprot\uniprot-antigen-filtered-organism__Saccharomyces+cerevisiae+(strain+ATCC+2--.xlsx']
path_count=1
for path in paths:
    wb=openpyxl.load_workbook(path)
    sheet = wb.active

    #Track the cells
    cells=["A","B","C","D","E","F","G"]
    count=2

    #insert values
    values_table=[]

    #To break the while loop
    break_loop=False
    while(True):
        if(break_loop):
            break
        entry=""
        #each row
        temp_row=[]
        for cell_alpha in cells:
            if(cell_alpha=="A"):
                if(sheet[cell_alpha+str(count)].value):
                    if cell_alpha=="G":
                        entry+="'"+str(sheet[cell_alpha+str(count)].value)+"'"
                    else:  
                        entry+="'"+str(sheet[cell_alpha+str(count)].value)+"',"
        
                else:
                    break_loop=True
                    break
            else:
                if(sheet[cell_alpha+str(count)].value):
                    if cell_alpha=="G":
                        entry+="\""+str(sheet[cell_alpha+str(count)].value)+"\""
                    else:  
                        entry+="\""+str(sheet[cell_alpha+str(count)].value)+"\","
                else:
                    if cell_alpha=="G":
                        entry+="\""+"\""
                    else:  
                        entry+="\""+"\","
        if(entry!=""):  
            entry="("+entry+",\"https://www.uniprot.org/uniprot/"+str(sheet["A"+str(count)].value)+"\""+")"
            temp_row.append(entry)
            values_table.append(entry)
        count+=1

    with open("File"+str(path_count)+".txt",'w',encoding = 'utf-8') as f:
        for i in values_table:
            if i==values_table[len(values_table)-1]:
                f.write(i+';')
                f.write('\n')
            else:
                f.write(i+',')
                f.write('\n')
    path_count+=1
    # print(values_table)


            
    # if(sheet['H1'].value):  
    #     print(sheet['H1'].value)
    # else:
    #     print("The cell is empty")

    """
    INSERT INTO 'TABLE_NAME' ('UniProt_ID','Entry_Name','status','Protein_Name','Gene_Name','Organism','Seq_Length','uniprotLink') VALUES

    """
