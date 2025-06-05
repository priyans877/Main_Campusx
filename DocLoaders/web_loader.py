from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader , WebBaseLoader
from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

url = "https://www.flipkart.com/miral-enterprises-decorative-black-wallpaper/p/itmd7aba80dc84dc?pid=WLPGHR3QTCVUJVUQ&lid=LSTWLPGHR3QTCVUJVUQY6DGYH&marketplace=FLIPKART&q=vinyl+wrap+for+table&store=arb%2Fyod%2F8m7&srno=s_1_40&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&fm=search-autosuggest&iid=feba549e-d27e-4c82-88c7-bb2a5e9a2517.WLPGHR3QTCVUJVUQ.SEARCH&ppt=sp&ppn=sp&ssid=w7cryir6io0000001749123708605&qH=cd1ec017dbb2c1ae"

web_loader = WebBaseLoader(url)

data = web_loader.load()

prompt = PromptTemplate(
    template = "Answer the following question \n {question} from this text :- {text}",
    input_variables=["question", "text"],
)

parser = StrOutputParser()

chain = prompt | chatai | parser    

result = chain.invoke({"question": "What is the total reviews on this product", "text": data[0].page_content})

print(result)


