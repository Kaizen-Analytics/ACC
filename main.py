
data_min=999
id_produtos=[]
id_produtos.append(produtos_ret[0].id)
id_ofs=[]

for i in range(1,len(produtos_ret)):
    if produtos_ret[i].data_prioridade<id_produtos[0]:
        data_min=produtos_ret[i].data_prioridade
        id_produtos.insert(0,produtos_ret[i].id)
        # passar para função
        if produtos_ret[i].vetor_ofs[0].id not in id_ofs:
            id_ofs.insert(0,produtos_ret[i].vetor_ofs[0].id)
    else:
        id_produtos.append(produtos_ret[i].id)
        #passar para função
        if produtos_ret[i].vetor_ofs[0].id not in id_ofs:
            id_ofs.append(produtos_ret[i].vetor_ofs[0].id)

id_maquina=1
n_ofs=len(id_ofs)
n_alocadas=0
n_refs=1
refs=[]
turno=0
temp_of=0

def get_last_of()
    return id_of

def alocar(n_alocadas,turno,)
    ofs[id_ofs[n_alocadas]].alocado = id_inicio_turno[turno]
    retificadora.capacidade_turno[id_inicio_turno[turno]] -= ofs[id_ofs[n_alocadas]].t_producao
    ofs[id_ofs[n_alocadas]].data_inicio = get_last_of().data_fim + get_setups(retificadora,ofs[id_ofs[n_alocadas]].dimensao) #falta ver slots!!!
    ofs[id_ofs[n_alocadas]].data_fim = ofs[id_ofs[n_alocadas]].data_inicio + ofs[id_ofs[n_alocadas]].t_producao

for n_refs in range(1,3):
    while n_alocadas<n_ofs:
        if retificadora.capacidade_turno[id_inicio_turno[turno]]-ofs[id_ofs[n_alocadas]].t_producao-get_setups(retificadora,ofs[id_ofs[n_alocadas]].dimensao>0:
            if (len(refs)=n_refs) and (ofs[id_ofs[n_alocadas]].dimensao in refs):
                alocar(of)
                n_alocadas += 1
            elif ofs[id_ofs[n_alocadas]].dimensao not in refs and len(refs)<n_refs:
                refs.append(ofs[id_ofs[n_alocadas]].dimensao)
                alocar(of)
                n_alocadas += 1
        else:
            turno+=1





