# create a library class
# display books
# lend books
# add books
# return book
#
# harrylibrary = library(listofbooks, libraryname)
#
# dictionary = (books-name o person)
#
# create a main function and run infinite times while loop asking users for theri input
#
def minion_game(string):
    # your code goes here
    vowel = 'aeiou'.upper()
    strl = len(string)
    kevin = sum(strl-i for i in range(strl) if string[i] in vowel)
    stuart = strl*(strl + 1)/2 - kevin

    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)
if __name__ == '__main__':
    s = input()
    minion_game(s)
