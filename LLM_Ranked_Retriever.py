from llama_index.retrievers import VectorIndexRetriever
from llama_index.indices.query.schema import QueryBundle

# Gets the top k nodes from the index for a given query

def get_retrieved_nodes(index, query_str, vector_top_k=10):
    query_bundle = QueryBundle(query_str)
    # configure retriever
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=vector_top_k,
        temperature=0.0
    )
    nodes = retriever.retrieve(query_bundle)

    return nodes
