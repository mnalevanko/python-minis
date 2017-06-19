class IP_iterator(object):
  '''Creates in IP address iterator.'''
  
  def __init__(self, start='0.0.0.0', end='255.255.255.255', step=1):
    self.start = start
    self.start_num = self.from_IP_to_num(self.start)
    self.end = end
    self.end_num = self.from_IP_to_num(self.end)
    self.step = step
    self.current_IP_num = self.from_IP_to_num(self.start)
  
  def from_IP_to_num(self, IP_str):
    '''Converts an IP address from string format to an integer.'''
    
    pole = IP_str.split('.')
    value = 0
    len_pole = len(pole)
    
    for idx, item in enumerate(pole):
      value += 256**(len_pole - 1 - idx) * int(item)
    return value
  
  def from_num_to_IP(self, num):
    
    num_1 = num // 256**3
    num -= num_1 * 256**3
    num_2 = num // 256**2
    num -= num_2 * 256**2
    num_3 = num // 256
    num_4 = num - num_3 * 256
    return '{}.{}.{}.{}'.format(num_1, num_2, num_3, num_4)
    
  def __iter__(self):
    self.current_IP_num = self.from_IP_to_num(self.start)
    return self
    
  
  def __next__(self):
    result = self.from_num_to_IP(self.current_IP_num)
    
    if self.from_IP_to_num(result) > self.from_IP_to_num(self.end):
      raise StopIteration
      
    self.current_IP_num += self.step
    
    return result
    
  next = __next__
  
ip = IP_iterator()

for item in ip:
  print(item)

    
