#Select Model Function

# https://www.sbert.net/docs/pretrained_models.html

#250MB, multi-qa-distilbert-cos-v1',  Max Sequence Length:	512, Dimensions:768, Normalized Embeddings:	true
#80MB, all-MiniLM-L6-v2, Max Sequence Length:	256, Dimensions:	384, Normalized Embeddings:	true
#290MB, all-distilroberta-v1, Max Sequence Length:	512, Dimensions:	768, Normalized Embeddings:	true
#420MB, all-mpnet-base-v2, Max Sequence Length:	384, Dimensions:	768, Normalized Embeddings:	true
#1.36GB, all-roberta-large-v1, Max Sequence Length:	256, Dimensions: 1024, Normalized Embeddings:	true

def select_embmodel(num, verbose=True):
    emb_modelshortlist = ['distilbert','minilm','distilroberta','mpnet','roberta']

    emb_modellist = ['multi-qa-distilbert-cos-v1',
                'all-MiniLM-L6-v2',
                'all-distilroberta-v1',
                'multi-qa-mpnet-base-dot-v1',
                'all-roberta-large-v1']

    embmodelname = emb_modellist[num]
    embmodelshort = emb_modelshortlist[num]
    embmodelname1 = "_" + embmodelname
    if verbose:
        print (embmodelname,'\t',embmodelshort,'\t', embmodelname1)
        
    return embmodelname, embmodelshort, embmodelname1