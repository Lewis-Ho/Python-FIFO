"""
  Implement a basic FIFO queue that provides the ability to add and remove values.
  
"""

def remove_value(arr):
  """ Remove value from array """

  if (len(arr) < 1):
    print('ERROR! Can\'t remove value from empty queue')
    return
  
  arr.pop(0)
  print('Current FIFO queue:')
  print(arr)


def add_value(arr):
  """ Add value from array """
  
  value = input('Please enter the value to add')
  arr.insert(0,value)
  print('Current FIFO queue:')
  print(arr)


def main():
  """ Take command from console """

  array = []
  command = input('Please enter one of the commands: (a)add, (r)remove or (q)quit.')
  print ('You entered command: ' + command)

  while (command):
    if (command == 'q'):
      return
    elif (command == 'a'):
      add_value(array)
    elif (command == 'r'):
      remove_value(array)
    else:
      print ('Input Invalid.')
      
    command = input('Please enter one of the commands: (a)add, (r)remove or (q)quit.')


if __name__ == '__main__':
    main()
