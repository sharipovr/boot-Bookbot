from stats import get_num_words, get_num_chars, get_list_of_dicts
import sys

def main():

  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path = sys.argv[1]

  num_words = get_num_words(path)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  dic = get_num_chars(path)

  # return sorted (desc) list of dictionaries
  list_of_dics = get_list_of_dicts(dic)

  for el in list_of_dics:
    if el["char"].isalpha():
      print(f"{el["char"]}: {el["num"]}")

main()