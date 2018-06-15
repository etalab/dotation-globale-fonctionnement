#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datapackage import Package

pkg = Package()
pkg.infer('2014.csv')
pkg.infer('2015.csv')
pkg.infer('2016.csv')
pkg.infer('2017.csv')
for r in range(0,len(pkg.descriptor['resources'])):
    pkg.descriptor['resources'][r]['schema']['fields'][0]['title'] = 'Code INSEE de la commune'
    pkg.descriptor['resources'][r]['schema']['fields'][0]['type'] = 'string'
    pkg.descriptor['resources'][r]['schema']['fields'][0]['constraints'] = [dict(required=True,
                                                                                 unique=True,
                                                                                 pattern='[0-9][0-9A-B][0-9]{3}')
                                                                           ]
    pkg.descriptor['resources'][r]['schema']['fields'][1]['title'] = 'Nom de la commune'
    pkg.descriptor['resources'][r]['schema']['fields'][1]['constraints'] = [dict(required=True,
                                                                                 maxLength=45,
                                                                                 minLength=1)]

    pkg.descriptor['resources'][r]['schema']['fields'][2]['title'] = 'dotation forfaitaire (DF)'
    pkg.descriptor['resources'][r]['schema']['fields'][3]['title'] = 'dotation élu local (DPEL)'
    pkg.descriptor['resources'][r]['schema']['fields'][4]['title'] = 'dotation de solidarité urbaine et de cohésion sociale (DSU)'
    pkg.descriptor['resources'][r]['schema']['fields'][5]['title'] = 'dotation de solidarité rurale "bourg centre" (DSR BC)'
    pkg.descriptor['resources'][r]['schema']['fields'][6]['title'] = 'dotation de solidarité rurale "péréquation" (DSR P)'
    pkg.descriptor['resources'][r]['schema']['fields'][7]['title'] = 'dotation nationale de péréquation (DNP)'
    pkg.descriptor['resources'][r]['schema']['fields'][8]['title'] = "dotation d'aménagement des communes d'outre-mer (DACOM)'"
    pkg.descriptor['resources'][r]['schema']['fields'][9]['title'] = 'dotation de solidarité rurale "cible" (DSR C)'
    pkg.descriptor['resources'][r]['schema']['fields'][10]['title'] = 'Prélèvement de la commune isolée'
    pkg.descriptor['resources'][r]['schema']['fields'][11]['title'] = 'Versement FPIC au profit de la commune isolée'
    pkg.descriptor['resources'][r]['schema']['fields'][12]['title'] = 'Solde FPIC de la commune isolée'
    pkg.descriptor['resources'][r]['schema']['fields'][13]['title'] = 'Prélèvement FSRIF de la commune'
    pkg.descriptor['resources'][r]['schema']['fields'][14]['title'] = 'Versement FSRIF de la commune'
    pkg.descriptor['resources'][r]['schema']['fields'][15]['title'] = 'Solde FSRIF de la commune'

    for c in range(2,16):
        pkg.descriptor['resources'][r]['schema']['fields'][c]['type'] = 'integer'

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
pkg.save('datapackage.json')
