for i in range(100):
    with open(f'file{i}.ggbro', 'wb') as out:
        out.seek(1073741824-1)
        out.write(b'\0')
        out.close()
    print(f"{i} file created!")
    
