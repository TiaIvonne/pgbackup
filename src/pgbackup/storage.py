def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    outfile.open()

