
from multiprocessing import Pool
from alive_progress import alive_bar

from get.from_page import from_page


def get_page_list(info,spaces,n):
    pagelist=[]
    for i in info:
        for num in range(1,i['max']+1):
            pagelist.append(dict({
                'player':i['player'],
                'pid':i['pid'],
                'page':num
            }))

    with alive_bar(len(pagelist),title=f' > Extracting pages   {spaces}',bar='filling',spinner='classic') as bar:
        with Pool(n) as pool:
            for result in pool.imap_unordered(from_page,pagelist):
                bar()