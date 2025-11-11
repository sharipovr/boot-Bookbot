def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
  return content

def get_num_words():
  book_path = "books/frankenstein.txt"
  num_words = len(get_book_text(book_path).split())
  return num_words


def get_num_chars():
  result = {}
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path).lower()
  for char in text:
    if char in result:
      result[char] += 1
    else:
      result[char] = 1
  return result


def get_list_of_dicts(dict):
  result = []
  for el in dict:
    d_inner = {}
    d_inner["char"] = el
    d_inner["num"] = dict[el]
    result.append(d_inner)
  
  result.sort(reverse=True, key=sort_on)
  return result

def sort_on(items):
  return items["num"]

