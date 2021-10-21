from math import *
# koszt zużycia prądu przez wentylator o mocy 150W pracujący przez całą dobę 24h.
print("Moc wentylatora: 150W")
print("Czas pracy wentylatora: 24h")
print("Koszt zużytego prądu: %.2f zł"%(150./1E3*0.6*24.))
# --------------------------------------------------------
# Kapitał netto do inwestycji
kapitał=23e6*0.9;
print("\nKapitał do inwestycji: %.2f zł"%(kapitał));
# Utrata wartości przez kapitał po roku
inflacja=0.05;
utrata_wart_kapitału = kapitał*inflacja;
print("Utrata wartości przez kapitał w ciągu roku: %.2f zł"%(utrata_wart_kapitału ));
# Rzeczywista wartość kapitału po roku 
rze_wart_kaptiału = kapitał - utrata_wart_kapitału;
print("Rzeczywista wartość kapitału po roku: %.2f"%(rze_wart_kaptiału));
# Rzeczywista wartość odsetek po roku / pokazuje na m-ąc
rze_odsetki=(kapitał*0.01)*0.81*(1-inflacja);
print("Odsetki netto z uwzględnieniem inflacji: %.2f zł"%(rze_odsetki));
print("Odsetki netto na m-ąc z uwzględnieniem inflacji: %.2f zł"%(rze_odsetki/12.));
# Rzeczywista wartość kapitału wraz z odsetkami po roku
rze_kap_ods = rze_wart_kaptiału + rze_odsetki;
print("Rzeczywista wartość kapitału wraz z odsetkami po roku: %.2f"%(rze_kap_ods));
# Marża inflacyjna od kapitału po odliczeniu podatku Belki
marza_inflacyjna = kapitał*inflacja*0.81;
rze_marza_inflacyjna = marza_inflacyjna*(1-inflacja);
print("Marża inflacyjna z uwzględnieniem podatku Belki: %.2f"%(marza_inflacyjna));
print("Rzeczywista wartość marży inflacyjnej: %.2f"%(rze_marza_inflacyjna));
# Rzeczywista wartość kapitału wraz z odsetkami i marżą inflacyjną po roku
rze_kap_ods_marza = rze_wart_kaptiału + rze_odsetki + rze_marza_inflacyjna;
print("Rzeczywista wartość kapitału wraz z reczywistymi odsetkami i rzeczywistą marżą inflacyjną po roku: %.2f"%(rze_kap_ods_marza));
# Rzeczywiste oprocentowanie (marża odsetkowa + inflacja):
rze_oprocen = (rze_kap_ods_marza - kapitał)/kapitał*100.;
print("Rzeczywiste oprocentowanie kapitału w skali roku: %.5f%%"%(rze_oprocen));
