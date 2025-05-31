import ast
import datasets

# def process_ast(string):
#     return ast.literal_eval(string)


# def last_problem(doc):
#     problem = {'question':doc['question'], 
#                    'answer':doc['answer'], 
#                    'options':doc['options']}
#     return problem


def get_answer_option(problem):
    letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3}
    answer = letter_to_num[problem["answer"]]
    return problem["options"][answer]

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        # print(len(doc['answer']))
        # print(len(doc['article']))
        return doc

    return dataset.map(_process_doc)


def doc_to_choice(doc):
    # print("doc_to_choice")
    choices = [doc["options"][i] for i in range(4)]
    return choices


def doc_to_text(doc):
    text = "Article: " + doc["article"] + "\n\n"
    # print(type(doc))
    # print(dict_len)
    # print(doc["article"])
    # print(doc.keys())
    # print(len(doc['answer']))
    # print(len(ast.literal_eval(doc['example_id'])))
    # for idx in range(dict_len-1):
    problem = {'question':doc['question'], 
                'answer':doc['answer'], 
                'options':doc['options']}
    if problem["question"][-6:] == "  _  .":
        text += problem["question"][-5:] + get_answer_option(problem) + "\n"
    else:
        question = "Question: " + problem["question"] + "\n"
        # answer = "Answer: " + get_answer_option(problem) + "\n"
        text += question
    # text += last_problem(doc)["question"]
    return text


def doc_to_target(doc):
    # print("doc_to_target")
    letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3}
    answer = letter_to_num[doc["answer"]]
    return answer