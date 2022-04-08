from pandas import to_datetime
from textblob import TextBlob
int=TextBlob("Tinkle est un magazine bimensuel indien pour enfants, publié principalement en Inde. Détenue à l'origine par India Book House, la marque Tinkle a été acquise par ACK Media en 2007.")
print(int.translate(to="en"))
module=TextBlob("he Pilgrim’s Progress by John Bunyan (1678). A story of a man in search of truth told with the simple clarity and Robinson Crusoe by Daniel Defoe (1719)")
print(module.translate(to="es"))