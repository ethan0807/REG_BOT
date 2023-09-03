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
query = "What are the basic steps for processing a flipl?"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)

print("************************\n")
print(nodes_with_score[0].score)
print(nodes_with_score[0].node.text)
print("************************\n")
print(nodes_with_score[1].score)
print(nodes_with_score[1].node.text)
print("************************\n")
print(nodes_with_score[2].score)
print(nodes_with_score[2].node.text)


print("\n************************\n\n")
query = "How much time does the Approving Authority have to sign the DD200?"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)

print("************************\n")
print(nodes_with_score[0].score)
print(nodes_with_score[0].node.text)
print("************************\n")
print(nodes_with_score[1].score)
print(nodes_with_score[1].node.text)
print("************************\n")
print(nodes_with_score[2].score)
print(nodes_with_score[2].node.text)



print("\n************************\n\n")
query = "What are the correct codes to enter into GCSS-Army for reported equipment faults in the context of material maintenance?"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)

print("\n************************\n\n")
query = "Hi!"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)


print("\n************************\n\n")
query = "Tell me a story!"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=1)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)


query = "What are the time constraints for processing a flipl?"

nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=1)
for node_with_score in nodes_with_score:
    print(node_with_score.node.metadata["regulation"])
    print(node_with_score.node.metadata["section_number"])
    print(node_with_score.node.metadata["section_name"])


'''
print("************************\n")
print(nodes[0].score)
print(nodes[0].node_with_score.text)
print("************************\n")
print(nodes[1].score)
print(nodes[1].node_with_score.text)
print("************************\n")
print(nodes[2].score)
print(nodes[2].node_with_score.text)
'''

print("\n************************\n\n")
print(query)
summaries = generate_summary_chat(nodes_with_score)
first_summary = summaries[0].response
for summary in summaries:
    print("\n************************\n")
    print(summary)


print("\n************************\n\n")
query = "What happens to an officer that is dismissed due to a court martial?"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)

'''
print("************************\n")
print(nodes[0].score)
print(nodes[0].node_with_score.text)
print("************************\n")
print(nodes[1].score)
print(nodes[1].node_with_score.text)
print("************************\n")
print(nodes[2].score)
print(nodes[2].node_with_score.text)
'''

print("\n************************\n\n")
query = "What occurs when I file a complaint against an FCC provider?"
print(query)
nodes_with_score = get_retrieved_nodes(index, query, vector_top_k=3)
summaries = generate_summary_chat(nodes_with_score)
for summary in summaries:
    print("\n************************\n")
    print(summary)
