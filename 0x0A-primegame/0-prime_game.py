#!/usr/bin/python3
"""
find Prime Game winner
"""


def checkwin(maria, ben):
  """checkwin"""

  if maria > ben:
    return ("Maria")
  elif maria == ben:
    return None
  else:
    return "Ben"

def checkmultiples(x, nums=[]):
  """checkmultiples"""

  nonmultiples = []
  for i in range(len(nums)):
    if (nums[i] % x) != 0:
      nonmultiples.append(nums[i])
  return nonmultiples

def checkprimenum(num):
  """checkprim"""

  if num > 1:
    for i in range(2, int(num / 2) + 1):
      if (num % i) == 0:
        return False
      else:
        return True
  else:
    return False

def chepriinlist(nums = []):
  """checkprimlist"""

  for i in nums:
    if checkprimenum(i):
      return True
  return False

def createlist(num):
  """createlist"""

  list = [i for i in range(1, num + 1)]
  return list

def check(num):
  """check"""

  if ((num % 2) == 0):
    return True
  else:
    return False
  
def isWinner(x, nums) :
  """findwinner"""

  prgreassion = 0
  Maria = 0
  Ben = 0
  for i in range(0,x):
    n_list = createlist(nums[i])
    for i in range(0, nums[i]):
      if chepriinlist(n_list):
        prgreassion += 1
        for con_int in n_list:
          if checkprimenum(con_int):
            n_list = checkmultiples(con_int, n_list)
            break
      else:
        if check(prgreassion):
          Ben += 1
        else:
          Maria += 1
        prgreassion = 0
        break
  return(checkwin(Maria, Ben))
