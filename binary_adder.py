# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


binary = [1,1,1,1]
end = False
val= 0
while not end:
    print('Press \'N\' to quit')
    if not val:
        val = input('Enter number: ')
        try:
            val = int(val)
        except:
            if val == 'N':
                end = True
            else:
                print('Invalid input.')
                val=0
                continue
    val -= 1
    if sum(binary) == len(binary):
        binary.insert(0,1)
        for i in range(1,len(binary)):
            binary[i] = 0
    else:
        last_0 = ''.join([str(x) for x in binary]).rfind('0')
        binary[last_0] = 1
        for i in range(last_0 + 1,len(binary)):
            binary[i] = 0
    print(binary)