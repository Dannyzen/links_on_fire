from google.cloud import firestore

db = firestore.Client()


def get_url_from_query(slug):
    """An end user sends a url ex: dannyrosen.net/word where 'word' is a slug. The app queries the link collection for the document containing the slug and returns the url"""
    links = db.collection(u'links')
    query_ref = links.where(u'slug', u'==', slug).get()
    for item in query_ref:
        return item._data['url']

a = get_url_from_query('chickens')
print(a)
