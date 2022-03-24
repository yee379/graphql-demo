from mongoengine import connect, disconnect

from iris.models import User, Facility, Repo

import logging
logging.basicConfig(level=logging.DEBUG)


def load_data( tsv, array_fields=[] ):
    header = None
    with open( tsv ) as data:
        for l in data.readlines():
            l = l.strip()
            if l.startswith('#') and header == None:
                header = l.split('\t')
                header[0] = header[0].replace('#','')
                logging.info(f"header: {header}")
            else:
                items = {}
                for i,v in enumerate(l.split('\t')):
                    items[header[i]] = v
                    if header[i] in array_fields:
                        items[header[i]] = v.split(',')
                logging.info(f"data: {items}")
                yield items


def push( klass, filepath, array_fields=[] ):
    for item in load_data( filepath, array_fields=array_fields ):
        i = klass( **item )
        i.save()

if __name__ == "__main__":
    connect('new-iris')

    User.drop_collection()
    push( User, 'users.tsv', array_fields=('eppns',) )

    Repo.drop_collection()
    push( Repo, 'repos.tsv', array_fields=('leaders','users') )

    Facility.drop_collection()
    push( Facility, 'facilities.tsv' )

    disconnect()
