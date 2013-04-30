def dig_root_recursive(n):
  return n if n < 10 else dig_root_recursive(sum([int(i) for i in str(n)]));

print dig_root_recursive(31337);

print dig_root_recursive(1073741824);
