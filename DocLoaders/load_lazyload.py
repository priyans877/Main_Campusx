from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader , TextLoader
from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Directory Based loader
data_load = DirectoryLoader(
    path = "books",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

# data = data_load.load()

# #Load , Collect All data once then give ontput at end 
# for document in data:
#     print(document.metadata)
    
#Lazy Load , It give contumnous output while laoding item documents one by one each iteration
lazy = data_load.lazy_load()

for doc in lazy:
    print(doc.metadata)