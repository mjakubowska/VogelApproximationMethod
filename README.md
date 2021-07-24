This terminal app minimalizes costs of vaccine purchase and ensures the supply to all pharmacies. The program should provide the most cost-effective for all pharmacies configuration.

# Input data
The input .txt file should consist of information about:
* Vaccine Manufacturers
    * manufacturer's id
    * name
    * daily production
* Pharmacies
    * pharmacy's id
    * name
    * daily demand
* Connections between manufacturers and pharmacies
    * manufacturer's id
    * pharmacy's id
    * max daily amount of provided vaccines
    * cost of one vaccine
    
Example of input file:
```
# Producenci szczepionek (id | nazwa | dzienna produkcja) 0 | BioTech 2.0 | 900
1 | Eko Polska 2020 | 1300
2 | Post-Covid Sp. z o.o. | 1100
# Apteki (id | nazwa | dzienne zapotrzebowanie) 0 | CentMedEko Centrala | 450
1 | CentMedEko 24h | 690
2 | CentMedEko Nowogrodzka | 1200
# Połączenia producentów i aptek (id producenta | id apteki | dzienna maksymalna liczba dostarczanych szczepionek | koszt szczepionki [zł] )
0 | 0 | 800 | 70.5
0 | 1 | 600 | 70
0 | 2 | 750 | 90.99
1 | 0 | 900 | 100 
1 | 1 | 600 | 80
1 | 2 | 450 | 70
2 | 0 | 900 | 80 
2 | 1 | 900 | 90 
2 | 2 | 300 | 100
```
# Output data

Output file consist possibly best combination of vaccine orders, for example:
```
Post-Covid Sp. z o.o.    -> CentMedEko Centrala [Koszt = 450 * 80.0 = 36000.00 zł]
BioTech 2.0              -> CentMedEko 24h [Koszt = 150 * 70.0 = 10500.00 zł]
Eko Polska 2020          -> CentMedEko 24h [Koszt = 540 * 80.0 = 43200.00 zł]
BioTech 2.0              -> CentMedEko Nowogrodzka [Koszt = 750 * 90.99 = 68242.50 zł]
Eko Polska 2020          -> CentMedEko Nowogrodzka [Koszt = 450 * 70.0 = 31500.00 zł]

Opłaty całkowite: 189442.50 zł
```
