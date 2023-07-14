from LLM_Ranked_Retriever import get_retrieved_nodes
from LLM_Text_Summerizer import generate_summary_chat
from LLM_Index_Loader import load_index
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# load index
index = load_index()

print("\n************************\n\n")
query = "What are the correct codes to enter into GCSS-Army for reported equipment faults in the context of material maintenance?"
print(query)
nodes = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes)
for summary in summaries:
    print("\n************************\n")
    print(summary)

print("\n************************\n\n")
query = "Hi!"
print(query)
nodes = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes)
for summary in summaries:
    print("\n************************\n")
    print(summary)


print("\n************************\n\n")
query = "Tell me a story!"
print(query)
nodes = get_retrieved_nodes(index, query, vector_top_k=1)
summaries = generate_summary_chat(nodes)
for summary in summaries:
    print("\n************************\n")
    print(summary)


query = "What are the time constraints for processing a flipl?"

nodes = get_retrieved_nodes(index, query, vector_top_k=1)
for node in nodes:
    print(node.extra_info["regulation"])
    print(node.extra_info["section_number"])
    print(node.extra_info["section_name"])


'''
print("************************\n")
print(nodes[0].score)
print(nodes[0].source_text)
print("************************\n")
print(nodes[1].score)
print(nodes[1].source_text)
print("************************\n")
print(nodes[2].score)
print(nodes[2].source_text)
'''

print("\n************************\n\n")
print(query)
summaries = generate_summary_chat(nodes)
first_summary = summaries[0].response
for summary in summaries:
    print("\n************************\n")
    print(summary)


print("\n************************\n\n")
query = "What happens to an officer that is dismissed due to a court martial?"
print(query)
nodes = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes)
for summary in summaries:
    print("\n************************\n")
    print(summary)

'''
print("************************\n")
print(nodes[0].score)
print(nodes[0].source_text)
print("************************\n")
print(nodes[1].score)
print(nodes[1].source_text)
print("************************\n")
print(nodes[2].score)
print(nodes[2].source_text)
'''

print("\n************************\n\n")
query = "What occurs when I file a complaint against an FCC provider?"
print(query)
nodes = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes)
for summary in summaries:
    print("\n************************\n")
    print(summary)
