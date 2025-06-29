def concatenate_wow(*input_strings):
  """
  Concatenates "WOW!" to each input string and then concatenates them together.

  Args:
    *input_strings: A variable number of strings.

  Returns:
    The concatenated string with "WOW!" appended to each input string.
  """
  modified_strings = [s + "WOW!" for s in input_strings]
  return "".join(modified_strings)
