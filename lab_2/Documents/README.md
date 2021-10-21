Podczas obróbki danych obrano następujące cele:
- po pierwsze pozbyć się różnych seperatorów (I, S, czasami tylko spacje) dla łatwiejszego wczytywania
- po drugie przerobić dane tak, żeby jeden rekord był jednym dniem, a zmienne takie jak maksymalna/minimalna temperatura oraz opad w danym dniu znajdowały się w osobnych kolumnach

W tym celu najpierw użyto wyrażeń regularnych do edycji tekstu (usunięcie niechcianych seperatorów) a następnie przerobiono układ komórek w sposób zgodny z tidy-data (szczegóły w pliku tidying data w folderze Command Files)

Jedynym ostrzejszym krokiem było odcięcie ostatnich ~400 rekordów z powodu bardzo dużych braków w danych.

Bardzo możliwe że gdzieś jest błąd którego jeszcze nie zlokalizowano, chociaż bardzo możliwe że to jednak wybrakowanie danych powoduje tak wyraźne ubytki - kwestia do ponownej analizy. 

