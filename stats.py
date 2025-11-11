def get_book_text(filepath):
  # returns file content
  with open(filepath) as f:
    content = f.read()
  return content

def get_num_words(book_path):
  # returns words count
  num_words = len(get_book_text(book_path).split())
  return num_words


def get_num_chars(book_path):
  # returns simple dictionary counting letters frequency
  result = {}
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
    # fill the list with two-elements dictionary on each iteration
    d_inner = {}
    d_inner["char"] = el
    d_inner["num"] = dict[el]
    result.append(d_inner)
  
  result.sort(reverse=True, key=sort_on)
  return result

# below is helper function determines key for sorting
def sort_on(items):
  return items["num"]

