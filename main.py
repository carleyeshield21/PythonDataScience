# word = 'cool'
# list = [letter for letter in word[1:len(word)]]
# join = ''.join(list)
# first_letter = word[0]
# new_word = join + first_letter + 'ay'

# ph = ('Pig latin is cool')
# ph = ('This is my string')
# ph = ph.split()
#
# arr = []
# for n in ph:
#     arr.append(n.replace(n[0],'')+n[0]+'ay')
# print(' '.join(arr))

def pig_it(text):
    ph = text.split()

    arr = []
    for n in ph:
        arr.append(n.replace(n[0],'') + n[0] + 'ay')
    # print(' '.join(arr))
    print(str(' '.join(arr)))
    return arr

pig_it('This is my string')
pig_it('Pig latin is cool')

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
