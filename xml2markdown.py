import xml.dom.minidom as md

VERSION = "ACF"

def write2File(versicules, nomeDoArquivo):
    f = open(nomeDoArquivo, "w")

    f.write("## " +  str(nomeDoArquivo) + '\n')

    i = 1
    for versicule in versicules:
        f.write("### v" + str(i) + "\n " + versicule.firstChild.nodeValue + "\n")
        i +=1
    f.close()

def main():
    file = md.parse( VERSION + ".xml" )
    books = file.getElementsByTagName( "book" )
  
    for book in books:
        chapters = book.getElementsByTagName("c")
        i = 1
        for chapter in chapters:
            versicules = chapter.getElementsByTagName("v")
            
            titulo = VERSION+ "/" + VERSION+ "-" + str(book.getAttribute("name"))  + " " + str(i) + ".md" 
            write2File(versicules, titulo)
            i +=1

if __name__=="__main__":
    main()
