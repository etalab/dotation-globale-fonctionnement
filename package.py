from datapackage import Package

pkg = Package()
pkg.infer('2014.csv')
pkg.infer('2015.csv')
pkg.infer('2016.csv')
pkg.infer('2017.csv')
for r in range(0,len(pkg.descriptor['resources'])):
    pkg.descriptor['resources'][r]['schema']['fields'][0]['type'] = 'string'
    for c in range(3,17):
        pkg.descriptor['resources'][r]['schema']['fields'][c-1]['type'] = 'integer'

pkg.descriptor['name'] = 'Dotations Globales de Fonctionnement'
pkg.descriptor['homepage'] = 'http://www.dotations-dgcl.interieur.gouv.fr/'
pkg.descriptor['created'] = '2018-03-16'

pkg.descriptor['licences'] = [dict(name='LO-2.0',
                                   title='Licence Ouverte 2.0',
                                   path='https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf')]

pkg.descriptor['sources'] = [dict(title='DGCL',
                                  path='http://www.dotations-dgcl.interieur.gouv.fr/')]

pkg.descriptor['contributors'] = [dict(title='Christian Quest',
                                       email='christian.quest@data.gouv.fr')]

pkg.descriptor['temporal'] = dict(start='2014-01-01', end='2017-12-31')
pkg.commit()
if pkg.valid:
    pkg.save('datapackage.json')
else:
    print('error')