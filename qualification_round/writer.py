def write(solution, filename):
    with open(filename, 'w') as fo:
        fo.write(str(solution['num_libraries']) + '\n')
        libs = sorted(solution['libraries'], key=lambda k: k['signup_order'])
        for lib in libs:
            fo.write(str(lib['id'])+' '+str(lib['num_book']) + '\n')
            fo.write(' '.join(map(str, lib['books_order'])) + '\n')