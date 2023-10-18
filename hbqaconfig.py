

apipath = r'/content/drive/MyDrive/config/hbqa-colab.txt'
apipath = r'H:\My Drive\config\hbqa.txt'
import configparser

config = configparser.ConfigParser()
config.read(apipath)

OPENAI_KEY = config['global']['OPENAI_KEY']
PINECONE_API_KEY = config['global']['PINECONE_KEY']
PINECONE_ENV = config['global']['PINECONE_ENV']
CHATPDF_KEY = config['global']['CHATPDF_KEY']
DATA_FOLDER =  config['global']['DATA_FOLDER']
PE_FOLDER = config['global']['PE_FOLDER']
QAGS_FOLDER = config['global']['QAGS_FOLDER']
DRS_FOLDER = config['global']['DRS_FOLDER']
AGS_FOLDER = config['global']['AGS_FOLDER']
REPORT_FOLDER =  config['global']['REPORT_FOLDER']
CORPUS_SECTIONS_FOLDER =  config['global']['CORPUS_SECTIONS_FOLDER']
CORPUS_CHAPTER_FOLDER =  config['global']['CORPUS_CHAPTER_FOLDER']