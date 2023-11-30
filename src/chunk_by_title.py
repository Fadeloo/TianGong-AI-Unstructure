from unstructured.chunking.title import chunk_by_title
from unstructured.partition.auto import partition
from unstructured.partition.docx import partition_docx

file_name = "water/book2-1-5.docx"

elements = partition_docx(
    filename=file_name,
    multipage_sections=True,
    infer_table_structure=True,
    include_page_breaks=False,
)


chunks = chunk_by_title(
    elements=elements,
    multipage_sections=True,
    combine_text_under_n_chars=0,
    new_after_n_chars=None,
    max_characters=4096,
)

for chunk in chunks:
    print(chunk)
    print("\n\n" + "-" * 80)
    input()
