from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader , TextLoader
from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Directory Based loader
data = DirectoryLoader(
    path = "books",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

data = data.load()

print(len(data))

