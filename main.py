from stats import get_num_words, get_num_chars, get_list_of_dicts

def main():
  num_words = get_num_words()
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  dic = get_num_chars()
  result = get_list_of_dicts(dic)

  for el in result:
    if el["char"].isalpha():
      print(f"{el["char"]}: {el["num"]}")

main()