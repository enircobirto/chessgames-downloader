from multiprocessing import Pool
from alive_progress import alive_bar
from itertools import repeat
from export import export

from get.pgn import pgn

def export_games(path,n,options,spaces):
    try:
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()
    except:
        gamelist = open("gamelist", "w", encoding='utf-8')
        gamelist.close()
        gamelist = open("gamelist", "r", encoding='utf-8').readlines()

    resultlist=[]
    with alive_bar(len(gamelist),title=f' > Writing games      {spaces}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(pgn,zip(gamelist,repeat(options))):
                if result!= '':
                    bar()
                    resultlist.append(result)
                else:
                    bar(skipped=True)
                    
    with alive_bar(len(resultlist),title=f' > Exporting to temp  {spaces}',bar='filling',spinner='classic') as bar:
        output = open("temp.pgn","a+",encoding='utf-8')
        for result in resultlist:
            output.write(result)
            output.write("<><>\n\n")
            bar()
        output.close()
        
    with alive_bar(title=f' > Exporting games to {path}',bar='filling',spinner='classic') as bar:
        output=open("temp.pgn","r",encoding='utf-8')
        lines=output.read().split('\n')
        output.close()
        nonemptylines=[line for line in lines if line.strip()!='']
        result=""
        for line in nonemptylines:
            result+=line+'\n'
        result = result.replace("<><>","\n\n")
        
        output=open("temp.pgn","w")
        output.write(result)
        output.close()
        
        export(path)

        gamelist = open("gamelist", "w", encoding='utf-8')
        gamelist.close()
        gamelist = open("temp.pgn", "w", encoding='utf-8')
        gamelist.close()
        bar()
