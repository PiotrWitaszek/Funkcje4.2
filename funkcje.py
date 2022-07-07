def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
  s = "potop"
  ans = is_palindrome(s)

  if ans:
    print("Yes")
  else:
    print("No")


