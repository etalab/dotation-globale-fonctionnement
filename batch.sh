# téléchargement des fichiers CSV
for a in `seq 2014 2017`
do
  for c in 02 05 12 13 14 16 15 18 19 20 21 22 23 24
  do
    echo "Download $a-$c"
    curl -s "http://www.dotations-dgcl.interieur.gouv.fr/consultation/dotation_communes.php?annee=$a&dot=c$c" > dgf-$a-$c.csv
  done
  mv dgf-$a-05.csv dgf-$a-00.csv
  mv dgf-$a-02.csv dgf-$a-10.csv
done

# remise en CSV, utf8, sur 2 colonnes
rm -f clean*
for c in dgf-*-1*.csv dgf-*-2*.csv
do
  echo "clean_$c"
  iconv -f iso8859-1 -t utf8 $c | sed 's!,!!;s! - \([^0-9]\)!,\1!;s!\t!,!;s!\(^[^0-9].*\)!depcom,commune,\1!;s!\([0-9]\) \([0-9]\)!\1\2!g' | csvcut -C 2 > clean_$c
done
for c in dgf-*-00.csv
do
  echo "clean_$c"
  iconv -f iso8859-1 -t utf8 $c | sed 's!,!!;s! - \([^0-9]\)!,\1!;s!\t!,!;s!\(^[^0-9].*\)!depcom,commune,\1!;s!\([0-9]\) \([0-9]\)!\1\2!g' > clean_$c
done

# agrégation des colonnes par année et renommage des colonnes
for a in `seq 2014 2017`
do
  csvjoin -c 1 --left clean_dgf-$a-*.csv | sed 's!depcom,commune.*$!depcom,commune,dotation_forfaitaire,dotation_elu_local,dsu,dsr_bc,dsr_p,dnp,dacom,dsr_c,fpic_prelevement,fpic_versement,fpic_solde,fsrif_prelevement,fsrif_versement,fsrid_solde!' > $a.csv
done
